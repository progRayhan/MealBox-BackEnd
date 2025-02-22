from django.contrib import admin
from meal_manager.models import MealRate, MealTracker


@admin.register(MealRate)
class MealRateAdmin(admin.ModelAdmin):
    list_display = ("vendor_name", "vendor_phone", "staff", "meal_rate")
    search_fields = ("vendor_name", "vendor_phone", "staff__name")
    list_filter = ("staff",)
    ordering = ("vendor_name",)
    list_per_page = 30


@admin.register(MealTracker)
class MealTrackerAdmin(admin.ModelAdmin):
    list_display = ("staff", "employee", "order_datetime", "payment_status", "meal_rate", "deliver_status", "created_at")
    search_fields = ("staff__name", "employee__name", "meal_rate__vendor_name")
    list_filter = ("payment_status", "deliver_status", "order_datetime")
    ordering = ("-order_datetime",)
    list_per_page = 30
