from datetime import timedelta
from pathlib import Path
#################################################


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# СИКРЕТНЫЙ КЛЮЧ ДЛЯ АУТЕНТИФИКАЦИИ (для безопасности) (должен быть случайным и не должен быть открыт в коде)
SECRET_KEY = 'django-insecure-ys^r=vca2j)oa$2u-zl*oz*aeyz4k=+*831%!jx^$z&5d%l-6c'


# !!!! ПРИ РЕЛИЗЕ ОТКЛЮЧИТЬ ДИБАГ !!!!
DEBUG = True


ALLOWED_HOSTS = []


#Стандартные приложения джанго
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

    
# Дополнительные приложения библиотек для джанго
INSTALLED_APPS += [
    'phonenumber_field',
    'rest_framework',
    'djoser',
]


#приложения проекта
INSTALLED_APPS += [
    'api',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'Tomsk_kedr.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'Tomsk_kedr.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#Импорт аутентификации кастомной модели пользователя 
AUTH_USER_MODEL = 'api.User'


#Импорт бэкенда аутентификации
AUTHENTICATION_BACKENDS = ('api.backends.AuthBackend',)


###########################
#  DJANGO REST FRAMEWORK #
##########################
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FileUploadParser',
    ],
}


#######################
#       DJOSER        #
#######################
DJOSER = {
    'SERIALIZERS' : {
        'user_create' : 'users.serializers.UserSerializer'
    },
    #'USER_CREATE_PASSWORD_RETYPE': True,
    #'SET_PASSWORD_RETYPE': True,
    #'SEND_CONFIRMATION_EMAIL': True,
    #'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
    #'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    'PASSWORD_RESET_CONFIRM': True,
    'PASSWORD_RESET_CONFIRM_URL': 'api/djoser-auth/users/reset_password_confirm/{uid}/{token}',
    #'USERNAME_RESET_CONFIRM_URL': 'api/v1/email/reset/confirm/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'EMAIL_FRONTEND_URL' : 'томскстолицакедра.рф/{uid}/{token}',
    'ACTIVATION_URL': 'api/activate/{uid}/{token}',
}

DEFAULT_FROM_EMAIL = 'support@xn--80aaldnlcfhtc4aebkf5e.xn--p1ai'
SERVER_EMAIL = 'admin@mail.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'connect.smtp.bz'
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'krysanovmatvei@gmail.com'
EMAIL_HOST_PASSWORD = 'sRaRnQOJXaDy'
EMAIL_PORT = 587