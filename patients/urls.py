from django.urls import path
from .views import list_patients, detail_patient

urlpatterns = [
    path('patients/', list_patients), # Endpoint con GET y POST
    path('patients/<int:pk>/', detail_patient) # Endpoint con GET y PUT para cada usuario
]