from .settings import *

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pruebas_django',
        'USER': 'root', 
        'PASSWORD': 'facil123',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}