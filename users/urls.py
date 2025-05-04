# from django.urls import path
# from .views import register_view, login_view, logout_view
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.urls import path
from .views import RegisterView, CustomLoginView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(template_name='users/login.html'), name="login"),
    path("logout/", LogoutView.as_view(next_page=reverse_lazy('login')), name="logout"),
]

# urlpatterns = [
#     path('register/', register_view, name='register'),
#     path('login/', login_view, name='login'),
#     path('logout/', logout_view, name='logout'),
# ]
