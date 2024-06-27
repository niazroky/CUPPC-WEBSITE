# main urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('dept_services/', include('dept_services.urls')),
    path('exam_registration/', include('exam_registration.urls')),
]
