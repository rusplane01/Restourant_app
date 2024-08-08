from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView


class RegisterView(CreateView):
    model = User
    template_name = "auth_sys/register.html"
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(reverse_lazy("main:home"))


class CustomLoginView(LoginView):
    model = User
    template_name = "auth_sys/login_form.html"
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    reverse_lazy("main:home")