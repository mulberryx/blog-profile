import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SERVER_INDEX = BASE_DIR.index("/server")
WEB_DIR = BASE_DIR[:SERVER_INDEX] + "/web/dist"

print(WEB_DIR)

SECRET_KEY = "ushgp7_joel_+d)hx187xlv(x!_ezrl+&+_d_e-&ks2cj#ufj("

DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  "django.contrib.messages",
  "db",
  "app",
]

MIDDLEWARE = [
  "django.middleware.security.SecurityMiddleware",
  "django.contrib.sessions.middleware.SessionMiddleware",
  "django.middleware.common.CommonMiddleware",
  "django.middleware.csrf.CsrfViewMiddleware",
  "django.contrib.auth.middleware.AuthenticationMiddleware",
  "django.contrib.messages.middleware.MessageMiddleware",
  "django.middleware.clickjacking.XFrameOptionsMiddleware"
]

ROOT_URLCONF = "app.urls"

TEMPLATES = [
  {
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [WEB_DIR,],
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

WSGI_APPLICATION = "app.wsgi.application"

DATABASES = {
  "default": {
    "ENGINE": "django.db.backends.mysql",
    "NAME": "robot",
    "USER": "root",
    "PASSWORD": "wowcxy2008",
    "HOST":"localhost",
    "PORT":"3306",
  }
}

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

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOGIN_URL = "admin/login"
LOGIN_EXEMPT_URLS = [
  "",
  "talk",
  "api/getWeather",
  "admin/login"
]
