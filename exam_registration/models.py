from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=10, choices=[
        ('PHYS-301', 'PHYS-301'),
        ('PHYS-302', 'PHYS-302'),
        ('PHYS-303', 'PHYS-303'),
        ('PHYS-304', 'PHYS-304'),
        ('PHYS-305', 'PHYS-305'),
        ('PHYS-306', 'PHYS-306'),
        ('PHYS-307', 'PHYS-307'),
    ])

    def __str__(self):
        return self.name

class StudentRegistration(models.Model):
    FULL_NAME_MAX_LENGTH = 100
    STUDENT_ID_LENGTH = 8
    PHONE_NUMBER_LENGTH = 11

    STATUS_CHOICES = [
        ('regular', 'Regular'),
        ('improvement', 'Improvement'),
    ]

    PAYMENT_STATUS_CHOICES = [
        ('yes', 'Yes'),
        ('not_yet', 'Not Yet'),
    ]

    full_name = models.CharField(max_length=FULL_NAME_MAX_LENGTH)
    student_id = models.CharField(max_length=STUDENT_ID_LENGTH, unique=True)
    phone_number = models.CharField(max_length=PHONE_NUMBER_LENGTH)
    session = models.CharField(max_length=20)
    bank_payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES)
    bank_slip_serial_number = models.CharField(max_length=50)
    payment_date = models.DateField()
    student_status = models.CharField(max_length=12, choices=STATUS_CHOICES)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.full_name
