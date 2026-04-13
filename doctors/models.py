from django.db import models
# Create your models here.
class doctor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    specialization = models.CharField(max_length=100)
    rating = models.FloatField(max_length=5)
def __str__(self):
    return self.name