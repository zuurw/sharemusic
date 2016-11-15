"""
Django settings for sharemusic project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
#sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'sharemusic/apps/ext'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'core.User'

if DEBUG:
    DEBUG_LEVEL = 'DEBUG'
else:
    DEBUG_LEVEL = 'INFO'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'sharemusic.log'),
            'formatter': 'verbose'
        },
        'file_error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'sharemusic.error.log'),
            'formatter': 'verbose'
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file', 'file_error'],
            'propagate': True,
            'level': 'INFO',
        },
        'sharemusic': {
            'handlers': ['console', 'file', 'file_error'],
            'level': DEBUG_LEVEL,
        },
    }
}


# Application definition
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'pipeline',
    'djangobower',
    'sendfile',
    # apps
    'sharemusic.apps.storage',
    'sharemusic.apps.core',
    'sharemusic.apps.client'
]

OLD_PASSWORD_FIELD_ENABLED = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

MIDDLEWARE_CLASSES = (
    'sharemusic.apps.client.middleware.RemoveNextMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.gzip.GZipMiddleware',
)

SENDFILE_BACKEND = 'sendfile.backends.nginx'
SENDFILE_ROOT = '/usr/src/app/music'
SENDFILE_URL = '/proxied-download'

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': 'redis:6379',
    },
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

ROOT_URLCONF = 'sharemusic.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'sharemusic.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'postgres',
        'PORT': 5432,
    }
}

FIXTURE_DIRS = (
   os.path.join(BASE_DIR, 'sharemusic/fixtures'),
)

# bower config
BOWER_INSTALLED_APPS = (
    'jquery',
    'jplayer',
    'angular',
    'bootstrap',
    'angular-bootstrap',
    'angular-resource',
    'dndLists',
    'underscore',
    'angular-dropdowns',
    'angular-cookies',
    'json3',
    'es5-shim',
    'angular-sanitize',
    'angular-route',
    'chieffancypants/angular-hotkeys',
    'ng-file-upload',
    'angular-growl-notifications',
    'angular-animate',
)

# pipeline config
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.FileSystemFinder',
    'pipeline.finders.AppDirectoriesFinder',
    'pipeline.finders.CachedFileFinder',
    'pipeline.finders.PipelineFinder',
)
PIPELINE_COMPILERS = (
    'pipeline.compilers.less.LessCompiler',
)

PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'

PIPELINE_CSS = {
    'client': {
        'source_filenames': (
            'client/bower_components/bootstrap/dist/css/bootstrap.min.css',
            'client/style/sharemusic.less',
            'client/style/filebrowser.less',
            'client/style/mediaplayer.less',
            'client/style/playlist.less',
            'client/style/dropdowns.less',
        ),
        'output_filename': 'client/sharemusic.css',
        }
}
PIPELINE_JS = {
    'client': {
        'source_filenames': (
            'client/bower_components/jquery/dist/jquery.min.js',
            'client/bower_components/jPlayer/dist/jplayer/jquery.jplayer.min.js',
            'client/bower_components/angular/angular.min.js',
            'client/bower_components/angular-resource/angular-resource.min.js',
            'client/bower_components/angular-drag-and-drop-lists/angular-drag-and-drop-lists.min.js',
            'client/bower_components/angular-bootstrap/ui-bootstrap.min.js',
            'client/bower_components/angular-bootstrap/ui-bootstrap-tpls.min.js',
            'client/bower_components/underscore/underscore-min.js',
            'client/bower_components/angular-dropdowns/dist/angular-dropdowns.min.js',
            'client/bower_components/angular-cookies/angular-cookies.min.js',
            'client/bower_components/json3/lib/json3.min.js',
            'client/bower_components/es5-shim/es5-shim.min.js',
            'client/bower_components/angular-sanitize/angular-sanitize.min.js',
            'client/bower_components/angular-route/angular-route.min.js',
            'client/bower_components/angular-hotkeys/build/hotkeys.min.js',
            'client/bower_components/ng-file-upload/ng-file-upload-shim.min.js',
            'client/bower_components/ng-file-upload/ng-file-upload.min.js',
            'client/bower_components/angular-growl-notifications/dist/angular-growl-notifications.min.js',
            'client/bower_components/angular-animate/angular-animate.min.js',
            'client/js/main.js',
            'client/js/auth-user/django_auth.js',
            'client/js/auth-user/validate.js',
            'client/js/controllers/change_password.js',
            'client/js/controllers/dropdown_top_menu.js',
            'client/js/controllers/main_view.js',
            'client/js/controllers/jplayer.js',
            'client/js/controllers/playlists.js',
            'client/js/directives/progressbar.js',
            'client/js/directives/file.js',
            'client/js/directives/filebrowser.js',
            'client/js/directives/mediaplayer.js',
            'client/js/directives/playlist.js',
            'client/js/directives/playlistbrowser.js',
            'client/js/filters/timeago.js',
            'client/js/filters/timeformat.js',
            'client/js/resources/browse.js',
            'client/js/resources/directory.js',
            'client/js/resources/index_directory.js',
            'client/js/resources/playlist.js',
            'client/js/resources/search.js',
            'client/js/resources/track.js',
            'client/js/resources/user.js',
            'client/js/resources/user_settings.js',
            'client/js/resources/playback_service.js',
            'client/js/resources/playback_service_jplayer.js',
            'client/js/hotkeys.js',
        ),
        'output_filename': 'client/sharemusic.js'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'static'),
#)

BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'sharemusic/apps/client/static/client')
