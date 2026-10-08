"""
Guards against third-party static files being vendored into ``static/``.

``STATICFILES_DIRS`` (``static/``) is searched before the static folders of the
installed apps, both by the dev server and by ``collectstatic``. A copy of, say,
CKEditor that is committed into ``static/`` therefore silently replaces the one
shipped by the installed package -- even when the two are years apart, which
ends with a half-broken editor in the admin (missing toolbar icons, ...).
"""

import pathlib

from django.conf import settings
from django.contrib.staticfiles import finders
from django.contrib.staticfiles.finders import (
    AppDirectoriesFinder,
    FileSystemFinder,
)
from django.test import SimpleTestCase

import ckeditor

CKEDITOR_SPRITES = (
    "ckeditor/ckeditor/plugins/icons.png",
    "ckeditor/ckeditor/skins/moono-lisa/icons.png",
)


def project_static_files():
    """Every file living in one of the STATICFILES_DIRS, as relative paths."""
    for static_dir in settings.STATICFILES_DIRS:
        root = pathlib.Path(static_dir)

        for path in root.rglob("*"):
            if path.is_file():
                yield root, path.relative_to(root).as_posix()


class StaticFilesShadowingTests(SimpleTestCase):
    def test_project_static_does_not_shadow_installed_apps(self):
        """``static/`` must only hold assets that belong to this project."""
        app_finder = AppDirectoriesFinder()
        shadowed = []

        for root, relative_path in project_static_files():
            if app_finder.find(relative_path):
                shadowed.append(f"{root}/{relative_path}")

        self.assertEqual(
            shadowed,
            [],
            "These files hide assets shipped by an installed package. Delete "
            "them from static/ and let collectstatic gather them from the "
            f"package instead: {shadowed[:10]}",
        )

    def test_file_system_finder_runs_before_the_app_finder(self):
        """The assumption the test above is built on."""
        finder_classes = [finder.__class__ for finder in finders.get_finders()]

        self.assertLess(
            finder_classes.index(FileSystemFinder),
            finder_classes.index(AppDirectoriesFinder),
        )


class CKEditorAssetsTests(SimpleTestCase):
    def test_ckeditor_is_served_from_the_installed_package(self):
        package_root = pathlib.Path(ckeditor.__file__).parent

        for asset in ("ckeditor/ckeditor-init.js", "ckeditor/ckeditor/ckeditor.js"):
            with self.subTest(asset=asset):
                found = finders.find(asset)

                self.assertIsNotNone(found, f"{asset} is not collectable at all")
                self.assertTrue(
                    pathlib.Path(found).is_relative_to(package_root),
                    f"{asset} is served from {found} instead of the "
                    "django-ckeditor package",
                )

    def test_toolbar_icon_sprites_are_usable(self):
        """Empty sprites are what makes the toolbar buttons look blank."""
        for sprite in CKEDITOR_SPRITES:
            with self.subTest(sprite=sprite):
                found = finders.find(sprite)

                self.assertIsNotNone(found, f"{sprite} is missing")
                self.assertGreater(
                    pathlib.Path(found).stat().st_size,
                    0,
                    f"{sprite} is empty, the toolbar buttons will be blank",
                )
