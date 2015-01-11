"""
Django settings for Monocular project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import LOGOUT_URL, EMAIL_USE_TLS, EMAIL_HOST,\
    EMAIL_HOST_PASSWORD
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c67l8eh=a6a&rv1^5u5%^+o5@g7*1+r1m_y_f%pzcui6k!95n7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Redirect when login is correct.
LOGIN_REDIRECT_URL = "/administracion/"
# Redirect when login is not correct.
LOGIN_URL = '/administracion'
LOGOUT_URL = '/administracion/logout'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.inicio',
    'apps.autores',
    'apps.noticias',
    'apps.servicios',
    'apps.administracion',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'Monocular.urls'

WSGI_APPLICATION = 'Monocular.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'monocular',
        'USER': 'root',
        'PASSWORD': '',
        'PORT': '',
        'HOST': '',
    }
}

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER ='carlosgn2s@gmail.com'
EMAIL_HOST_PASSWORD='CAR36SY*53AR'
EMAIL_PORT = 587
# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# settings.py
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
#MEDIA_ROOT = os.path.join(PATH, 'static/media/')
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

#STATICFILES_DIRS = (join(PATH, "static"),)
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
#STATIC_ROOT= 'C:/workspace/luna/monocular/static/'
#STATIC_ROOT= 'C:/workspace/lunajee/mono//mono/static/'

STATIC_URL = '/static/'
# Aadir para poder ver los archivos estticos

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,'templates'),
)

