from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('', views.index),
    path('new_schema/', views.new_schema),
    path('my_schemas/', views.schemas_list),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view())
]
