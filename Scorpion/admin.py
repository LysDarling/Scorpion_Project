from django.contrib import admin
from .models import Cita
from django.contrib import admin
from .models import Cliente, Servicio, Cita

# Register your models here.

# MODELO CLIENTE
admin.site.register(Cliente)
# MODELO SERVICIO
admin.site.register(Servicio)
# MODELO CITA
admin.site.register(Cita)
