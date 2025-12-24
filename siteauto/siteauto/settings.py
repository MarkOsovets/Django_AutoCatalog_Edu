"""
Django settings (moved to project root)
"""

from pathlib import Path
import os
from os import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR should point to the project root (where manage.py is)
BASE_DIR = Path(__file__).resolve().parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

import os   

ALLOWED_HOSTS = ["127.0.0.1", "localhost", "0.0.0.0"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'auto.apps.AutoConfig',
    'users.apps.UsersConfig',
    'debug_toolbar',
    'social_django',
    'captcha'
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL configuration — after move we use the top-level `urls.py`
ROOT_URLCONF = 'siteauto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                BASE_DIR / 'templates',
                # Also keep compatibility with the previous layout where templates
                # were stored under siteauto/templates (siteauto/siteauto/templates)
                BASE_DIR / 'siteauto' / 'templates',
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'users.context_processors.get_auto_category'
            ],
        },
    },
]

# WSGI application path adjusted for root-level module
WSGI_APPLICATION = 'siteauto.wsgi.application'

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
#        "TIMEOUT": 300,
}
}

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': environ.get('DB_NAME'),
        'USER': environ.get('DB_USER'),
        'PASSWORD': environ.get('DB_PASSWORD'),
        'HOST': environ.get('DB_HOST'),
        'PORT': environ.get('DB_PORT'),
    }
}


# Password validation
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
LANGUAGE_CODE = 'ru-Ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_collected')
STATICFILES_DIRS = [
    BASE_DIR / 'siteauto' / 'static',
]

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'users.pipeline.new_user_handler',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

INTERNAL_IPS = [
    "127.0.0.1",
    "localhost",
]

LOGIN_URL = 'users:login'
LOGIN_REDIRECT_URL = '/' 

AUTHENTICATION_BACKENDS = [
    'social_core.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    'users.authentication.EmailAuthBackend',
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'markosovets@gmail.com'
EMAIL_HOST_PASSWORD = 'scbh jdkl ujil qxpn' 

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER

AUTH_USER_MODEL = 'users.User'

DEFAULT_USER_IMAGE = "users/default.png"

SOCIAL_AUTH_GITHUB_KEY = environ.get('SOCIAL_AUTH_GITHUB_KEY')
SOCIAL_AUTH_GITHUB_SECRET = environ.get('SOCIAL_AUTH_GITHUB_SECRET')
SERVER_EMAIL = EMAIL_HOST_USER

AUTH_USER_MODEL = 'users.User'

DEFAULT_USER_IMAGE = "users/default.png"


SOCIAL_AUTH_GITHUB_KEY = 'Ov23libiXh0mC3hjHQfd'
SOCIAL_AUTH_GITHUB_SECRET = '93bcadf4a866bbda11b7c1ff250569f5d9c1a73c'
SOCIAL_AUTH_GITHUB_SECRET = '93bcadf4a866bbda11b7c1ff250569f5d9c1a73c'
SOCIAL_AUTH_GITHUB_SECRET = '93bcadf4a866bbda11b7c1ff250569f5d9c1a73c'
