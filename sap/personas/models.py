from django.db import models

# Create your models here.

class Domicilio(models.Model):
    calle = models.CharField(max_length=255)
    no_calle = models.IntegerField()
    ciudad = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)

    def __str__(self):
        return f'Domicilio {self.calle} {self.no_calle} {self.ciudad} {self.pais}'

class Personas(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Persona {self.id}: {self.nombre} {self.apellido} {self.email}'


