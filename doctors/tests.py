from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from patients.models import Patient
from doctors.models import Doctor


# validador de appointments copiando el viewset
class DoctorViewSetTests(TestCase):
    # setUp Permite ejecutar codigo antes de iniciar con cada prueba
    def setUp(self):
        # Creamos un paciente y un doctor
        self.patient = Patient.objects.create(
            first_name="Juan",
            last_name="Martinez",
            date_of_birth="1993-12-05",
            contact_number="3163452358",
            email="example@example.com",
            address="Av paralela",
            medical_history="Ninguna",
        )
        self.doctor = Doctor.objects.create(
            first_name="Francis",
            last_name="Kobe",
            qualification="Profesional",
            contact_number="123542412",
            email="example2@example.com",
            address="Minitas",
            biography="Sin",
            is_on_vacation=False,
        )
        # el cliente nos permite simular requests GET,POST, etc
        # APIClient = define valores predeterminados que nos sirven para probar, como probar que lo que se envia es un JSON. Evitando codigo de mas
        self.client = APIClient()

    # Test de prueba el appointments debe retornar un http 200
    def test_list_should_return_200(self):
        # los nombres de las urls las obtenemos de ./manage.py show_urls
        # Obtenemos las urls de los appointments para el 'pk' indicado
        url = reverse("doctor-appointments", kwargs={"pk": self.doctor.id})
        response = self.client.get(url)  # Simulamos un request
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Test
