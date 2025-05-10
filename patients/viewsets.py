from rest_framework import viewsets

from .serializers import PatientSerializer, InsuranceSerializer, MedicalRecordSerializer
from .models import Patient, Insurance, MedicalRecord


class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class InsuranceViewSet(viewsets.ModelViewSet):
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()


class MedicalRecordViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()
