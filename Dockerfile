# Multi-stage Dockerfile for Django blog application

# Base stage
FROM python:3.12-slim as base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive \
    UV_PYTHON=python3.12 \
    PATH="/app/.venv/bin:/bin:/usr/local/bin:$PATH"

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
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

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Create app directory
WORKDIR /app

# Development stage
FROM base as development

# Copy project files
COPY pyproject.toml uv.lock /app/

# Install Python dependencies using uv
RUN uv sync --frozen --group dev

# Copy application code
COPY . /app/

# Create necessary directories
RUN mkdir -p /app/logs /app/media /app/staticfiles

# Production stage
FROM base as production

# Copy project files
COPY pyproject.toml uv.lock /app/

# Install Python dependencies using uv
RUN uv sync --frozen --no-group dev

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

# Collect static files at build time
# Use uv run to ensure we are in the environment
RUN uv run python manage.py collectstatic --noinput

# Switch to non-root user
USER django

# Expose port
EXPOSE 8000

# Set entrypoint to run migrations at container startup and then start gunicorn
ENTRYPOINT ["/app/scripts/entrypoint.sh"]

# Run gunicorn using uv run
CMD ["/bin/uv", "run", "gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "--threads", "2", "--timeout", "120", "config.wsgi:application"]
