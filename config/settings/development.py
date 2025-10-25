"""
Development settings for blog project.

This file contains settings specific to the development environment.
"""

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

# Database - Use SQLite for development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Debug toolbar configuration
INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE.insert(1, 'debug_toolbar.middleware.DebugToolbarMiddleware')
INTERNAL_IPS = ['127.0.0.1', 'localhost']

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: DEBUG,
}

# Email backend for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Disable caching in development
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Django extensions (useful for development)
# try:
#     import django_extensions
#     INSTALLED_APPS += ['django_extensions']
# except ImportError:
#     pass

# Allow all origins in development (for CORS)
CORS_ALLOW_ALL_ORIGINS = True

# Logging - More verbose in development by default. Allow override via env for Docker noise control.
import os
_DJANGO_LOG_LEVEL = os.environ.get('DJANGO_LOG_LEVEL', 'DEBUG')
_DJANGO_SERVER_LOG_LEVEL = os.environ.get('DJANGO_SERVER_LOG_LEVEL', 'WARNING')
LOGGING['handlers']['console']['level'] = _DJANGO_LOG_LEVEL
LOGGING['loggers']['django']['level'] = _DJANGO_LOG_LEVEL
LOGGING['loggers']['apps']['level'] = _DJANGO_LOG_LEVEL
# Reduce noisy runserver request logs in development unless explicitly overridden
LOGGING['loggers']['django.server'] = {
    'handlers': ['console'],
    'level': _DJANGO_SERVER_LOG_LEVEL,
    'propagate': False,
}

# Static files
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# Media files - simplified for development
MEDIA_ROOT = BASE_DIR / 'media_dev'

# Disable SSL redirect in development
SECURE_SSL_REDIRECT = False

# Session settings for development
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# Silence system check for django_recaptcha test keys in development
SILENCED_SYSTEM_CHECKS = ['django_recaptcha.recaptcha_test_key_error']
