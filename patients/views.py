from .serializers import PatientSerializer
from .models import Patient

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# GET /api/patients => Listar
# POST /api/patients => Crear
# GET /api/patients/<pk> => Detalle
# PUT /api/patients/<pk> => Modificacion
# DELETE /api/patients/<pk> => Borrar

# Vista basada en clase
class ListPatientsView(APIView):
    allowed_methods = ['GET', 'POST']


    def get(self, request):
        patients = Patient.objects.all() # Obtenemos todos los pacientes
        serializer = PatientSerializer(patients, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PatientSerializer(data=request.data) # Validar informacion digitada por el usuario
        serializer.is_valid(raise_exception=True) # con raise exception mostrarmos el error generado en formato json en caso de que la data haya sido ingresada incorrectamente
        serializer.save() # Guardamos
        return Response(status=status.HTTP_201_CREATED)

# vista basada en clase
class DetailPatientView(APIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']

    def get(self, request, pk):
        # Creamos un try-except en caso de que no exista el usuario solicitado
        try:
            patient = Patient.objects.get(id=pk) # Query para acceder a la informacion de 1 paciente con su id
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)# En caso de que no exista Lanzamos un error 404 not_found 
        serializer = PatientSerializer(patient) # Si existe el usuario, usamos la data de ese paciente dentro del serializer
        return Response(serializer.data) # retornar la data en formato json
    
    def put(self, request, pk):
        try:
            patient = Patient.objects.get(id=pk) 
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            patient = Patient.objects.get(id=pk) 
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Decorador para que django rest sea compatible con la vista
# @api_view(['GET', 'POST']) #solo es compatible con el get para no usar esta misma vista en otra url
# def list_patients(request):
#     if request.method == 'GET':
#       patients = Patient.objects.all()
#       serializer = PatientSerializer(patients, many = True)
#       return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = PatientSerializer(data=request.data) # Validar informacion digitada por el usuario
#         serializer.is_valid(raise_exception=True) # con raise exception mostrarmos el error generado en formato json en caso de que la data haya sido ingresada incorrectamente
#         serializer.save() # Guardamos
#         return Response(status=status.HTTP_201_CREATED) # Mostramos que se creo un nuevo paciente



# Modificando datos de un paciente especifico
# @api_view(['GET', 'PUT', 'DELETE'])
# def detail_patient(request, pk):
#     # Creamos un try-except en caso de que no exista el usuario solicitado
#     try:
#         patient = Patient.objects.get(id=pk) # Query para acceder a la informacion de 1 paciente con su id
#     except Patient.DoesNotExist:
#       # En caso de que no exista Lanzamos un error 404 not_found
#       return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = PatientSerializer(patient) # Si existe el usuario, usamos la data de ese paciente dentro del serializer
#         return Response(serializer.data) # retornar la data en formato json
    
#     if request.method == 'PUT':
#       serializer = PatientSerializer(patient, data=request.data)
#       if serializer.is_valid(raise_exception=True):
#           serializer.save()
#           return Response(serializer.data, status=status.HTTP_201_CREATED)
#       return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'DELETE':
#         patient.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)