from django.db import models

# Create your models here.

class cliente(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    identificacion = models.IntegerField()

class cuenta(models.Model):
    tipo_cuenta = models.CharField(max_length=45)
    num_cuenta = models.CharField(max_length=45)
    monto = models.IntegerField()
    Cliente = models.ForeignKey(cliente,on_delete= models.PROTECT)



