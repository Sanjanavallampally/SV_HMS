from django.db import models
 # Create your models here.
class Appointment(models.Model):
      patient = models.ForeignKey('patients.patient',on_delete=models.CASCADE)
      doctor = models.ForeignKey('doctors.doctor',on_delete=models.CASCADE)
      appointment_time = models.DateTimeField()
      appointment_status = models.CharField(max_length=100)
def __str__(self):
      return f"{self.patient} - {self.doctor}"