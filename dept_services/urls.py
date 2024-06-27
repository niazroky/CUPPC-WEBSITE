from django.urls import path
from . import views

urlpatterns = [
    path('', views.dept_services_home, name='dept_services_home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
