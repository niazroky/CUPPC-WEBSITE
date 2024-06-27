from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm
from .models import StudentRegistration, Course
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

@login_required
def register_exam(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save()
            request.session['registration_id'] = registration.id
            return redirect('dept_services_home')
    else:
        form = StudentRegistrationForm()
    return render(request, 'exam_registration/student_register.html', {'form': form})

@login_required
def download_registration_details(request, registration_id):
    registration = StudentRegistration.objects.get(id=registration_id)
    html_string = render_to_string('exam_registration/registration_details.html', {'registration': registration})

    response = HttpResponse(html_string, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename=registration_{registration.student_id}.html'
    return response

@login_required
def dashboard(request):
    registrations = StudentRegistration.objects.all()[:3]  # Displaying only the first 3 for the dashboard
    summary = {
        'total_students': StudentRegistration.objects.count(),
        'total_regular_students': StudentRegistration.objects.filter(student_status='regular').count(),
        'total_improvement_students': StudentRegistration.objects.filter(student_status='improvement').count(),
        'course_counts': {f'PHYS-30{i}': StudentRegistration.objects.filter(courses__name=f'PHYS-30{i}').count() for i in range(1, 8)}
    }
    return render(request, 'exam_registration/dashboard.html', {'registrations': registrations, 'summary': summary})
