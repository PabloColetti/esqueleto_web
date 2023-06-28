### Install MySQL Server
```
https://dev.mysql.com/downloads/installer/
``` 

### requeriments.txt
```
asgiref==3.7.2
Django==4.2.2
mysql-connector-python==8.0.33
mysqlclient==2.2.0
sqlparse==0.4.4
tzdata==2023.3
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
(2) - Para ejecutar comandos del entorno(crearlo, activarlo o desactivarlo)
- python -m venv nombre_entorno
- nombre_entorno\Scripts\activate
- nombre_entorno\Scripts\deactivate
- Si no les reconoce el comando >>> cd nombre_entorno >>> cd Scripts >>> activate
- python -m pip install --upgrade pip
- django-admin startproject nombre_proyecto
- pip install nombre_paquete
- etc

(2) - Para ejecutar comandos del manage.py
- pyhton manage.py runserver
- pyhton manage.py startapp nombre_aplicacion
- pyhton manage.py makemigrations
- pyhton manage.py migrate
- pyhton manage.py createsuperuser
- pip install nombre_del_paquete
- etc
```