from django.urls import path
from .views import (
    ListDoctorView,
    DetailDoctorView,
    ListDepartmentView,
    DetailDepartmentView,
    ListDoctorAvailabilityView,
    DetailDoctorAvailabilityView,
)

urlpatterns = [
    path("doctors/", ListDoctorView.as_view()),
    path("doctors/<int:pk>/", DetailDoctorView.as_view()),
    path("departments/", ListDepartmentView.as_view()),
    path("departments/<int:id>/", DetailDepartmentView.as_view()),
    path("doctoravailabilities/", ListDoctorAvailabilityView.as_view()),
    path("doctoravailabilities/<int:id>/", DetailDoctorAvailabilityView.as_view()),
]
