# Blog creado por el equipo 7 de la comisión 3 del informatorio del chaco 2da edición 2021

Para su despliegue de prueba local debe seguir los siguientes pasos
-	Abrir su instancia local de mysql y crear el esquema blogdb y seleccionarlo. 
-	Crear el entorno virtual donde se utilizará la prueba
-	Clonar este repositorio en su entorno local
-	Instalar las dependencias proporcionadas por el archivo requirements.txt
-	Dirigirse a la ubicación blog-django-dev/blog/blog/settings/local.py con tu editor de texto y modificar las variables de la base de datos mysql según su configuración personal
-	Dirigirse a la ubicación blog-django-dev/blog y ejecutar los siguientes comandos en la consola
o	python manage.py makemigrations
o	python manage.py migrate
o	python manage.py runserver
