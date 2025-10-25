# Multi-stage Dockerfile for Django blog application

# Base stage
FROM python:3.11-slim as base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    gdal-bin \
    libgdal-dev \
    libpq-dev \
    libxml2-dev \
    libxslt1-dev \
    libffi-dev \
    libjpeg-dev \
    libpng-dev \
    gettext \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create app directory
WORKDIR /app

# Development stage
FROM base as development

# Copy requirements
COPY requirements/base.txt /app/base.txt
COPY requirements/development.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy application code
COPY . /app/

# Create necessary directories
RUN mkdir -p /app/logs /app/media /app/staticfiles

# Production stage
FROM base as production

# Copy requirements
COPY requirements/base.txt /app/base.txt
COPY requirements/production.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Install runtime tools for entrypoint (bash + netcat)
RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    netcat-openbsd \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy application code
COPY . /app/

# Copy entrypoint script and make it executable
COPY scripts/entrypoint.sh /app/scripts/entrypoint.sh
RUN chmod +x /app/scripts/entrypoint.sh

# Create necessary directories and set permissions
RUN mkdir -p /app/logs /app/media /app/staticfiles && \
    groupadd -r django && \
    useradd -r -g django django && \
    chown -R django:django /app

# Collect static files at build time (safe; no DB required)
RUN python manage.py collectstatic --noinput

# Switch to non-root user
USER django

# Expose port
EXPOSE 8000

# Set entrypoint to run migrations at container startup and then start gunicorn
ENTRYPOINT ["/app/scripts/entrypoint.sh"]

# Run gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "--threads", "2", "--timeout", "120", "config.wsgi:application"]
