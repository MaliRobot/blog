# Project Structure Documentation

## Overview

This document explains the restructured Django blog project organization and the rationale behind each decision.

## Directory Structure Explained

### `/config/`
Contains all Django project configuration files:
- `settings/`: Split settings by environment (base, development, production, testing)
- `urls.py`: Main URL configuration
- `wsgi.py`: WSGI application for production
- `asgi.py`: ASGI application for async support

**Benefits:**
- Clear separation between configuration and application code
- Easy environment switching
- Better security (different settings per environment)

### `/apps/`
Contains all Django applications:
- Each app is self-contained with its own models, views, URLs, and templates
- Common structure for each app:
  ```
  app_name/
  ├── migrations/      # Database migrations
  ├── templates/       # App-specific templates
  ├── static/          # App-specific static files
  ├── api/            # REST API views and serializers
  ├── management/     # Custom management commands
  ├── tests/          # App tests
  ├── models.py       # Data models
  ├── views.py        # View logic
  ├── urls.py         # URL patterns
  ├── forms.py        # Django forms
  ├── admin.py        # Admin configuration
  └── apps.py         # App configuration
  ```

### `/static/`
Project-wide static files:
- `css/`: Stylesheets
- `js/`: JavaScript files
- `img/`: Images
- `vendor/`: Third-party assets

### `/media/`
User-uploaded files (handled by Django's media files system)

### `/templates/`
Project-wide templates:
- `base.html`: Base template for inheritance
- `includes/`: Reusable template partials
- `errors/`: Error page templates

### `/requirements/`
Split requirements by environment:
- `base.txt`: Common dependencies
- `development.txt`: Dev-only dependencies
- `production.txt`: Production dependencies
- `testing.txt`: Testing dependencies

### `/scripts/`
Utility scripts:
- `entrypoint.sh`: Docker entrypoint
- `setup_dev.sh`: Development setup script
- Other automation scripts

### `/tests/`
Project-wide tests that don't belong to specific apps

### `/docs/`
Project documentation

## Best Practices Implemented

1. **Twelve-Factor App Methodology**
   - Environment-based configuration
   - Dependencies explicitly declared
   - Config stored in environment variables

2. **Security First**
   - Separate settings for each environment
   - Secrets managed through environment variables
   - Security headers configured in production

3. **Scalability**
   - Redis caching ready
   - Celery for async tasks
   - Static files served efficiently

4. **Development Experience**
   - Docker for consistent environments
   - Debug toolbar in development
   - Comprehensive logging

5. **Testing**
   - Separate test settings
   - Test utilities and factories
   - Coverage reporting

6. **API Design**
   - RESTful API structure
   - Versioned APIs
   - Consistent serialization

## Configuration Management

### Environment Variables
Key environment variables:
- `DJANGO_SETTINGS_MODULE`: Specifies which settings to use
- `SECRET_KEY`: Django secret key
- `DEBUG`: Debug mode flag
- `DATABASE_URL`: Database connection string
- `REDIS_URL`: Redis connection string

### Settings Organization
- `base.py`: Common settings for all environments
- `development.py`: Overrides for local development
- `production.py`: Production-specific settings
- `testing.py`: Test-specific settings

## Development Workflow

1. **Local Development**
   ```bash
   # Using Django development server
   python manage.py runserver
   
   # Using Docker
   docker-compose up
   ```

2. **Running Tests**
   ```bash
   # Run all tests
   python manage.py test
   
   # Run specific app tests
   python manage.py test apps.blog
   ```

3. **Database Migrations**
   ```bash
   # Create migrations
   python manage.py makemigrations
   
   # Apply migrations
   python manage.py migrate
   ```

## Deployment Considerations

1. **Static Files**
   - Use WhiteNoise or CDN
   - Run `collectstatic` during deployment

2. **Media Files**
   - Use cloud storage (S3, GCS)
   - Configure proper CORS headers

3. **Database**
   - Use connection pooling
   - Regular backups
   - Read replicas for scaling

4. **Caching**
   - Redis for session storage
   - Cache frequently accessed data
   - Implement cache invalidation

5. **Monitoring**
   - Sentry for error tracking
   - Application metrics
   - Performance monitoring

## Maintenance

1. **Dependency Updates**
   - Regular security updates
   - Test thoroughly after updates
   - Use dependabot or similar

2. **Database Maintenance**
   - Regular backups
   - Optimize queries
   - Monitor slow queries

3. **Code Quality**
   - Pre-commit hooks
   - Code formatting (Black)
   - Linting (flake8, pylint)
   - Type hints where appropriate
