from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path(
        route='admin/', 
        view=admin.site.urls,
        name="admin",
    ),
    path(
        route='meal/',
        view=include("meal_manager.urls"),
        name="meal_manager",
    )
]

if settings.DEBUG:
    urlpatterns += [
        path(
            route="__debug__/", 
            view=include("debug_toolbar.urls"),
            name="debug_toolbar",
        ),
    ]
