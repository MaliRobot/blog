### Native Deployment Guide (DigitalOcean Droplet)

This guide helps you set up and deploy the blog project natively on a Ubuntu Droplet using `uv`, `Gunicorn`, `Systemd`, `Nginx`, and `MySQL`.

#### 1. Initial Server Setup

Install system dependencies:
```bash
sudo apt update
sudo apt install -y git build-essential libpq-dev libmysqlclient-dev pkg-config python3-dev
```

Install `uv`:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.cargo/env
```

#### 2. Project Preparation

Clone the repository and set up the environment:
```bash
git clone <your-repo-url> /home/django/blog
cd /home/django/blog
uv venv
cp .env.example .env
# Edit .env and set production values (especially DB and SECRET_KEY)
# Ensure DB_ENGINE is set to 'django.db.backends.mysql' in your settings if using MySQL
```

#### 3. Database Configuration (MySQL)

Create the database and user:
```sql
CREATE DATABASE nonliteral CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'nonliteral'@'localhost' IDENTIFIED BY 'your-password';
GRANT ALL PRIVILEGES ON nonliteral.* TO 'nonliteral'@'localhost';
FLUSH PRIVILEGES;
```

#### 4. Systemd Service Setup

Create a service file at `/etc/systemd/system/blog.service`:
```ini
[Unit]
Description=Gunicorn instance to serve blog
After=network.target

[Service]
User=django
Group=www-data
WorkingDirectory=/home/django/blog
Environment="PATH=/home/django/blog/.venv/bin"
EnvironmentFile=/home/django/blog/.env
ExecStart=/home/django/blog/.venv/bin/gunicorn \
    --workers 3 \
    --bind unix:blog.sock \
    config.wsgi:application

[Install]
WantedBy=multi-user.target
```

Start and enable the service:
```bash
sudo systemctl start blog
sudo systemctl enable blog
```

#### 5. Deployment Automation

Once the initial setup is done, you can use the deployment script to push updates:

```bash
# On the server
make deploy
```

The `scripts/deploy_native.sh` script will:
1. `git pull` the latest changes.
2. `uv sync` the dependencies.
3. Run `python manage.py migrate`.
4. Run `python manage.py collectstatic`.
5. Restart the `blog` service.

#### 6. Nginx Configuration

Configure Nginx to proxy requests to Gunicorn:
```nginx
server {
    listen 80;
    server_name your_domain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/django/blog;
    }

    location /media/ {
        root /home/django/blog;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/django/blog/blog.sock;
    }
}
```
