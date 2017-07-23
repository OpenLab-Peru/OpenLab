from .common import *  # noqa


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

THIRD_PARTY_APPS_LOCAL = (
    'debug_toolbar',
    'django_extensions',
)

INSTALLED_APPS += THIRD_PARTY_APPS_LOCAL  # noqa

MIDDLEWARE += (  # noqa
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME'),  # noqa
        'USER': os.environ.get('DB_USER'),  # noqa
        'PASSWORD': os.environ.get('DB_PASSWORD'),  # noqa
        'HOST': os.environ.get('DB_HOST'),  # noqa
        'PORT': os.environ.get('DB_PORT'),  # noqa
        'ATOMIC_TRANSACTIONS': True
    }
}
