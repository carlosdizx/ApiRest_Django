from django.db import models


class Persona(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
