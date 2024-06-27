from django import forms
from .models import StudentRegistration, Course

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = StudentRegistration
        fields = [
            'full_name',
            'student_id',
            'phone_number',
            'session',
            'bank_payment_status',
            'bank_slip_serial_number',
            'payment_date',
            'student_status',
            'courses',
        ]
        widgets = {
            'courses': forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['courses'].queryset = Course.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        student_status = cleaned_data.get("student_status")
        courses = cleaned_data.get("courses")

        if student_status == 'regular' and courses.count() != 7:
            raise forms.ValidationError("Regular students must select all courses.")
        
        if student_status == 'improvement' and courses.count() == 0:
            raise forms.ValidationError("Improvement students must select at least one course.")

        return cleaned_data
