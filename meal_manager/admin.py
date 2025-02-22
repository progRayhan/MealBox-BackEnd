from django.contrib import admin
from meal_manager.models import MealRate


@admin.register(MealRate)
class MealRateAdmin(admin.ModelAdmin):
    list_display = ("vendor_name", "vendor_phone", "staff", "meal_rate")
    search_fields = ("vendor_name", "vendor_phone", "staff__name")
    list_filter = ("staff",)
    ordering = ("vendor_name",)
    list_per_page = 30
