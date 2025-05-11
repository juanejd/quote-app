from django.urls import path

from rest_framework.routers import DefaultRouter

from .viewsets import PatientViewSet, InsuranceViewSet, MedicalRecordViewSet

# Instanciar objeto
router = DefaultRouter()

# Registrar URLS
router.register("patients", PatientViewSet)
router.register("insurances", InsuranceViewSet)
router.register("medical-records", MedicalRecordViewSet)

urlpatterns = router.urls
