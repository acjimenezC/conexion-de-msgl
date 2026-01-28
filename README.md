# Gestión de Nombres

Aplicación Django para registrar y gestionar nombres y apellidos con validación de duplicados.

## Características

- ✅ Crear nombres y apellidos
- ✅ Listar todos los registros
- ✅ Eliminar registros con confirmación
- ✅ Validación: campos obligatorios
- ✅ Validación: no permite duplicados
- ✅ Conexión a MySQL implementada

## Requisitos

- Python 3.8+
- Django 4.2.8
- MySQL
- mysqlclient 2.2.0

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/TU_USUARIO/conexion-de-msgl.git
cd conexion-de-msgl

# Crear entorno virtual
python -m venv venv
venv\Scripts\activate

# Instalar dependencias
pip install -r [requirements.txt](http://_vscodecontentref_/0)

# Configurar base de datos en .env
# DB_ENGINE=django.db.backends.mysql
# DB_NAME=base
# DB_USER=root
# DB_PASSWORD=tu_contraseña
# DB_HOST=localhost
# DB_PORT=3306

# Migraciones
python [manage.py](http://_vscodecontentref_/1) migrate

# Ejecutar servidor
python [manage.py](http://_vscodecontentref_/2) runserver
