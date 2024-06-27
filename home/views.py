from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def dept_services(request):
    return render(request, 'home/dept_services.html')
