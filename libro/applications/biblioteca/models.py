from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField('nombres', max_length=80)
    nacionalidad = models.CharField(blank=true, max_length=100)

    def __str__(self):
        return self.nombre
    