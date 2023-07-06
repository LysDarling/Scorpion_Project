from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name_plural = "Clientes"

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion = models.PositiveIntegerField(verbose_name="Minutos")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Servicios"

class Cita(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicio = models.ManyToManyField(Servicio)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f'Cita {self.id} - {self.cliente.nombre} {self.cliente.apellido}'

    class Meta:
        verbose_name_plural = "Citas"
