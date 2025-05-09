from .serializers import PatientSerializer
from .models import Patient

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Decorador para que django rest sea compatible con la vista
@api_view(["GET"]) #solo es compatible con el get para no usar esta misma vista en otra url
def list_patients(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many = True)
    return Response(serializer.data)

# Decorador para el POST
@api_view(["POST"])
def create_patient(request):
    serializer = PatientSerializer(data=request.data) # Deserializar los datos enviados por el cliente
    if serializer.is_valid(): # Verificar si los datos son válidos
        serializer.save() # Guardar el nuevo paciente en la base de datos
        return Response(serializer.data, status=status.HTTP_201_CREATED) # Devolver los datos del paciente creado
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Si hay errores, devolverlos