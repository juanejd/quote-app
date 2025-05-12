from rest_framework import serializers
from datetime import date

from .models import Patient, Insurance, MedicalRecord


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"

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
