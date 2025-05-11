from django.urls import path

from rest_framework.routers import DefaultRouter
from .viewsets import AppointmentViewSet, MedicalNoteViewSet

# Instanciamos objeto
router = DefaultRouter()

# Registrar URLS
router.register("appointments", AppointmentViewSet)
router.register("medical-notes", MedicalNoteViewSet)

urlpatterns = router.urls
