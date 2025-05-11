from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import (
    DoctorSerializer,
    DepartmentSerializer,
    DoctorAvailabilitySerializer,
)
from .models import Doctor, Department, DoctorAvailability
from .permissions import IsDoctor


# Generamos URL de doctor (crear,modificar,listar y actualizar)
class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsDoctor,
    ]  # todos los endpoints del viewset funcionan solo si esta logueado

    """
    @action es un decorador de DRF que permite crear endpoints personalizados

    ["POST"] indica que solo acepta peticiones POST
    detail=True significa que la acción se aplica a un objeto específico (requiere ID)
    
    url_path="set-on-vacation" define la URL del endpoint como /doctors/{id}/set-on-vacation/
    """

    @action(["POST"], detail=True, url_path="set-on-vacation")
    def set_on_vacation(self, request, pk):
        # self.get_object() obtiene el doctor específico basado en el ID (pk)
        doctor = self.get_object()
        doctor.is_on_vacation = True  # Actualiza el estado de vacaciones del doctor
        doctor.save()
        return Response({"status": "El doctor está en vacaciones"})

    # Similar al anterior, pero para quitar el estado de vacaciones
    # La URL será /doctors/{id}/set_off_vacation/
    @action(["POST"], detail=True)
    def set_off_vacation(self, request, pk, url_path="set-off-vacation"):
        doctor = self.get_object()
        doctor.is_on_vacation = False
        doctor.save()
        return Response({"status": "El doctor NO está en vacaciones"})


# Generamos URL de departamento (crear,modificar,listar y actualizar)
class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


# Generamos URL de disponibilidad doctor (crear,modificar,listar y actualizar)
class DoctorAvailabilityViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()
