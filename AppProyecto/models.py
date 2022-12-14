from django.db import models

class Familiar(models.Model):
    nombre=models.CharField(max_length=40)
    fecha_nacimiento=models.DateField()
    edad=models.IntegerField()
    parentesco=models.CharField(max_length=15)

class Curso(models.Model):
    nombre=models.CharField(max_length=50)
    comision=models.IntegerField()

    def __str__(self):
        return self.nombre+" "+str(self.comision)


class Estudiante(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()

    def __str__(self):
        return self.nombre+" "+self.apellido
        

class Profesor(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    profesion= models.CharField(max_length=50)

class Entregable(models.Model):
    nombre= models.CharField(max_length=50)
    fecha_entrega= models.DateField()
    entregado= models.BooleanField()


