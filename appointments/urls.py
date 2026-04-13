from django.urls import path
from .views import appointment_create, appointment_delete, appointment_edit, appointment_list,doctor_appointments

urlpatterns = [
    path('', appointment_list),
    path('<int:pk>/delete/',appointment_delete),
    path('<int:pk>/edit/',appointment_edit),
    path('create/', appointment_create),
    path('doctor/', doctor_appointments)
]