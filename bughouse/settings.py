"""
Django settings for bughouse-rankings project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
import excavator
from dj_database_url import config as dj_config


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = excavator.env_string('DJANGO_SECRET_KEY', required=True)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = excavator.env_bool('DJANGO_DEBUG', required=True)

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # local
    'bughouse',
    # 3rd party
    'pipeline',
    'argonauts',
    'rest_framework',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'bughouse.urls'

WSGI_APPLICATION = 'bughouse.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': dj_config(),
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = excavator.env_string(
    'DJANGO_STATIC_URL', default='/static/', required=False,
)
STATIC_ROOT = os.path.abspath(
    excavator.env_string('DJANGO_STATIC_ROOT', required=True),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)


DEFAULT_FILE_STORAGE = excavator.env_string('DEFAULT_FILE_STORAGE')


# Amazon S3 storage
AWS_ACCESS_KEY_ID = excavator.env_string('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = excavator.env_string('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = excavator.env_string('AWS_STORAGE_BUCKET_NAME')
AWS_BUCKET_NAME = AWS_STORAGE_BUCKET_NAME

DEFAULT_S3_PATH = "media"
STATIC_S3_PATH = "static"
STATICFILES_STORAGE = excavator.env_string('STATICFILES_STORAGE')


# Pipeline
PIPELINE_ENABLED = excavator.env_bool('DJANGO_PIPELINE_ENABLED', default=not DEBUG)

PIPELINE_DISABLE_WRAPPER = True

PIPELINE_CSS = {
    'base': {
        'source_filenames': (
            "css/bootstrap.css",
            "css/bootstrap-theme.css",
        ),
        'output_filename': 'base.css',
    },
}

PIPELINE_JS = {
    'base': {
        'source_filenames': (
            "js/jquery.js",
            "js/bootstrap.js",
            "js/handlebars.js",
            "js/underscore.js",
            "js/backbone.js",
            "js/backbone.wreqr.js",
            "js/backbone.babysitter.js",
            "js/backbone.marionette.js",
            "js/backbone.marionette.export.js",
            "js/report-game/config.js",
            "js/report-game/models.js",
            "js/report-game/collections.js",
            "js/report-game/views.js",
            "js/report-game/layouts.js",
            "js/report-game/app.js",
        ),
        'output_filename': 'base.js',
    },
}
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'

PIPELINE_TEMPLATE_EXT = '.handlebars'
PIPELINE_TEMPLATE_FUNC = 'Handlebars.compile'
PIPELINE_TEMPLATE_NAMESPACE = 'Handlebars.templates'
