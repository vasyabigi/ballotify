import sys
import datetime
from os.path import dirname, join

BASE_DIR = dirname(dirname(__file__))
sys.path.insert(0, join(BASE_DIR, 'apps'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

TIME_ZONE = 'UTC'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = join(BASE_DIR, 'public/media')
MEDIA_URL = '/media/'

STATIC_ROOT = join(BASE_DIR, 'public/static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

ROOT_URLCONF = 'ballotify.urls'

WSGI_APPLICATION = 'ballotify.wsgi.application'

TEMPLATE_DIRS = (
    join(BASE_DIR, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Plugins:
    'django_extensions',
    'rest_framework',
    'rest_framework_swagger',
    'django_filters',
    'social.apps.django_app.default',
    'corsheaders',

    # Apps:
    'core',
    'accounts',
    'streams',
    'questions',
    'votes'
)

REST_FRAMEWORK = {
    'PAGINATE_BY': 20,
    'MAX_PAGINATE_BY': 100,

    'DEFAULT_MODEL_SERIALIZER_CLASS': 'rest_framework.serializers.HyperlinkedModelSerializer',

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),

    'DEFAULT_RENDERER_CLASSES': (
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),

    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
    ),

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),

    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),

    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_USER_MODEL = 'accounts.User'
SOCIAL_AUTH_USER_MODEL = 'accounts.User'

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    # 'social.pipeline.user.get_username',
    'accounts.pipeline.create_user',
    'social.pipeline.social_auth.associate_user',
    'accounts.pipeline.create_default_stream',
    # 'social.pipeline.user.user_details',
)

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=2)
}
