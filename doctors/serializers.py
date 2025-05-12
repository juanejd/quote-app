from rest_framework import serializers

from .models import Doctor, Department, DoctorAvailability


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"

    # Validación personalizada en los doctores, donde el correo debe contener el dominio @example.com
    def validate_email(self, value):
        if "@example.com" in value:
            return value
        # usamos un raise de serializer "ValidationError"
        raise serializers.ValidationError("El correo debe incluir @example.com")

    # Validación personalizada con múltiples campos, en este caso el 'contact_number' y el 'is_on_vacation'
    def validate(self, attrs):
        # attrs = donde almacenamos los campos de la tabla 'doctors'
        if len(attrs["contact_number"]) < 10 and attrs["is_on_vacation"]:
            raise serializers.ValidationError(
                "Por favor, ingrese un numero antes de irte a vacaciones"
            )
        return super().validate(attrs)


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAvailability
        fields = "__all__"
