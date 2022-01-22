"""
Django settings for carshare project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-7am)+z!6v!9i731!p=gntgx6j$ns21@=hu&eoyg@0!in!1d=qa"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "192.168.1.77",
    "localhost",
    "172.20.10.6",
]

# Application definition

INSTALLED_APPS = [
    "billing.apps.BillingConfig",
    "bookings.apps.BookingsConfig",
    "drivers.apps.DriversConfig",
    "hardware.apps.HardwareConfig",
    "public.apps.PublicConfig",
    "users.apps.UsersConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "tailwind",
    "crispy_forms",
    "crispy_tailwind",
    "theme",
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
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
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
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_USERNAME_MIN_LENGTH = 3
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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"

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
EMAIL_HOST = "172.17.0.2"
EMAIL_PORT = 2500
EMAIL_USE_TLS = False
EMAIL_HOST_USER = "carshare@ioscv.co.uk"
EMAIL_HOST_PASSWORD = ""
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

MEDIA_ROOT = "media/"
