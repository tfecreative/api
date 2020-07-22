from .services.crypt import Crypt
import os
import sys
from distutils.util import strtobool
from decouple import config
settings_module = sys.modules[__name__]


### Django
DEBUG = config('DEBUG', default=True, cast=bool)
TAG = config('TAG', default='')
ENVIRONMENT_NAME = config('ENVIRONMENT_NAME', default='')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = config('SECRET_KEY')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [
                       s.strip() for s in v.split(',')])

EMAIL_USE_TLS = True
EMAIL_HOST = config('EMAIL_HOST', default='')
EMAIL_PORT = config('EMAIL_PORT', default='')
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

WSGI_APPLICATION = 'tfecreative.wsgi.application'
SITE_ID = 2
ROOT_URLCONF = 'tfecreative.urls'

INSTALLED_APPS = [
    'admin_interface',
    'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework.authtoken',
    'django_extensions',
    'tfecreative.api',
    'tfecreative.core',
    'admin_reorder',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'admin_reorder.middleware.ModelAdminReorder',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['tfecreative/templates', 'tfecreative/templates/email'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


### Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_ENV_DB', default='postgres'),
        'USER': config('DB_ENV_POSTGRES_USER', default='postgres'),
        'PASSWORD': config('DB_ENV_POSTGRES_PASSWORD', default='postgres'),
        'HOST': config('DB_PORT_5432_TCP_ADDR', default='db'),
        'PORT': config('DB_PORT_5432_TCP_PORT', default='5432'),
    },
}


### Django Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'EXCEPTION_HANDLER': 'tfecreative.core.exceptions.base_exception_handler',
    'PAGE_SIZE': 100,
}


### Authentication
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


### Admin Panel
ADMIN_REORDER = (
    {
        'app': 'core',
        'label': 'Auth',
        'models': (
            'auth.Group',
            'authtoken.Token',
            'sites.Site',
        )
    },
    {
        'app': 'core',
        'label': 'Users',
        'models': (
            'core.TfeUser',
            'core.UserProfile',
        )
    },
)


### Email
NO_REPLY_EMAIL = config('NO_REPLY_EMAIL', default='noreply@tfecreative.com')


### AWS
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID', '')
AWS_DEFAULT_ACL = None
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY', '')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME', '')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

if not DEBUG:
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


### Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


### Security
CORS_ORIGIN_ALLOW_ALL = True


### ACCOUNTS
ADMIN_EMAIL = config('ADMIN_EMAIL', default='')
ADMIN_USERNAME = config('ADMIN_USERNAME', default='')
ADMIN_PASSWORD = config('ADMIN_PASSWORD', default='')

TEST_USER_FIRST_NAME = config('TEST_USER_FIRST_NAME', default='')
TEST_USER_LAST_NAME = config('TEST_USER_LAST_NAME', default='')
TEST_USER_EMAIL = config('TEST_USER_EMAIL', default='')
TEST_USER_PASSWORD = config('TEST_USER_PASSWORD', default='')
TEST_USER_USERNAME = config('TEST_USER_USERNAME', default='')

AUTH_USER_MODEL = 'core.TfeUser'


### RECAPTCHA
RECAPTCHA_VERIFICATION_URL = config(
    'RECAPTCHA_VERIFICATION_URL',
    default='https://www.google.com/recaptcha/api/siteverify'
)
RECAPTCHA_SECRET_KEY = config('RECAPTCHA_SECRET_KEY', default='')
RECAPTCHA_ENABLED = config('RECAPTCHA_ENABLED', default=True, cast=bool)


### VAULT
CRYPT_VAULT_ENV_PATH = config('CRYPT_VAULT_ENV_PATH', '')
CRYPT_VAULT_TOKEN = config('CRYPT_VAULT_TOKEN', '')
CRYPT_VAULT_URL = config('CRYPT_VAULT_URL', '')
