"""
Django settings for Netflix_backend_conf project.

Generated by 'django-admin startproject' using Django 4.2.
For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from pathlib import Path
import os
import datetime
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2yp%pyzea!llakkvzhwx85njb#-72ka(gc2g*sap70mp!!rjjm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [

]


# Application definition

INSTALLED_APPS = [
    'material',
    'material.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'djoser',
    'rest_framework_simplejwt',
    'account',
    'Favorite_List',
    'comment',
    'Watch_List',
    'report',
    'corsheaders'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
] 

ROOT_URLCONF = 'Netflix_backend_conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'build')],
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

WSGI_APPLICATION = 'Netflix_backend_conf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Netflix_backend_1',
        'USER': 'postgres',
        'PASSWORD': 'bdu1203346',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'build/static')
]
STATIC_ROOT = os.path.join(BASE_DIR,'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
'''
all custome configration below
'''
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '192.168.43.26',
]
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://localhost:19006',
    'http://192.168.43.26',
    'exp://192.168.43.26:8081',
    
]
CORS_ORIGIN_ALLOW_ALL = True

AUTH_USER_MODEL = 'account.useracount'
'''used for use custome model for authentication'''

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'yihelgn@gmail.com'
EMAIL_HOST_PASSWORD = 'zkebxpgxidmububt'
'''this is another password->pxoyueakineecsad'''
EMAIL_USE_TLS = True

DJOSER = {
    'LOGIN_FIELD':'email',
    'USER_CREATE_PASSWORD_RETYPE':True,
    'USERNAME_CHANGED_EMAIL_CONFIRMATION':True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION':True,
    'SEND_CONFIRMATION_EMAIL':True,
    'SET_USERNAME_RETYPE':True,
    'SET_PASSWORD_RETYPE':True,
    'PASSWORD_RESET_CONFIRM_URL':'password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL':'email/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL':'activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL':True,
    'SERIALIZERS':{
        'user_create':'account.serializers.UserCreateSerializer',
        'user':'account.serializers.UserCreateSerializer',
        'user_delete':'djoser.serializers.UserDeleteSerializer'
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASS':{
        'rest_framework.permission.IsAuthenticated',
    },
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
}
SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ('JWT',),
}
AUTHENTICATION_BACKENDS = [
    'account.backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
]

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": datetime.timedelta(days=1),
    "AUTH_HEADER_TYPES": ("Bearer",),
    }