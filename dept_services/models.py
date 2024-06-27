# dept_services/models.py

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models

class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    def clean(self):
        super().clean()
        if self.is_student and self.is_teacher:
            raise ValidationError("A user cannot be both a student and a teacher.")

    def __str__(self):
        return self.username
