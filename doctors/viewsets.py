from rest_framework import viewsets

from .serializers import (
    DoctorSerializer,
    DepartmentSerializer,
    DoctorAvailabilitySerializer,
)
from .models import Doctor, Department, DoctorAvailability


# Generamos URL de doctor (crear,modificar,listar y actualizar)
class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


# Generamos URL de departamento (crear,modificar,listar y actualizar)
class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


# Generamos URL de disponibilidad doctor (crear,modificar,listar y actualizar)
class DoctorAvailabilityViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()
