import json

from django.contrib import admin, messages
from django.db import transaction
from django.http import JsonResponse
from django.urls import path, reverse

from .models import Section


class SectionAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_main", "public", "date_modified")
    list_display_links = ("title",)
    list_editable = ("order", "is_main", "public")
    list_filter = ("public", "is_main")
    search_fields = ("title", "text")
    ordering = ("order", "id")
    actions = ("move_up", "move_down")
    fields = ("title", "text", "image", "is_main", "public", "order")

    class Media:
        js = ("susko/js/susko_admin_reorder.js",)

    # -- actions ---------------------------------------------------------
    @admin.action(description="Move selected sections up")
    def move_up(self, request, queryset):
        moved = 0
        # Start from the top so selected sections keep their relative order.
        for section in queryset.order_by("order", "id"):
            if section.move_up():
                moved += 1

        self.message_user(
            request, f"Moved {moved} section(s) up.", level=messages.INFO
        )

    @admin.action(description="Move selected sections down")
    def move_down(self, request, queryset):
        moved = 0
        # Start from the bottom so selected sections keep their relative order.
        for section in queryset.order_by("-order", "-id"):
            if section.move_down():
                moved += 1

        self.message_user(
            request, f"Moved {moved} section(s) down.", level=messages.INFO
        )

    # -- drag & drop reordering -----------------------------------------
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "reorder/",
                self.admin_site.admin_view(self.reorder_view),
                name="susko_section_reorder",
            ),
        ]
        return custom_urls + urls

    def reorder_view(self, request):
        """Persist a new order, used by the drag & drop of the changelist."""
        if request.method != "POST":
            return JsonResponse({"error": "Only POST is allowed."}, status=405)

        if not self.has_change_permission(request):
            return JsonResponse({"error": "Permission denied."}, status=403)

        try:
            payload = json.loads(request.body.decode("utf-8") or "{}")
        except (ValueError, UnicodeDecodeError):
            return JsonResponse({"error": "Invalid payload."}, status=400)

        ids = payload.get("ids") or []

        if not isinstance(ids, list) or not ids:
            return JsonResponse({"error": "No sections given."}, status=400)

        try:
            ids = [int(pk) for pk in ids]
        except (TypeError, ValueError):
            return JsonResponse({"error": "Invalid section id."}, status=400)

        known_ids = set(
            Section.objects.filter(pk__in=ids).values_list("pk", flat=True)
        )

        if len(known_ids) != len(set(ids)):
            return JsonResponse({"error": "Unknown section id."}, status=400)

        with transaction.atomic():
            for position, pk in enumerate(ids, start=1):
                Section.objects.filter(pk=pk).update(order=position)

        return JsonResponse({"ok": True, "ids": ids})


admin.site.register(Section, SectionAdmin)
