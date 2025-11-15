import django.forms as forms
from django.utils import timezone
from .models import Evento,CustomUser
from django.contrib.auth.forms import UserCreationForm

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        labels = {
            'nombre': 'Nombre del Evento',
            'descripcion': 'Descripción del Evento',
            'tipo_evento': 'Tipo de Evento',
            'privado': '¿Es un Evento Privado?',
            'fecha': 'Fecha y Hora del Evento',
            'ubicacion': 'Ubicación del Evento',
        }
        fields = ['nombre', 'descripcion', 'tipo_evento', 'privado', 'fecha', 'ubicacion']
        widgets = {
            'fecha': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'privado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        if fecha < timezone.now():
            raise forms.ValidationError("La fecha del evento no puede ser en el pasado.")
        return fecha

class CustomUserCreationForm(UserCreationForm):
        class Meta:
            model = CustomUser
            fields = ('username', 'email', 'first_name', 'last_name')
    
