from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.contrib.auth.models import User

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")

class CustomLoginView(LoginView):
    template_name = "users/login.html"
    redirect_authenticated_user = True

# class CustomLogoutView(LogoutView):
#     next_page = reverse_lazy("login")
#
