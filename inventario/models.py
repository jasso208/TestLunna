from django.db import models
from django.db.models.fields import DecimalField
from rest_framework.serializers import ModelSerializer
from datetime import datetime
from django.utils import timezone

class Productos(models.Model):
    sku = models.IntegerField(unique = True,primary_key = True)
    name = models.CharField(max_length = 100,null = False)
    price = models.DecimalField(decimal_places=2,max_digits = 26)
    brand = models.CharField(max_length = 40)


class BitacoraConsultaUsuarioAnonimo(models.Model):
    producto = models.ForeignKey(Productos,on_delete=models.PROTECT)
    fecha = models.DateTimeField(default = timezone.now)



