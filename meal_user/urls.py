from django.urls import path
from meal_user.views import LoginView, StaffDashboardView, OrdersView, MealsView, SettingsView, CancelOrderView

urlpatterns = [
    path(
        route="login/", 
        view=LoginView.as_view(), 
        name="login",
    ),
    path(
        route="staff/dashboard/",
        view=StaffDashboardView.as_view(), 
        name="staff_dashboard",
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
    path(
        route='cancel-order/', 
        view=CancelOrderView.as_view(), 
        name='cancel_order'
    ),
]
