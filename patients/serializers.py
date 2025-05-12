from rest_framework import serializers
from datetime import date

from .models import Patient, Insurance, MedicalRecord
from bookings.serializers import AppointmentSerializer


class PatientSerializer(serializers.ModelSerializer):

    appointments = AppointmentSerializer(many=True, read_only=True)
    age = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = [
            "id",
            "first_name",
            "last_name",
            "age",
            "date_of_birth",
            "contact_number",
            "email",
            "address",
            "medical_history",
            "appointments",
        ]

    def get_age(self, obj):
        age_td = date.today() - obj.date_of_birth
        year = age_td.days // 365
        return f"{year} años"

    def validate_date_of_birth(self, value):
        """
        Valida que la fecha de nacimiento no sea futura
        """
        today = date.today()
        if value > today:
            raise serializers.ValidationError(
                "La fecha de nacimiento no puede ser una fecha futura"
            )
        return value

    def validate_address(self, value):
        """
        Validamos que la direccion sea mayor a 5 caracteres
        """
        if len(value.strip()) < 5:
            raise serializers.ValidationError(
                "La dirección debe tener al menos 5 caracteres"
            )
        return value


class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = "__all__"


class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = "__all__"
