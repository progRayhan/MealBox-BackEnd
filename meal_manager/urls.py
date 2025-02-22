from django.urls import path
from meal_manager.views.staff_dashboard import StaffDashboardView

urlpatterns = [
    path(
        route='dashboard/', 
        view=StaffDashboardView.as_view(), 
        name='staff_dashboard',
    ),
]
