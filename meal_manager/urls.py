from django.urls import path
from meal_manager.views.staff_dashboard import DashboardView, OrdersView, MealsView, SettingsView, CancelOrderView

urlpatterns = [
    path(
        route='dashboard/', 
        view=DashboardView.as_view(), 
        name='staff_dashboard',
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
