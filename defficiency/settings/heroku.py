from defficiency.settings.base import *
import environ

env = environ.Env()

# Debug
DEBUG = env.bool('DEBUG', False)

# Secret Key
SECRET_KEY = env('SECRET_KEY')

# Allowed Hosts
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('MYSQL_DB_NAME'),
        'HOST': env('MYSQL_HOST'),
        'USER': env('MYSQL_USER'),
        'PASSWORD': env('MYSQL_PASSWORD'),
        'PORT': env('MYSQL_PORT'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}
