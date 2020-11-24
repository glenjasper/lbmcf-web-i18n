"""
Django settings for lbmcf project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import os
from decouple import config
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default = True, cast = bool)
HOSTS = config('ALLOWED_HOSTS', default = '')
ALLOWED_HOSTS = []
if HOSTS:
    for host in HOSTS.split(','):
        ALLOWED_HOSTS.append(host)

# Application definition

INSTALLED_APPS = [
    'apps.registration',
    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # other apps
    'ckeditor',
    'naomi',
    'auditlog',
    'parler',
    # my apps
    'apps.core',
    'apps.research',
    'apps.partnerships',
    'apps.publications',
    'apps.members',
    'apps.social',
    'apps.legal',
    'apps.contact',
    'apps.about',
    'apps.profiles',
    'apps.messenger',
    'apps.links',
    'apps.news',
    'apps.innovation',
    #'apps.research.apps.ResearchConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # Encargado de escoger el lenguaje adecuado (HTML text)
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'auditlog.middleware.AuditlogMiddleware',
]

ROOT_URLCONF = 'lbmcf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n', # Util para i18n (HTML text)
                'apps.social.processors.get_links',
                'apps.legal.processors.global_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'lbmcf.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE', default = ''),
        'NAME': config('DB_NAME', default = ''),
        'USER': config('DB_USER', default = ''),
        'PASSWORD': config('DB_PASSWORD', default = ''),
        'HOST': config('DB_HOST', default = ''),
    }
}

_db_port = config('DB_PORT', default = '')
if _db_port:
    DATABASES['default'].update({'PORT': _db_port})

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

default_language = 'pt'

# LANGUAGE_CODE = 'en-us'
# LANGUAGE_CODE = 'es'
# LANGUAGE_CODE = 'pt'
LANGUAGE_CODE = default_language

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# i18n (HTML text)
LANGUAGES = [
    ('pt', _('Portuguese')),
    ('en', _('English')),
    ('es', _('Spanish'))
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

# Parler
PARLER_DEFAULT_LANGUAGE_CODE = default_language
PARLER_SHOW_EXCLUDED_LANGUAGE_TABS = True

PARLER_LANGUAGES = {
    None: (
        {'code': 'pt',},
        {'code': 'en',},
        {'code': 'es',},
    ),
    'default': {
        'fallbacks': [default_language], # defaults to PARLER_DEFAULT_LANGUAGE_CODE
        'hide_untranslated': False,      # the default; let .active_translations() return fallbacks too.
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Media config
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# CkEditor
# https://github.com/django-ckeditor/django-ckeditor
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            #['RemoveFormat', 'Source']
        ]
    }
}

# Auth redirects
# LOGIN_REDIRECT_URL = 'core_app:url_home' # Auto redirect Home
LOGOUT_REDIRECT_URL = 'core_app:url_home'

# Email config
if DEBUG:
    # EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_BACKEND = "naomi.mail.backends.naomi.NaomiBackend"
    EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'send_emails')

EMAIL_HOST = config('EMAIL_HOST', default = 'localhost')
EMAIL_PORT = config('EMAIL_PORT', default = 587, cast = int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default = '')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default = '')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default = False, cast = bool)

# GROUPS DB
GROUP_REGULAR = "regular"