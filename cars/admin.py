from django.contrib import admin
from django.utils.html import format_html
from .models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = (
    'id',
        'thumbnail',
        'car_title',
        'city',
        'color',
        'model',
        'year',
        'body_style',
        'fuel_type',
        'is_featured',
    )
    list_display_links = (
    'id','thumbnail','car_title'
    )
    list_filter = ('city','model','body_style','fuel_type',)
    list_editable=('is_featured',)
    search_fields = ('id','car_title','city','model','body_style','fuel_type',)
    def thumbnail(self, obj):
        if obj.car_photo:
            return format_html(
                '<img src="{}" width="40" style="border-radius:4px;" />',
                obj.car_photo.url
            )
        return "—"

    thumbnail.short_description = "Car Image"


admin.site.register(Car, CarAdmin)
