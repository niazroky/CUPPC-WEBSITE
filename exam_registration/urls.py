# exam_registration/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_exam, name='register_exam'),
    path('download_registration_details/<int:registration_id>/', views.download_registration_details, name='download_registration_details'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
