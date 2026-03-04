from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Base

def Baseviews(request):
    base = Base.objects.first()

    if request.method == "POST":
        username = (request.POST.get("username") or "").strip()
        password = (request.POST.get("password") or "").strip()

        if len(username) < 5:
            messages.error(request, "Username kam. Kamida 5 ta kiriting!")
            return redirect("base")
        
        if not password:
            messages.error(request, "Parolni kiriting!")
            return redirect("base")
        
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Username yoki password xato!")
            return redirect("base")

        login(request, user)
        messages.success(request, "Muvaffaqiyatli kirdingiz!")
        return redirect("home")

    return render(request, 'base.html', {"base": base})