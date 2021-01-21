from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('', views.index),
    path('new_schema/', views.new_schema),
    path('my_schemas/', views.schemas_list),
    path('generate_data/', views.generate_data),
    path('my_tasks/', views.tasks_list),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
