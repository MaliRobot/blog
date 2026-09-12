#!/bin/bash
set -e

# Defaults for Compose production if not provided via env
export DB_HOST=${DB_HOST:-db}
export DB_PORT=${DB_PORT:-5432}

echo "Waiting for PostgreSQL to start at ${DB_HOST}:${DB_PORT}..."
while ! nc -z "$DB_HOST" "$DB_PORT"; do
  sleep 0.5
done
echo "PostgreSQL started"

echo "Running migrations..."
uv run python manage.py makemigrations --noinput
uv run python manage.py migrate --noinput

echo "Collecting static files..."
uv run python manage.py collectstatic --noinput

echo "Starting server..."
exec "$@"
