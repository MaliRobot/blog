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
try:
    import django_extensions
    INSTALLED_APPS += ['django_extensions']
except ImportError:
    pass

# Allow all origins in development (for CORS)
CORS_ALLOW_ALL_ORIGINS = True

# Logging - More verbose in development
LOGGING['handlers']['console']['level'] = 'DEBUG'
LOGGING['loggers']['django']['level'] = 'DEBUG'
LOGGING['loggers']['apps']['level'] = 'DEBUG'

# Static files
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# Media files - simplified for development
MEDIA_ROOT = BASE_DIR / 'media_dev'

# Disable SSL redirect in development
SECURE_SSL_REDIRECT = False

# Session settings for development
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
