.PHONY: help install install-dev migrate makemigrations superuser \
        run shell test coverage lint format clean docker-up docker-down \
        docker-build docker-logs collectstatic

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## Install production dependencies
	pip install -r requirements/production.txt

install-dev: ## Install development dependencies
	pip install -r requirements/development.txt

migrate: ## Run database migrations
	python manage.py migrate

makemigrations: ## Create new migrations
	python manage.py makemigrations

superuser: ## Create a superuser
	python manage.py createsuperuser

run: ## Run development server
	python manage.py runserver

shell: ## Open Django shell
	python manage.py shell_plus --ipython

test: ## Run tests
	python manage.py test

coverage: ## Run tests with coverage
	coverage run --source='.' manage.py test
	coverage report
	coverage html

lint: ## Run linting
	flake8 apps/
	pylint apps/

format: ## Format code with black
	black apps/
	isort apps/

clean: ## Clean up generated files
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name "htmlcov" -exec rm -rf {} +
	find . -type f -name ".coverage" -delete
	find . -type f -name "db.sqlite3" -delete

docker-up: ## Start Docker containers
	docker-compose up -d

docker-down: ## Stop Docker containers
	docker-compose down

docker-build: ## Build Docker containers
	docker-compose build

docker-logs: ## View Docker logs
	docker-compose logs -f

collectstatic: ## Collect static files
	python manage.py collectstatic --noinput

# Development shortcuts
dev-reset: clean ## Reset development environment
	rm -rf venv/
	python -m venv venv
	. venv/bin/activate && pip install -r requirements/development.txt
	cp .env.example .env
	python manage.py migrate
	python manage.py loaddata fixtures/initial_data.json

prod-deploy: ## Deploy to production (example)
	@echo "Running production deployment..."
	git pull origin main
	pip install -r requirements/production.txt
	python manage.py migrate --noinput
	python manage.py collectstatic --noinput
	sudo systemctl restart gunicorn
	sudo systemctl restart nginx
