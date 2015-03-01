import os
from django.core.exceptions import ImproperlyConfigured

from .common import *


DEBUG = True


def get_env_variable(var_name):
    """
    Get the environment variable or return exception.

    """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s env variable" % var_name
        raise ImproperlyConfigured(error_msg)

DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql_psycopg2",
        'NAME': get_env_variable("DB_ENV_DATABASE_NAME"),
        'USER': get_env_variable("DB_ENV_POSTGRES_USER"),
        'PASSWORD': get_env_variable("DB_ENV_POSTGRES_PASSWORD"),
        'HOST': get_env_variable("DB_PORT_5432_TCP_ADDR"),
        'PORT': get_env_variable("DB_PORT_5432_TCP_PORT"),
    }
}

SECRET_KEY = get_env_variable("SECRET_KEY")

ADMINS = (
    # ('', ''),
)

ALLOWED_HOSTS = []
