# dept_services/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'is_student', 'is_teacher')

    def clean(self):
        cleaned_data = super().clean()
        is_student = cleaned_data.get("is_student")
        is_teacher = cleaned_data.get("is_teacher")
        if is_student and is_teacher:
            raise forms.ValidationError("A user cannot be both a student and a teacher.")
        return cleaned_data
