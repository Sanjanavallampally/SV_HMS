from django.urls import path
from .views import doctor_create, doctor_list, doctor_delete, doctor_edit
  
urlpatterns = [
      path('', doctor_list, name='doctor_list'),
      path('<int:pk>/edit/', doctor_edit, name='doctor_edit'),
      path('create/', doctor_create, name='doctor_create'),
      path('<int:pk>/delete/', doctor_delete, name='doctor_delete')
]