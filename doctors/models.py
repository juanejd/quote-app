from django.db import models

# Tabla doctor
class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    biography = models.TextField()

# Tabla departamento
class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

# Tabla disponibilidad del doctor
class DoctorAvailability(models.Model):
    doctor = models.ForeignKey(Doctor, related_name= 'medical_notes', on_delete=models.CASCADE)
    note = models.TextField()
    date = models.DateField()