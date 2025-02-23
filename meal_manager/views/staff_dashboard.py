from django.shortcuts import render
from django.views import View
from meal_manager.models import MealTracker
from meal_user.models import Staff


class DashboardView(View):
    def get(self, request):
        staff_phone = "01942531394" # Todo: get phone from token

        staff = Staff.objects.filter(phone_number=staff_phone).first()
        staff_meals = MealTracker.objects.filter(staff=staff)
        context = {
            "staff_name": staff.name,
            "total_sales": staff.total_sales,
            "order_completed": staff.order_completed,
            "total_employee": staff.total_employee,
            "staff_meals": staff_meals
        }
        return render(request, "dashboard.html", context)
    

class OrdersView(View):
    def get(self, request):
        return render(request, 'orders.html')


class MealsView(View):
    def get(self, request):
        return render(request, 'meals.html')


class SettingsView(View):
    def get(self, request):
        return render(request, 'settings.html')
    