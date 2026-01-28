from django.urls import path
from .views import lista_nombres, crear_nombre, eliminar_nombre

urlpatterns = [
    path('', lista_nombres, name='lista_nombres'),
    path('crear/', crear_nombre, name='crear_nombre'),
    path('eliminar/<int:id>/', eliminar_nombre, name='eliminar_nombre'),
]
