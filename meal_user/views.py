from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from meal_user.models import Staff


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if isinstance(user, Staff):
                return redirect("staff_dashboard")
            else:
                return redirect("user_dashboard")

        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")
