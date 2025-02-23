from django.urls import path
from meal_manager.views.staff_dashboard import DashboardView, OrdersView, MealsView, SettingsView

urlpatterns = [
    path(
        route='dashboard/', 
        view=DashboardView.as_view(), 
        name='dashboard',
    ),
    path(
        route='orders/', 
        view=OrdersView.as_view(), 
        name='orders',
    ),
    path(
        route='meals/', 
        view=MealsView.as_view(), 
        name='meals',
    ),
    path(
        route='settings/', 
        view=SettingsView.as_view(), 
        name='settings',
    ),
]
