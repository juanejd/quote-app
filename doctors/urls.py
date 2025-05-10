from django.urls import path
from .views import all_doctors, detail_doctor

urlpatterns = [
    path('doctors/', all_doctors),
    path('doctors/<int:pk>/', detail_doctor)
]