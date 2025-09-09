# Migration Guide: From Old Structure to New Structure

This guide will help you migrate your Django blog project from the old structure to the new, improved structure.

## Prerequisites

1. **Backup your data**: Before starting, make sure to backup your database and media files.
2. **Version control**: Ensure your code is committed to version control.

## Step-by-Step Migration

### 1. Create New Project Structure

```bash
# Create the new directory structure
mkdir -p blog_restructured/{config/settings,apps,static/{css,js,img},media,templates/{includes,errors},requirements,scripts,tests}
```

### 2. Move Configuration Files

```bash
# Move Django project files to config directory
mkdir -p blog_restructured/config
cp nonliteral/settings.py blog_restructured/config/settings/base.py
cp nonliteral/urls.py blog_restructured/config/urls.py
cp nonliteral/wsgi.py blog_restructured/config/wsgi.py

# Update manage.py
cp nonliteral/manage.py blog_restructured/manage.py
```

### 3. Migrate Apps

Move each app to the `apps` directory and update imports:

```bash
# Example for the posts app (renamed to blog)
cp -r nonliteral/posts blog_restructured/apps/blog
cp -r nonliteral/news blog_restructured/apps/news
cp -r nonliteral/events blog_restructured/apps/events
# ... repeat for other apps
```

### 4. Update Imports

Update all imports in your code:

**Old imports:**
```python
from posts.models import Post
from news.views import NewsListView
```

**New imports:**
```python
from apps.blog.models import Post
from apps.news.views import NewsListView
```

### 5. Update Settings

1. Split `settings.py` into environment-specific files
2. Update `INSTALLED_APPS` to use new app paths:

```python
LOCAL_APPS = [
    'apps.core',
    'apps.blog',  # instead of 'posts'
    'apps.news',
    # ... other apps
]
```

### 6. Update URL Configuration

Update `urls.py` to include apps from new locations:

```python
urlpatterns = [
    path('', include('apps.core.urls')),
    path('blog/', include('apps.blog.urls')),
    # ... other patterns
]
```

### 7. Move Templates

Consolidate templates:

```bash
# Move app templates to centralized location
mkdir -p blog_restructured/templates/{blog,news,events}
cp -r nonliteral/posts/templates/* blog_restructured/templates/blog/
# ... repeat for other apps
```

### 8. Move Static Files

```bash
# Move static files
cp -r nonliteral/core/rest_framework/* blog_restructured/static/vendor/
# Move other static assets
```

### 9. Update Database Migrations

Since app names are changing, you'll need to:

1. **Option A: Fresh Start** (Recommended for development)
   ```bash
   # Delete old migrations
   find apps -path "*/migrations/*.py" -not -name "__init__.py" -delete
   
   # Create new migrations
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Option B: Preserve Data** (For production)
   - Use Django's `MIGRATION_MODULES` setting to map old app names to new ones
   - Or manually update migration files to reflect new app structure

### 10. Update Docker Configuration

1. Copy new Docker files:
   ```bash
   cp docker-compose.yml blog_restructured/
   cp Dockerfile blog_restructured/
   ```

2. Update environment variables in `.env` file

### 11. Install Dependencies

```bash
cd blog_restructured
pip install -r requirements/development.txt
```

### 12. Test the Migration

1. Run migrations:
   ```bash
   python manage.py migrate
   ```

2. Collect static files:
   ```bash
   python manage.py collectstatic
   ```

3. Run development server:
   ```bash
   python manage.py runserver
   ```

## Post-Migration Checklist

- [ ] All apps are working correctly
- [ ] Admin interface is accessible
- [ ] Static files are loading
- [ ] Media files are accessible
- [ ] API endpoints are functioning
- [ ] Tests are passing
- [ ] Docker containers start successfully

## Troubleshooting

### Import Errors

If you get import errors, search and replace old import paths:

```bash
# Find all Python files with old imports
grep -r "from posts" --include="*.py" .
grep -r "from news" --include="*.py" .

# Use your IDE's find/replace to update imports
```

### Migration Conflicts

If you have migration conflicts:

1. Back up your database
2. Note down any custom migrations
3. Reset migrations for affected apps
4. Recreate migrations with new app structure

### Static Files Not Loading

1. Check `STATIC_URL` and `STATIC_ROOT` settings
2. Run `python manage.py collectstatic`
3. Ensure your web server is configured to serve static files

## Benefits After Migration

1. **Better Organization**: Clear separation between project config and apps
2. **Environment-Specific Settings**: Easy switching between dev/staging/production
3. **Improved Maintainability**: Logical grouping of related functionality
4. **Better Testing**: Centralized test directory
5. **Docker Ready**: Improved containerization setup
6. **Production Ready**: Security and performance optimizations included
