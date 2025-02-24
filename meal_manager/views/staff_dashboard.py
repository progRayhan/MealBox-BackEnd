from django.shortcuts import render
from django.views import View
from meal_manager.models import MealTracker
from meal_user.models import Staff
from _applibs.choice_fields import DeliverStatus

from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.utils import timezone
from datetime import timedelta


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
        staff_phone = "01942531394" # Todo: get phone from token

        today_start = timezone.localdate()
        today_end = today_start + timedelta(days=1)
        query = request.GET.get('q', '')

        if query:
            staff_meals = MealTracker.objects.filter(
                id=query, 
                order_datetime__gte=today_start, 
                order_datetime__lt=today_end
            )
        else:
            staff_meals = MealTracker.objects.filter(
                staff__phone_number=staff_phone, 
                deliver_status=DeliverStatus.PENDING,
                order_datetime__gte=today_start, 
                order_datetime__lt=today_end
            )
        
        context = {
            "staff_meals": staff_meals
        }
        
        return render(request, "orders.html", context)


class MealsView(View):
    def get(self, request):
        return render(request, 'meals.html')


class SettingsView(View):
    def get(self, request):
        return render(request, 'settings.html')
    

class CancelOrderView(View):
    def post(self, request, *args, **kwargs):
        order_id = request.POST.get("order_id")

        if order_id:
            order = get_object_or_404(MealTracker, id=order_id)
            order.deliver_status = DeliverStatus.CANCEL
            order.save()
            return redirect(request.META.get("HTTP_REFERER", "/"))  # Redirect back to previous page
        
        return JsonResponse({"error": "Order ID is required"}, status=400)

    def get(self, request, *args, **kwargs):
        return JsonResponse({"error": "Invalid request"}, status=405)
    