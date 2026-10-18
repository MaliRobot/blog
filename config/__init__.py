# This is the main configuration package for the blog project

from .celery import app as celery_app

__all__ = ("celery_app",)
