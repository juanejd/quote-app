from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import Doctor, Department, DoctorAvailability
from .serializers import (
    DoctorSerializer,
    DepartmentSerializer,
    DoctorAvailabilitySerializer,
)


class ListDoctorView(ListAPIView, CreateAPIView):
    allowed_methods = ["GET", "POST"]
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class DetailDoctorView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ["GET", "PUT", "DELETE"]
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class ListDepartmentView(ListAPIView, CreateAPIView):
    allowed_methods = ["GET", "POST"]
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class DetailDepartmentView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ["GET", "PUT", "DELETE"]
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class ListDoctorAvailabilityView(ListAPIView, CreateAPIView):
    allowed_methods = ["GET", "POST"]
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()


class DetailDoctorAvailabilityView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ["GET", "PUT", "DELETE"]
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()
