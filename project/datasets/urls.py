from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('', views.index),
    path('new_schema/', views.new_schema),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view())
]
