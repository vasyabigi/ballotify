from os.path import join, normpath

from .common import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': normpath(join(BASE_DIR, 'dev.db')),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'nx7=njxnb4%qolk33mty^0(c7s2l+yxj%b5b^g&^o9_+7&5^na'

ADMINS = (
    # ('', ''),
)

# Show emails in the console during developement.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS += (
    'debug_toolbar.apps.DebugToolbarConfig',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': join(BASE_DIR, 'logs', 'ballotify.log'),
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 50,
            'formatter': 'standard',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True
        }
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


SOCIAL_AUTH_FACEBOOK_KEY = '107790869310294'
SOCIAL_AUTH_FACEBOOK_SECRET = '3b53c9038e5b696f8d934be18b33a6f5'
