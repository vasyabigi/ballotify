from .common import *

from os.path import join, normpath

DEBUG = False

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
