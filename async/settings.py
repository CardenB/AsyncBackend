"""
Django settings for async project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5qkz*x!ii1hayo0lbav+!0*o9-_w3dc+$p0%tx5rh6t8ahg79i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'hacker',
    'oauth2_provider',
    'social.apps.django_app.default',
    'rest_framework_social_oauth2',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'async.urls'

WSGI_APPLICATION = 'async.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Carden',  # os.path.join(BASE_DIR, 'mydb'),
        'USER': 'Carden',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            # For those who wants to have a custom place for templates in their
            # Django apps/projects.
            'DIRS': [os.path.join(BASE_DIR, '<enter here your custom templates directory')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    # OAuth
                    'social.apps.django_app.context_processors.backends',
                    'social.apps.django_app.context_processors.login_redirect',
                ],
                },
            },
]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # OAuth
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
        'rest_framework_social_oauth2.authentication.SocialAuthentication',
    ),
}

AUTHENTICATION_BACKENDS = (

    # Facebook OAuth2
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',

   # django-rest-framework-social-oauth2
   'rest_framework_social_oauth2.backends.DjangoOAuth2',

   # Django
   'django.contrib.auth.backends.ModelBackend',
)


# Facebook configuration
SOCIAL_AUTH_FACEBOOK_KEY = '691381307663542'
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('FACEBOOK_KEY')
