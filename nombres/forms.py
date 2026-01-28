from django import forms
from django.core.exceptions import ValidationError
from .models import Nombre

class NombreForm(forms.ModelForm):
    class Meta:
        model = Nombre
        fields = ['nombre', 'apellido']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Hacer obligatorios ambos campos
        self.fields['nombre'].required = True
        self.fields['apellido'].required = True
        self.fields['nombre'].error_messages = {'required': 'El nombre es obligatorio.'}
        self.fields['apellido'].error_messages = {'required': 'El apellido es obligatorio.'}
    
    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre', '').strip()
        apellido = cleaned_data.get('apellido', '').strip()
        
        # Validar que no estén vacíos después de limpiar espacios
        if not nombre:
            self.add_error('nombre', 'El nombre no puede estar vacío.')
        if not apellido:
            self.add_error('apellido', 'El apellido no puede estar vacío.')
        
        if nombre and apellido:
            # Verificar si ya existe un registro con el mismo nombre y apellido
            existe = Nombre.objects.filter(
                nombre__iexact=nombre,
                apellido__iexact=apellido
            ).exists()
            
            if existe:
                raise ValidationError(
                    '⚠️ Este nombre y apellido ya está registrado en el sistema.'
                )
        
        return cleaned_data
