# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.conf import settings

# Create your models here.
class Burritos(models.Model):
    #Relacionar al usuario
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    tamano = models.CharField(max_length = 100)
    descripcion = models.CharField(max_length = 100)
    ingredientes = models.CharField(max_length = 100)
    precio = models.DecimalField(max_digits = 10, decimal_places = 2)
    creado = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.tamano)
