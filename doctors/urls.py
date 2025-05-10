from django.urls import path
from .views import (
    ListDoctorView,
    DetailDoctorView,
    ListDepartmentView,
    DetailDepartmentView,
    ListDoctorAvailabilityView,
    DetailDoctorAvailabilityView,
)

from rest_framework.routers import DefaultRouter
from .viewsets import DoctorViewSet, DepartmentViewSet, DoctorAvailabilityViewSet

# Nos permite agregar las viewsets
router = DefaultRouter()
# registrar viewsets
router.register("doctors", DoctorViewSet)
router.register("department", DepartmentViewSet)
router.register("doctor_availabilities", DoctorAvailabilityViewSet)

urlpatterns = router.urls
