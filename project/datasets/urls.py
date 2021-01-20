from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('', views.index),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view())
]
