from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dbintranet',
        'USER': 'postgres',
        'PASSWORD': 'sistemas',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}