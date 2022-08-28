from django.db import models

class Familiar(models.Model):
    nombre=models.CharField(max_length=40)
    fecha_nacimiento=models.DateField()
    edad=models.IntegerField()
    parentesco=models.CharField(max_length=15)