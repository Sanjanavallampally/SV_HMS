from django.urls import path
from .views import home, contact

urlpatterns = [
    path('', home),
    path('contact/', contact)
]