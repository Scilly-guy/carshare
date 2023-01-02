"""
Django settings for carshare project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
import stripe

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "nothing")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get("DEBUG", True))


def env_get_list(variable, default):
    var = os.environ.get(variable, None)
    if var is None:
        return default
    return var.split(",")


ALLOWED_HOSTS = env_get_list("ALLOWED_HOSTS", ["localhost", "127.0.0.1"])
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Application definition

INSTALLED_APPS = [
    "backoffice.apps.BackofficeConfig",
    "billing.apps.BillingConfig",
    "bookings.apps.BookingsConfig",
    "drivers.apps.DriversConfig",
    "hardware.apps.HardwareConfig",
    "public.apps.PublicConfig",
    "securemedia.apps.SecuremediaConfig",
    "users.apps.UsersConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.postgres",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "tailwind",
    "crispy_forms",
    "crispy_tailwind",
    "theme",
    "django_celery_results",
    "django_celery_beat",
    "polymorphic",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "carshare.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "carshare.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", "postgres"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "mysecretpassword"),
        "USER": os.environ.get("POSTGRES_USER", "postgres"),
        "PORT": int(os.environ.get("POSTGRES_PORT", 5433)),
        "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
    },
}

# Custom user model
AUTH_USER_MODEL = "users.User"

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
]

# AllAuth stuff
ACCOUNT_ADAPTER = "users.adapter.AccountAdapter"
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_SUBJECT_PREFIX = ""
LOGIN_REDIRECT_URL = "/bookings"
LOGIN_URL = "/users/login"
LOGOUT_REDIRECT_URL = "/"

# ACCOUNT_FORMS = {
#    'login': 'allauth.account.forms.LoginForm',
#    'signup': 'users.forms.PersonalSignupForm',
#    'add_email': 'allauth.account.forms.AddEmailForm',
#    'change_password': 'allauth.account.forms.ChangePasswordForm',
#    'set_password': 'allauth.account.forms.SetPasswordForm',
#    'reset_password': 'allauth.account.forms.ResetPasswordForm',
#    'reset_password_from_key': 'allauth.account.forms.ResetPasswordKeyForm',
#    'disconnect': 'allauth.socialaccount.forms.DisconnectForm',
# }

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-gb"

TIME_ZONE = "Europe/London"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

TAILWIND_APP_NAME = "theme"

INTERNAL_IPS = [
    "127.0.0.1",
]

SITE_ID = 1

CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"

# Emails
EMAIL_HOST = os.environ.get("EMAIL_HOST", "localhost")
EMAIL_PORT = int(os.environ.get("EMAIL_PORT", 2500))
EMAIL_USE_TLS = bool(os.environ.get("EMAIL_USE_TLS", False))
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", "carshare@localhost")

MEDIA_ROOT = os.environ.get("MEDIA_ROOT", "media/")
MEDIA_URL = "media/"
MEDIA_PROTECTED_URL = "media_protected/"
PROTECT_MEDIA = bool(os.environ.get("PROTECT_MEDIA", False))

# SMS Gateway
SMS_API_KEY = os.environ.get("SMS_API_KEY", None)

# Stripe
STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY", None)
STRIPE_PUBLIC_KEY = os.environ.get("STRIPE_PUBLIC_KEY", None)
stripe.api_key = STRIPE_API_KEY

# Base URL
BASE_URL = os.environ.get("BASE_URL", "http://localhost:8000")

# Celery
CELERY_RESULT_BACKEND = "django-db"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_BROKER_URL = os.environ.get(
    "CELERY_BROKER_URL", "amqp://guest:guest@localhost:5672//"
)

# Some tasks are not truly idempotent or transactional, so if you have the beat running and not
# the worker, if worker concurrency is greater than one, when the worker starts up again it'll
# execute the same periodic task simultaneously in multiple workers and things will get a bit
# weird (duplicate invoices for example...)
CELERY_WORKER_CONCURRENCY = os.environ.get("CELERY_WORKER_CONCURRENCY", 1)

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {"format": "[%(asctime)s] %(levelname)s %(name)s: %(message)s"},
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
    "loggers": {
        "hardware": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}
