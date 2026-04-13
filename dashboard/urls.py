from django.urls import path
from .views import dashboard_hms_ai, dashboard_home
    
urlpatterns = [
    path('', dashboard_home),
    path('ai/', dashboard_hms_ai)
]