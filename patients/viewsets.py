from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import PatientSerializer, InsuranceSerializer, MedicalRecordSerializer
from .models import Patient, Insurance, MedicalRecord


class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

    @action(["GET"], detail=True, url_path="medical-history")
    def get_medical_report(self, request, pk):
        # Devuelve el paciente seleccionado de acuerdo a su id=pk
        patient = self.get_object()
        return Response(
            {"status": patient.medical_history}
        )  # devolvemos como respuesta el campo de "medical_history" definido en el modelo Patient"


class InsuranceViewSet(viewsets.ModelViewSet):
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()


class MedicalRecordViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()
