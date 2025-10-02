## Paso a paso para crear una aplicación web en Django

## 1. Prepara tu entorno de desarrollo

Crear y activar un entorno virtual

En Windows:

```sh
python -m venv venv
venv\Scripts\activate
```

## 2. Crea el proyecto y la app en Django

Instala Django si no lo tienes instalado:

```sh
pip install django
```

Luego, crea un nuevo proyecto y una app dentro de él:

```sh

django-admin startproject registro_eventos ## Crear el proyecto
cd registro_eventos
python manage.py startapp eventos ## Crear la app de eventos
```

## 2. Configura la app en settings.py de registro_eventos

Abre `registro_eventos/settings.py` y añade `'eventos'` a la lista de `INSTALLED_APPS`:



## 3. Luego cree el model en models.py de eventos

    de acuerdo a los requerimientos

## 4. Crea los formularios en forms.py de eventos

    de acuerdo a
    [AE4_Formularios en Django](https://learning-pro.skillnest.com/mod/page/view.php?id=2746)

## 5. Crea las vistas en views.py de eventos

 yluego crea las vistas necesarias para manejar los formularios y la lógica de la aplicación.
    de acuerdo a
    [AE4_Vistas y Templates en Django](https://learning-pro.skillnest.com/mod/page/view.php?id=2747)

    
## 6. creacion de archivos Base.html formulario_base.html, registro_participante.html, registro_exito.html e index.html

Crea los archivos HTML en la carpeta `templates` de la app `eventos` con el siguiente contenido:
- formulario_base.html
- registro_evento.html
- registro_participante.html
- registro_exito.html
- base.html
- index.html

## 7. Configura las URLs en urls.py de eventos

Crea un archivo `urls.py` en la carpeta de la app `eventos` y configura las URLs para las vistas que has creado.

Luego, incluye las URLs de la app `eventos` en el archivo `urls.py` del proyecto principal `registro_eventos`.

## 8. Migra la base de datos
Aplica las migraciones para crear las tablas en la base de datos:

```sh
python manage.py makemigrations
python manage.py migrate
```
## 9. Ejecuta el servidor de desarrollo

```sh
python manage.py runserver
```

## 10. Para hacer dinámico el index.html

mejorar la vista en views.py de index y agregar los valores
    eventos = Evento.objects.all()
    participantes = Participante.objects.all()

    y en el render se pasan los valores
    return render(request, 'index.html', {'eventos': eventos, 'participantes': participantes})

