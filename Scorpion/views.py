from django.shortcuts import render, redirect
from .forms import ClienteForm
from .models import Cliente

# Create your views here.

from django.shortcuts import render, redirect
from .forms import ClienteForm, CitaForm
from .models import Cliente, Cita

def crear_cliente(request):
    cliente_existente = False

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            rut_limpio = form.cleaned_data['rut']
            cliente_existente = Cliente.objects.filter(rut=rut_limpio).exists()
            if cliente_existente:
                form.add_error('rut', '')
            else:
                form.save()
                return redirect('crear_cita')
    else:
        form = ClienteForm()

    context = {
        'form': form,
        'cliente_existente': cliente_existente
    }
    
    return render(request, 'cliente_form.html', context)


def crear_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            cita = form.save()

            # Obtener los datos de la cita recién creada
            cliente = cita.cliente
            hora = cita.hora
            fecha = cita.fecha
            servicios = cita.servicio.all()

            # Pasar los datos a la plantilla de confirmación
            context = {
                'cliente': cliente,
                'hora': hora,
                'fecha': fecha,
                'servicios': servicios,
            }

            return render(request, 'confirmacion.html', context)
    else:
        form = CitaForm()
    
    return render(request, 'cita_form.html', {'form': form})


def index(request):
    return render(request,'index.html')

def servicios(request):
    return render(request, 'servicios.html')

def confirmacion(request):
    return render(request,'confirmacion.html')

def citas(request):
    citas = Cita.objects.all()
    return render(request, 'citas.html', {'citas': citas})
