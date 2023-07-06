from django.urls import path
from . import views

urlpatterns = [
    # Otras URLS de tu aplicación
    path('crear_cliente/', views.crear_cliente, name='crear_cliente'),
    path('crear_cita/', views.crear_cita, name='crear_cita'),
    path('', views.index, name="index"),
    path('servicios/', views.servicios, name="servicios"),
    path('confirmacion/', views.confirmacion, name="confirmacion"),
    path('citas/', views.citas, name='citas'),
]
