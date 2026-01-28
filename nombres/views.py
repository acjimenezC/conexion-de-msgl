from django.shortcuts import render, redirect
from .models import Nombre
from .forms import NombreForm

def lista_nombres(request):
    """Lista todos los nombres"""
    nombres = Nombre.objects.all()
    return render(request, 'nombres/lista.html', {'nombres': nombres})

def crear_nombre(request):
    """Crear un nuevo nombre"""
    mensaje_error = None
    if request.method == 'POST':
        form = NombreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_nombres')
        else:
            # Capturar errores de validación para mostrar en plantilla
            if 'non_field_errors' in form.errors:
                mensaje_error = form.errors['non_field_errors'][0]
    else:
        form = NombreForm()
    return render(request, 'nombres/crear.html', {'form': form, 'mensaje_error': mensaje_error})

def eliminar_nombre(request, id):
    """Eliminar un nombre"""
    nombre = Nombre.objects.get(id=id)
    nombre.delete()
    return redirect('lista_nombres')
