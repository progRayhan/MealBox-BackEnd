from django import urls
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from meal_manager.models import MealTracker
from _applibs.choice_fields import DeliverStatus

from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta

from meal_user.models import Staff


class LoginView(View):
    template_name = "login.html"

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_type = request.POST.get("user_type")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if isinstance(user, Staff):
                return redirect(reverse("staff_dashboard"))
            else:
                return redirect("user_dashboard")

        else:
            messages.error(request, "Invalid username or password")

        return render(request, "login.html")

        
class StaffDashboardView(LoginRequiredMixin, TemplateView):
    login_url = "login"
    template_name = "staff_templetes/dashboard.html"

    # Optional: If you need to pass extra context to the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["welcome_message"] = "Welcome to the Staff Dashboard!"  # Example data
        return context
    

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
        
        return render(request, "staff_templetes/orders.html", context)


class MealsView(View):
    def get(self, request):
        return render(request, 'staff_templetes/meals.html')


class SettingsView(View):
    def get(self, request):
        return render(request, 'staff_templetes/settings.html')
    

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
    