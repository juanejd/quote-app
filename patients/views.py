from .serializers import PatientSerializer, InsuranceSerializer, MedicalRecordSerializer
from .models import Patient, Insurance, MedicalRecord

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

# GET /api/patients => Listar
# POST /api/patients => Crear
# GET /api/patients/<pk> => Detalle
# PUT /api/patients/<pk> => Modificacion
# DELETE /api/patients/<pk> => Borrar


# Vista basada en clases genericas, ListAPIView para el get y CreateAPIView para el post
class ListPatientsView(ListAPIView, CreateAPIView):
    # parametros a usar en los metodos GET y POST
    allowed_methods = ["GET", "POST"]  # Metodos permitidos
    serializer_class = PatientSerializer  # Serializer a utilizar
    queryset = Patient.objects.all()  # Query que se envia a la base de datos


# Vista basada en clase genericas, RetrieveAPIView get cada pk, UpdateAPIView para el put y   DestroyAPIView para el delete
class DetailPatientView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ["GET", "PUT", "DELETE"]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class ListInsuranceView(ListAPIView, CreateAPIView):
    allowed_methods = ["GET", "POST"]
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()


class DetailInsuranceView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ["GET", "PUT", "DELETE"]
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()


class ListMedicalRecordView(ListAPIView, CreateAPIView):
    allowed_methods = ["GET", "POST"]
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()


class DetailMedicalRecordView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ["GET", "PUT", "DELETE"]
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()
