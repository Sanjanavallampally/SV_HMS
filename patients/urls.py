from django.urls import path
from .views import patient_create, patient_delete, patient_list, patient_edit
  
urlpatterns = [
      path('',patient_list),
      path('<int:pk>/edit/', patient_edit),
      path('<int:pk>/delete/', patient_delete),
      path('create/', patient_create)

]