from django.urls import path

from user import views

urlpatterns = [
    path('test_celery', views.test_celery),
]