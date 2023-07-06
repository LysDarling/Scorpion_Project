from django import forms
from django.shortcuts import render
from Scorpion.models import Cliente, Cita
from datetime import datetime, timedelta, time



class ClienteForm(forms.ModelForm):
    rut = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Ej: 21078145-K', 'maxlength': '12', 'oninput': 'formatRut(this)'}),
        max_length=12,
        min_length=9,
    )

    def clean_rut(self):
        rut = self.cleaned_data['rut']
        rut_limpio = rut.replace(".", "").replace("-", "").upper()
        cliente_existente = Cliente.objects.filter(rut=rut_limpio).exists()
        if cliente_existente:
            self.cliente_existente = True
        return rut_limpio

    class Meta:
        model = Cliente
        fields = ['rut', 'nombre', 'apellido', 'telefono', 'email']



class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['cliente', 'servicio', 'fecha', 'hora']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'min': datetime.now().strftime('%Y-%m-%d'), 'max': (datetime.now() + timedelta(weeks=4)).strftime('%Y-%m-%d')}),
            'hora': forms.TimeInput(attrs={'type': 'time', 'min': time(8, 0).strftime('%H:%M'), 'max': time(17, 30).strftime('%H:%M')}),
            'servicio': forms.SelectMultiple(attrs={'size': 5, 'class': 'custom-service'}),

        }

    def clean_hora(self):
        hora = self.cleaned_data['hora']

        if hora < time(8, 0) or hora > time(17, 30):
            raise forms.ValidationError("El horario de Scorpion es de 08:00 a 17:30")

        fecha = self.cleaned_data['fecha']

        # Filtrar citas existentes para la misma fecha y hora seleccionada
        citas_existentes = Cita.objects.filter(fecha=fecha, hora=hora)

        if citas_existentes.exists():
            raise forms.ValidationError("La hora seleccionada no está disponible. Por favor, elija otra hora.")

        return hora