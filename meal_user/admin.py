from django.contrib import admin
from meal_user.models import Employee, Staff


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "email", "gender", "office", "status")
    search_fields = ("name", "phone_number", "email")
    list_filter = ("gender", "status", "office")
    ordering = ("name",)
    list_per_page = 30


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "email", "employee", "office")
    search_fields = ("name", "phone_number", "email", "employee__phone_number")
    list_filter = ("office",)
    ordering = ("name",)
    list_per_page = 30
