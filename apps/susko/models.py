from django.db import models, transaction

from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

from apps.core.helpers import RandomFileName


class SectionQuerySet(models.QuerySet):
    """Queryset helpers shared by the manager and by related managers."""

    def public(self):
        return self.filter(public=True)

    def ordered(self):
        return self.order_by("order", "id")


class SectionManager(models.Manager.from_queryset(SectionQuerySet)):
    """Manager holding the logic needed to render the single Šuško page."""

    def visible(self):
        """All sections that should end up on the page, in display order."""
        return self.public().ordered()

    def main_section(self):
        """
        The section rendered on top of the page.

        It is an ordinary section flagged with ``is_main``. When nothing is
        flagged (for instance right after the first section was created) the
        first section in the display order is used, so the page always has a
        top section.
        """
        visible = self.visible()
        return visible.filter(is_main=True).first() or visible.first()

    def other_sections(self):
        """Every visible section except the main one, in display order."""
        main_section = self.main_section()
        visible = self.visible()

        if main_section is None:
            return visible

        return visible.exclude(pk=main_section.pk)

    def next_order(self):
        """The order value placing a new section at the bottom of the page."""
        last_order = self.aggregate(models.Max("order"))["order__max"]
        return (last_order or 0) + 1

    def normalize_order(self):
        """Rewrite the order values so they are sequential (1, 2, 3, ...)."""
        with transaction.atomic():
            sections = self.ordered().only("pk", "order")
            for position, section in enumerate(sections, start=1):
                if section.order != position:
                    self.filter(pk=section.pk).update(order=position)


class Section(models.Model):
    """A single block of the Šuško page: a title, a text and maybe an image."""

    title = models.CharField(max_length=255)
    text = RichTextUploadingField(
        blank=True,
        default="",
        help_text="Rich text, images can be uploaded straight into the editor.",
    )
    image = models.ImageField(
        upload_to=RandomFileName("images/"),
        blank=True,
        null=True,
        default=None,
        help_text="Optional image shown next to the text.",
    )
    image_thumbnail = ImageSpecField(
        source="image",
        processors=[ResizeToFit(800, 500)],
        format="JPEG",
        options={"quality": 75},
    )
    is_main = models.BooleanField(
        default=False,
        verbose_name="main section",
        help_text="The section shown on top of the page, with a bigger title.",
    )
    public = models.BooleanField(default=True)
    order = models.PositiveIntegerField(
        default=0,
        db_index=True,
        help_text="Sections are shown from the smallest to the biggest value.",
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    objects = SectionManager()

    class Meta:
        db_table = "susko_sections"
        ordering = ("order", "id")
        verbose_name = "Šuško section"
        verbose_name_plural = "Šuško sections"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        adding = self._state.adding

        with transaction.atomic():
            if adding and not self.order:
                self.order = type(self).objects.next_order()

            super().save(*args, **kwargs)

            if self.is_main:
                # Only a single section can be the main one.
                type(self).objects.filter(is_main=True).exclude(pk=self.pk).update(
                    is_main=False
                )

    # -- ordering helpers ------------------------------------------------
    def _move(self, offset):
        """Swap this section with the one ``offset`` places away from it."""
        manager = type(self).objects

        with transaction.atomic():
            manager.normalize_order()
            self.refresh_from_db()

            sections = list(manager.ordered())
            position = [section.pk for section in sections].index(self.pk)
            target = position + offset

            if target < 0 or target >= len(sections):
                return False

            neighbour = sections[target]
            manager.filter(pk=self.pk).update(order=neighbour.order)
            manager.filter(pk=neighbour.pk).update(order=self.order)
            self.refresh_from_db()

        return True

    def move_up(self):
        """Move the section one place towards the top of the page."""
        return self._move(-1)

    def move_down(self):
        """Move the section one place towards the bottom of the page."""
        return self._move(1)
