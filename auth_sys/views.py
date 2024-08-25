from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.views.generic import CreateView

class CustomLoginView(LoginView):
    template_name = "auth_sys/login.html"
    redirect_authenticated_user = True


def logout_view(request):
    logout(request)            
    return HttpResponseRedirect('/')


class RegisterView(CreateView):
    template_name = "auth_sys/register.html"
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(reverse_lazy("auth_sys:login"))