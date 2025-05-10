from django.urls import path
from .views import ListPatientsView, DetailPatientView

urlpatterns = [
    path('patients/', ListPatientsView.as_view()), # Endpoint con GET y POST
    path('patients/<int:pk>/', DetailPatientView.as_view()) # Endpoint con GET y PUT para cada usuario
]