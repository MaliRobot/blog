from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.blog'
    verbose_name = 'Blog'
    
    def ready(self):
        """Import signal handlers."""
        try:
            import apps.blog.signals  # noqa
        except ImportError:
            pass
