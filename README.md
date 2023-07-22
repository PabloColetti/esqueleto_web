### Install MySQL Server
```
https://dev.mysql.com/downloads/installer/
``` 

### Install modules from requeriments.txt
```
pip install -r requeriments.txt
```

### Migrate dependencies
```
python manage.py migrate
``` 

### Run Django server
```
python manage.py runserver
``` 

### Example - Project structure 
```
content-project/        (1) <--- Carpeta contenedora del proyecto
├── esqueleto_web/      (2) <--- Carpeta Repositorio
│ ├── env/              (3) <--- Carpeta del entorno - Ignorada en el .gitignore
│ ├── myproject/        (4) <--- Carpeta del proyecto
│ │ ├── myproject/
│ │ │ ├── __pycache__/
│ │ │ ├── __init__.py
│ │ │ ├── asgi.py
│ │ │ ├── settings.py
│ │ │ ├── urls.py
│ │ │ ├── wsgi.py
│ │ │ └── ...
│ │ ├── myapp/          (5) <--- Carpeta de la aplicacion
│ │ │ ├── __pycache__/
│ │ │ ├── migrations/
│ │ │ ├── __init__.py
│ │ │ ├── admin.py
│ │ │ ├── apps.py
│ │ │ ├── models.py
│ │ │ ├── tests.py
│ │ │ ├── urls.py
│ │ │ ├── views.py
│ │ │ └── ...
│ │ ├── manage.py       (6) <--- Archivo manage.py
│ │ └── ...
│ ├── .gitignore
│ ├── README.md
│ ├── requeriments.txt  (7) <--- Archivo requeriments.txt - Ver si lo quieren ignorar en el .gitignore
| └── ...
└── ...
```

### Used commands
```
(1) En carpeta contenedora del proyecto
Para ejecutar comandos de git(clonar)
- git clone url_del_repo

- git remote add origin url_repo

(2) En la carpeta del epositorio
Para ejecutar comandos del entorno(crearlo, activarlo o desactivarlo)
- python -m venv nombre_entorno
- nombre_entorno\Scripts\activate
- nombre_entorno\Scripts\deactivate
- Si no les reconoce el comando >>> cd nombre_entorno >>> cd Scripts >>> activate o deactivate
- python -m pip install --upgrade pip

- django-admin startproject nombre_proyecto

- pip install nombre_paquete
- pip freeze
- pip freeze > requeriments.txt

Creaando un archivo requirementes.txt y definiendo el paquete y sus version
- pip install -r requeriments.txt

- git status
- git add .
- git add archivo_especifico
- git commit -m "mensaje_del_commit"
- git push
- git fetch
- git pull
- etc

(4) En la carpeta del proyecto
Para ejecutar comandos del manage.py
- python manage.py runserver
- python manage.py startapp nombre_aplicacion
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser

- pip install nombre_del_paquete
- etc
```

julian hace unos cambios en el readme por ejemplo

AGREGO UN CAMBIO DE PRUEBA