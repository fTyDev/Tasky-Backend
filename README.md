# Todo Backend

A Django-based REST API for a todo application.

## Features

- User authentication using django-allauth
- PostgreSQL database
- Dockerized development environment

## Getting Started

1. Build and start the containers:
```bash
docker-compose up --build
```

2. Run migrations:
```bash
docker-compose exec web python manage.py migrate
```

3. Create a superuser (optional):
```bash
docker-compose exec web python manage.py createsuperuser
```

The application will be available at `http://localhost:8000`

## Development

The project uses:
- Django 5.2
- PostgreSQL 14
- Poetry for dependency management
- Docker for containerization