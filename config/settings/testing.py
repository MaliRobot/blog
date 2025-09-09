"""
Testing settings for blog project.

This file contains settings specific to running tests.
"""

from .base import *

# Use SQLite for faster tests
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# Disable migrations for faster tests
class DisableMigrations:
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None

MIGRATION_MODULES = DisableMigrations()

# Use simple password hasher for faster tests
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# Disable cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Email backend for testing
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

# Static files storage
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# Media files for testing
MEDIA_ROOT = BASE_DIR / 'test_media'

# Disable debug toolbar in tests
DEBUG = False
INTERNAL_IPS = []

# Celery - Use synchronous mode for testing
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True

# Logging - Minimal logging during tests
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'null': {
            'class': 'logging.NullHandler',
        },
    },
    'root': {
        'handlers': ['null'],
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
        },
        'apps': {
            'handlers': ['null'],
        },
    },
}

# Disable SSL redirect for tests
SECURE_SSL_REDIRECT = False

# Test-specific settings
TEST_RUNNER = 'django.test.runner.DiscoverRunner'
