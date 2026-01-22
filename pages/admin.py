from django.contrib import admin
from django.utils.html import format_html
from .models import Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("id", "thumbnail", "first_name", "designation", "created_date")
    list_display_links = ("id", "thumbnail","first_name")
    search_fields = ("first_name", "last_name", "designation")
    list_filter = ("designation",)  # ✅ must be tuple/list

    @admin.display(description="Photo")
    def thumbnail(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="40" style="border-radius:4px;" />', obj.photo.url)
        return "—"
