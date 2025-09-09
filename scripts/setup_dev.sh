#!/bin/bash
# Development environment setup script

echo "Setting up development environment..."

# Create virtual environment
echo "Creating virtual environment..."
python -m venv venv
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements/development.txt

# Copy environment file
if [ ! -f .env ]; then
    echo "Creating .env file..."
    cp .env.example .env
    echo "Please update .env with your local settings"
fi

# Create necessary directories
echo "Creating directories..."
mkdir -p logs media staticfiles

# Run migrations
echo "Running migrations..."
python manage.py migrate

# Create superuser
echo "Creating superuser..."
python manage.py createsuperuser

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Setup complete! Run 'python manage.py runserver' to start the development server."
