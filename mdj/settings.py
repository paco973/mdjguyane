"""
Django settings for mdj project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#import django_heroku

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-mz$@-2e25eb$ts#pwz2xpfaz2daq%qx4baoodo_zjku1c1r$(='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'djrichtextfield',
    'ckeditor',
    'django_summernote',
    'base',
    'blog',
    'don',
    'payment'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'mdj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'mdj.wsgi.application'

INTERNAL_IPS = [

    '127.0.0.1',

]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases



DATABASES = {




    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mdjguyane',
        'USER': 'paco@mdjguyane',
        'PASSWORD': 'PAPApadeo1',
        'HOST': 'mdjguyane.postgres.database.azure.com',
        'PORT': '5432',
    }
}


'''


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mdjguyane',
        'USER': 'paco',
        'PASSWORD': 'PAPApadeo1',
        'HOST': '/cloudsal/mdjguyane:us-central1:myinstance',
    }
}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
DATABASES = {




    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mdjguyane',
        'USER': 'paco',
        'PASSWORD': 'PAPApadeo1',
        'HOST': 'mdjguyane.postgres.database.azure.com',
        'PORT': '5432',
    }
}

'''
# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


STATIC_ROOT = [os.path.join(BASE_DIR, 'staticfiles')]
STATIC_URL = '/static/'
STATICFILES = [os.path.join(BASE_DIR, 'static')]
MEDIA_URL = '/media/'
Media_ROOT = os.path.join(BASE_DIR, 'static', 'media')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_FROM_EMAIL = 'mdjg.973@gmail.com'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'mdjg.973@gmail.com'
EMAIL_HOST_PASSWORD = 'Maison973j.'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#django_heroku.settings(locals())


# Constante de stripe
STRIPE_PUBLIC_KEY = "pk_test_51JvNteLu7wedQjFifldNigf9VDg6rVAPRFw0ir12Znwq4jT7xa0PKfxZ7Z0TNPwXCayhzLWeQbbpDCsuatn0ssUs00CwUVlagB"
STRIPE_SECRET_KEY = "sk_test_51JvNteLu7wedQjFimwBxANDjbV0k3mHnP3sUa6kA3uHzn6l3bpngbSdPDrlRCGPej25EVTMFurIo83t332zl00P800gJFqVTly"
STRIPE_WEBHOOK_SECRET = ""



