from django.shortcuts import render
from django.views import View
from meal_manager.models import MealTracker


class StaffDashboardView(View):
    def get(self, request):
        staff_phone = "01942531394" # Todo: get phone from token

        staff_meals = MealTracker.objects.filter(staff__phone_number=staff_phone)
        context = {
            "total_sales": 1500,
            "order_completed": 150,
            "total_employee": 50,
            "staff_meals": staff_meals
        }
        return render(request, "dashboard.html", context)
