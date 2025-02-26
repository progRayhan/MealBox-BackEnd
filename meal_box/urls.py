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
        route='',
        view=include("meal_user.urls"),
        name="meal_user",
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
