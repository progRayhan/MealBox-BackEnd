from django.contrib import admin
from meal_user.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "email", "gender", "office", "status")
    search_fields = ("name", "phone_number", "email")
    list_filter = ("gender", "status", "office")
    ordering = ("name",)
    list_per_page = 30
