from django.db import models

class Familiares(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    cumpleanios = models.DateField()
    parentezco = models.CharField(max_length=40)
    
