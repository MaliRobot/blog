#!/bin/bash

# Deployment script for native DigitalOcean Droplet setup
# Assumes: 
# 1. Project is already cloned
# 2. uv is installed on the system
# 3. .venv is created
# 4. .env file is configured correctly
# 5. Systemd service is named 'blog'

set -e

PROJECT_DIR="/home/django/blog"  # Adjust to your actual path
SERVICE_NAME="blog"              # Adjust to your actual systemd service name

echo "Starting deployment..."

cd $PROJECT_DIR

# 1. Pull latest code
echo "Pulling latest changes from git..."
git pull origin main

# 2. Sync dependencies using uv
echo "Syncing dependencies..."
uv sync --frozen --no-group dev

# 3. Run migrations
echo "Running migrations..."
uv run python manage.py migrate --noinput

# 4. Collect static files
echo "Collecting static files..."
uv run python manage.py collectstatic --noinput

# 5. Restart application service
echo "Restarting $SERVICE_NAME service..."
sudo systemctl restart $SERVICE_NAME

# Optional: Restart Celery services if they exist
# sudo systemctl restart blog-celery
# sudo systemctl restart blog-celery-beat

echo "Deployment completed successfully!"
