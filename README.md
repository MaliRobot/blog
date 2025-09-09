# Blog Project - Restructured

This is a restructured version of your Django blog project following best practices for better maintainability and organization.

## Project Structure

```
blog_restructured/
├── config/                    # Project configuration
│   ├── __init__.py
│   ├── settings/             # Settings module
│   │   ├── __init__.py
│   │   ├── base.py          # Base settings
│   │   ├── development.py   # Development settings
│   │   ├── production.py    # Production settings
│   │   └── testing.py       # Test settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration (for Django 3.0+)
│
├── apps/                     # All Django apps
│   ├── __init__.py
│   ├── core/                # Core functionality
│   ├── blog/                # Blog posts app
│   ├── news/                # News app
│   ├── events/              # Events app
│   ├── albums/              # Albums app
│   ├── poems/               # Poetry app
│   ├── about/               # About pages
│   ├── story/               # Stories app
│   └── access_log/          # Access logging
│
├── static/                   # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   ├── img/
│   └── vendor/              # Third-party static files
│
├── media/                    # User-uploaded files
│
├── templates/               # Project-wide templates
│   ├── base.html
│   ├── includes/
│   └── errors/
│
├── locale/                  # Translations
│
├── requirements/            # Requirements files
│   ├── base.txt
│   ├── development.txt
│   ├── production.txt
│   └── testing.txt
│
├── scripts/                 # Utility scripts
│   ├── entrypoint.sh
│   └── wait-for-it.sh
│
├── tests/                   # Project-wide tests
│
├── .env.example            # Example environment variables
├── .gitignore
├── docker-compose.yml
├── docker-compose.prod.yml
├── Dockerfile
├── manage.py
└── README.md
```

## Key Improvements

1. **Clear separation of concerns**: Project configuration is separated from apps
2. **Environment-specific settings**: Different settings for development, production, and testing
3. **Organized requirements**: Split requirements by environment
4. **Centralized templates**: Project-wide templates in one location
5. **Better app organization**: All apps under a single `apps` directory
6. **Proper static/media file handling**: Clear separation of static and media files
7. **Docker support**: Improved Docker configuration
8. **Testing structure**: Dedicated testing directory

## Migration Guide

Follow the migration steps in `MIGRATION_GUIDE.md` to move from the old structure to this new one.
