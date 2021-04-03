import os
import psycopg2
from pathlib import Path
from decouple import config
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
try:
    SECRET_KEY = os.environ.get("SECRET_KEY")
except:
    SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
try:
    DEBUG = config("DEBUG")
except:
    DEBUG = os.environ.get("DEBUG")

ALLOWED_HOSTS = [
    "audiocave.herokuapp.com",
    "127.0.0.1",
    "localhost",
]

# CSRF
CORS_ORIGIN_ALLOW_ALL = False
CSRF_COOKIE_NAME = "csrftoken"
CORS_ORIGIN_WHITELIST = [
    "https://audiocave.herokuapp.com",
    "https://localhost:3000",
    "http://localhost:5000",
    "https://localhost:5000",
    "http://localhost:3000",
    "http://127.0.0.1:8000",
]
CORS_ALLOW_CREDENTIALS = True

# Application definition

INSTALLED_APPS = [
    "channels",
    "music_room.apps.MusicRoomConfig",
    "spotifyapi.apps.SpotifyapiConfig",
    "youtubeapi.apps.YoutubeapiConfig",
    "chatroom.apps.ChatroomConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "django_extensions",
    "ckeditor",
    "corsheaders",
    "rest_framework",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "web_main.urls"

ASGI_APPLICATION = "web_main.asgi.application"

# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             "hosts": [('127.0.0.1', 6379)],
#         },
#     },
# }


CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}

TEMPLATE_DIR = os.path.join(BASE_DIR, "music_room", "templates", "music_room/")

REACT_APP_DIR = os.path.join(BASE_DIR, "frontend/build")

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            REACT_APP_DIR,
        ],
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

# WSGI_APPLICATION = "web_main.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

try:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "USER": config("DB_USER"),
            "NAME": config("DB_NAME"),
            "HOST": config("DB_HOST"),
            "PASSWORD": config("DB_PASSWORD"),
            "PORT": config("DB_PORT"),
        },
    }

except:
    try:
        DB_HEROKU_URL = os.environ.get("DB_HEROKU_URL")
        DATABASES["default"] = dj_database_url.config(
            conn_max_age=600, ssl_require=True
        )
        DATABASES["default"] = dj_database_url.config(default=DB_HEROKU_URL)
        DATABASES["default"] = dj_database_url.parse(
            DB_HEROKU_URL,
            conn_max_age=600,
        )

    except:
        DB_HEROKU_URL = os.environ.get("DATABASE_URL")
        DATABASES["default"] = dj_database_url.config(
            conn_max_age=600, ssl_require=True
        )
        DATABASES["default"] = dj_database_url.config(default=DB_HEROKU_URL)
        DATABASES["default"] = dj_database_url.parse(
            DB_HEROKU_URL,
            conn_max_age=600,
        )

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_DIRS = [os.path.join(BASE_DIR, "frontend/build/static")]

MEDIA_ROOT = os.path.join(BASE_DIR, "music_room/static/music_room/images/")

MEDIA_URL = "/music_room/static/music_room/images/"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
