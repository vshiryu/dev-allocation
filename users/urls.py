from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserRegisterView, UserLoginView

urlpatterns = [
    path('users/register/', UserRegisterView.as_view(), name='register'),
    path('users/login/', UserLoginView.as_view(), name='login'),
]
