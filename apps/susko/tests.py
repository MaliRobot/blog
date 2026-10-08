import json
import shutil
import tempfile
from io import BytesIO

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.urls import resolve, reverse

from ckeditor_uploader.fields import RichTextUploadingField
from PIL import Image

from apps.susko import views
from apps.susko.admin import SectionAdmin
from apps.susko.models import Section

MEDIA_ROOT = tempfile.mkdtemp(prefix="susko-tests-")


def tearDownModule():
    """Drop the images written by the tests."""
    shutil.rmtree(MEDIA_ROOT, ignore_errors=True)


def make_image(name="susko.png"):
    """A tiny, but real, image usable by ImageField/imagekit."""
    buffer = BytesIO()
    Image.new("RGB", (10, 10), "white").save(buffer, format="PNG")

    return SimpleUploadedFile(name, buffer.getvalue(), content_type="image/png")


class SectionModelTests(TestCase):
    def test_str_is_the_title(self):
        section = Section.objects.create(title="Prva")

        self.assertEqual(str(section), "Prva")

    def test_sections_are_ordered_by_order_then_id(self):
        third = Section.objects.create(title="Third", order=3)
        first = Section.objects.create(title="First", order=1)
        second = Section.objects.create(title="Second", order=2)

        self.assertEqual(list(Section.objects.all()), [first, second, third])

    def test_new_sections_go_to_the_bottom(self):
        first = Section.objects.create(title="First")
        second = Section.objects.create(title="Second")
        third = Section.objects.create(title="Third")

        self.assertEqual([first.order, second.order, third.order], [1, 2, 3])

    def test_explicit_order_is_kept(self):
        section = Section.objects.create(title="Somewhere", order=17)

        self.assertEqual(section.order, 17)
        self.assertEqual(Section.objects.next_order(), 18)

    def test_text_uses_ckeditor_with_image_uploads(self):
        field = Section._meta.get_field("text")

        self.assertIsInstance(field, RichTextUploadingField)

    def test_image_is_optional(self):
        section = Section.objects.create(title="No image")

        self.assertFalse(section.image)

    @override_settings(MEDIA_ROOT=MEDIA_ROOT)
    def test_image_can_be_added(self):
        section = Section.objects.create(title="With image", image=make_image())

        self.assertTrue(section.image)
        self.assertTrue(section.image_thumbnail.url)

    def test_only_one_section_can_be_the_main_one(self):
        first = Section.objects.create(title="First", is_main=True)
        second = Section.objects.create(title="Second", is_main=True)

        first.refresh_from_db()
        second.refresh_from_db()

        self.assertFalse(first.is_main)
        self.assertTrue(second.is_main)
        self.assertEqual(Section.objects.filter(is_main=True).count(), 1)

    def test_flagging_a_section_as_main_does_not_change_the_order(self):
        first = Section.objects.create(title="First")
        second = Section.objects.create(title="Second")

        second.is_main = True
        second.save()
        first.refresh_from_db()
        second.refresh_from_db()

        self.assertEqual([first.order, second.order], [1, 2])


class SectionOrderingTests(TestCase):
    def setUp(self):
        self.first = Section.objects.create(title="First")
        self.second = Section.objects.create(title="Second")
        self.third = Section.objects.create(title="Third")

    def titles(self):
        return list(Section.objects.ordered().values_list("title", flat=True))

    def test_move_up(self):
        self.assertTrue(self.third.move_up())

        self.assertEqual(self.titles(), ["First", "Third", "Second"])

    def test_move_down(self):
        self.assertTrue(self.first.move_down())

        self.assertEqual(self.titles(), ["Second", "First", "Third"])

    def test_move_up_on_first_section_does_nothing(self):
        self.assertFalse(self.first.move_up())

        self.assertEqual(self.titles(), ["First", "Second", "Third"])

    def test_move_down_on_last_section_does_nothing(self):
        self.assertFalse(self.third.move_down())

        self.assertEqual(self.titles(), ["First", "Second", "Third"])

    def test_moving_twice_walks_the_section_to_the_top(self):
        self.third.move_up()
        self.third.move_up()

        self.assertEqual(self.titles(), ["Third", "First", "Second"])

    def test_move_works_when_orders_clash(self):
        Section.objects.update(order=0)
        section = Section.objects.ordered().last()

        self.assertTrue(section.move_up())

        self.assertEqual(self.titles(), ["First", "Third", "Second"])

    def test_normalize_order_makes_the_values_sequential(self):
        Section.objects.filter(pk=self.first.pk).update(order=10)
        Section.objects.filter(pk=self.second.pk).update(order=20)
        Section.objects.filter(pk=self.third.pk).update(order=30)

        Section.objects.normalize_order()

        self.assertEqual(
            list(Section.objects.ordered().values_list("order", flat=True)), [1, 2, 3]
        )

    def test_reordering_changes_the_page_order(self):
        self.third.move_up()
        self.third.move_up()

        response = self.client.get(reverse("susko:susko"))
        content = response.content.decode()

        self.assertLess(content.index("Third"), content.index("First"))


class SectionManagerTests(TestCase):
    def test_public_filters_out_hidden_sections(self):
        public = Section.objects.create(title="Public")
        Section.objects.create(title="Hidden", public=False)

        self.assertEqual(list(Section.objects.public()), [public])

    def test_visible_is_public_and_ordered(self):
        second = Section.objects.create(title="Second", order=2)
        first = Section.objects.create(title="First", order=1)
        Section.objects.create(title="Hidden", order=0, public=False)

        self.assertEqual(list(Section.objects.visible()), [first, second])

    def test_main_section_is_the_flagged_one(self):
        Section.objects.create(title="First")
        main = Section.objects.create(title="Second", is_main=True)

        self.assertEqual(Section.objects.main_section(), main)

    def test_main_section_falls_back_to_the_first_section(self):
        first = Section.objects.create(title="First")
        Section.objects.create(title="Second")

        self.assertEqual(Section.objects.main_section(), first)

    def test_main_section_ignores_hidden_sections(self):
        Section.objects.create(title="Hidden", is_main=True, public=False)
        visible = Section.objects.create(title="Visible")

        self.assertEqual(Section.objects.main_section(), visible)

    def test_main_section_is_none_without_sections(self):
        self.assertIsNone(Section.objects.main_section())

    def test_other_sections_excludes_the_main_one(self):
        Section.objects.create(title="First")
        second = Section.objects.create(title="Second")
        third = Section.objects.create(title="Third")

        self.assertEqual(list(Section.objects.other_sections()), [second, third])

    def test_other_sections_without_sections(self):
        self.assertEqual(list(Section.objects.other_sections()), [])


@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class SuskoPageTests(TestCase):
    def setUp(self):
        self.url = reverse("susko:susko")

    def test_url_is_wired_up(self):
        self.assertEqual(self.url, "/susko/")
        self.assertEqual(resolve("/susko/").func, views.susko)

    def test_url_without_trailing_slash_redirects(self):
        response = self.client.get("/susko")

        self.assertRedirects(response, self.url, status_code=301)

    def test_page_renders(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "susko/susko.html")
        self.assertTemplateUsed(response, "base.html")

    def test_page_title_is_static(self):
        response = self.client.get(self.url)

        self.assertContains(response, "Šuško")
        self.assertContains(response, 'id="susko-title"')

    def test_page_shows_the_menu_of_the_site(self):
        response = self.client.get(self.url)

        self.assertContains(response, 'href="/susko/"')
        self.assertContains(response, 'href="/blog"')

    def test_menu_links_to_susko_from_the_home_page(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'href="/susko/"')
        self.assertContains(response, "Šuško")

    def test_empty_page_does_not_break(self):
        response = self.client.get(self.url)

        self.assertIsNone(response.context["main_section"])
        self.assertEqual(list(response.context["sections"]), [])
        self.assertContains(response, "susko-empty")

    def test_main_section_is_on_top_with_a_bigger_title(self):
        Section.objects.create(title="Below", text="<p>below</p>")
        main = Section.objects.create(title="On top", text="<p>top</p>", is_main=True)

        response = self.client.get(self.url)
        content = response.content.decode()

        self.assertEqual(response.context["main_section"], main)
        self.assertEqual(
            [section.title for section in response.context["sections"]], ["Below"]
        )
        self.assertLess(content.index("On top"), content.index("Below"))
        self.assertInHTML(
            '<h2 class="susko-section-title susko-section-title-main">On top</h2>',
            content,
        )
        self.assertInHTML('<h3 class="susko-section-title">Below</h3>', content)

    def test_sections_are_rendered_in_order(self):
        Section.objects.create(title="Main", is_main=True)
        Section.objects.create(title="Alpha", order=10)
        Section.objects.create(title="Beta", order=20)
        Section.objects.create(title="Gamma", order=30)

        content = self.client.get(self.url).content.decode()

        self.assertLess(content.index("Alpha"), content.index("Beta"))
        self.assertLess(content.index("Beta"), content.index("Gamma"))

    def test_rich_text_is_not_escaped(self):
        Section.objects.create(title="Rich", text="<p><em>hello</em></p>")

        response = self.client.get(self.url)

        self.assertContains(response, "<p><em>hello</em></p>", html=True)

    def test_hidden_sections_are_not_shown(self):
        Section.objects.create(title="Visible")
        Section.objects.create(title="Invisible", public=False)

        response = self.client.get(self.url)

        self.assertContains(response, "Visible")
        self.assertNotContains(response, "Invisible")

    def test_image_is_rendered_when_present(self):
        Section.objects.create(title="Main", is_main=True)
        Section.objects.create(title="With image", image=make_image())

        response = self.client.get(self.url)

        self.assertContains(response, 'class="susko-image"')
        self.assertContains(response, 'alt="With image"')

    def test_no_image_markup_without_an_image(self):
        Section.objects.create(title="Plain")

        response = self.client.get(self.url)

        self.assertNotContains(response, "susko-image")

    def test_everything_is_on_a_single_page(self):
        for index in range(25):
            Section.objects.create(title=f"Section {index}")

        response = self.client.get(self.url)
        content = response.content.decode()

        self.assertNotIn("pagination", content)
        self.assertIsNone(response.context.get("paginator"))
        for index in range(25):
            self.assertIn(f"Section {index}", content)


class SuskoAdminTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.admin_user = User.objects.create_superuser(
            username="admin", email="admin@example.com", password="password"
        )

    def setUp(self):
        self.client.force_login(self.admin_user)
        self.first = Section.objects.create(title="First")
        self.second = Section.objects.create(title="Second")
        self.third = Section.objects.create(title="Third")

    def titles(self):
        return list(Section.objects.ordered().values_list("title", flat=True))

    def test_section_is_registered_in_the_admin(self):
        from django.contrib import admin as django_admin

        self.assertIn(Section, django_admin.site._registry)
        self.assertIsInstance(django_admin.site._registry[Section], SectionAdmin)

    def test_changelist_is_reachable(self):
        response = self.client.get(reverse("admin:susko_section_changelist"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "First")

    def test_add_form_contains_every_editable_field(self):
        response = self.client.get(reverse("admin:susko_section_add"))

        self.assertEqual(response.status_code, 200)
        for field in ("title", "text", "image", "is_main", "public", "order"):
            self.assertContains(response, f'name="{field}"')

    def test_add_form_uses_ckeditor_with_an_upload_url(self):
        response = self.client.get(reverse("admin:susko_section_add"))
        content = response.content.decode()

        self.assertIn("ckeditor", content)
        self.assertIn("filebrowserUploadUrl", content)

    def test_move_up_action(self):
        response = self.client.post(
            reverse("admin:susko_section_changelist"),
            {
                "action": "move_up",
                "_selected_action": [str(self.third.pk)],
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.titles(), ["First", "Third", "Second"])

    def test_move_down_action(self):
        self.client.post(
            reverse("admin:susko_section_changelist"),
            {
                "action": "move_down",
                "_selected_action": [str(self.first.pk)],
            },
            follow=True,
        )

        self.assertEqual(self.titles(), ["Second", "First", "Third"])

    def test_move_down_action_keeps_relative_order_of_selection(self):
        self.client.post(
            reverse("admin:susko_section_changelist"),
            {
                "action": "move_down",
                "_selected_action": [str(self.first.pk), str(self.second.pk)],
            },
            follow=True,
        )

        self.assertEqual(self.titles(), ["Third", "First", "Second"])

    def test_reorder_view_saves_a_new_order(self):
        response = self.client.post(
            reverse("admin:susko_section_reorder"),
            data=json.dumps({"ids": [self.third.pk, self.first.pk, self.second.pk]}),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()["ok"])
        self.assertEqual(self.titles(), ["Third", "First", "Second"])

    def test_reorder_view_rejects_get(self):
        response = self.client.get(reverse("admin:susko_section_reorder"))

        self.assertEqual(response.status_code, 405)

    def test_reorder_view_rejects_broken_payload(self):
        response = self.client.post(
            reverse("admin:susko_section_reorder"),
            data="not json",
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)

    def test_reorder_view_rejects_empty_payload(self):
        response = self.client.post(
            reverse("admin:susko_section_reorder"),
            data=json.dumps({"ids": []}),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)

    def test_reorder_view_rejects_unknown_sections(self):
        response = self.client.post(
            reverse("admin:susko_section_reorder"),
            data=json.dumps({"ids": [self.first.pk, 98765]}),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(self.titles(), ["First", "Second", "Third"])

    def test_reorder_view_needs_a_staff_user(self):
        self.client.logout()

        response = self.client.post(
            reverse("admin:susko_section_reorder"),
            data=json.dumps({"ids": [self.third.pk]}),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 302)
        self.assertIn("/stavka/login/", response["Location"])
        self.assertEqual(self.titles(), ["First", "Second", "Third"])