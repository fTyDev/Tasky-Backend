# Authentication System Changes

## Problem Solved
The allauth login page was redirecting with a 302 status code to profile pages instead of returning login-related details like tokens.

## Changes Made

### 1. Settings Configuration (`todo_project/settings.py`)
- Added allauth configuration to disable redirects
- Added REST framework authentication settings
- Added token authentication support

### 2. Custom Authentication Views (`todo_app/views.py`)
- `login_view`: Returns JSON with token instead of redirecting
- `logout_view`: Returns JSON response instead of redirecting
- `register_view`: Returns JSON with token after registration
- `user_profile_view`: Returns user profile data as JSON

### 3. URL Configuration (`todo_project/urls.py`)
- Replaced allauth URLs with custom authentication endpoints
- New endpoints:
  - `/auth/login/` - Login with email/password
  - `/auth/logout/` - Logout and invalidate token
  - `/auth/register/` - Register new user
  - `/auth/profile/` - Get user profile

## API Endpoints

### Login
```http
POST /auth/login/
Content-Type: application/json

{
    "email": "user@example.com",
    "password": "password123"
}
```

**Response:**
```json
{
    "token": "your-auth-token-here",
    "user": {
        "id": 1,
        "email": "user@example.com",
        "username": "username"
    },
    "message": "Login successful"
}
```

### Register
```http
POST /auth/register/
Content-Type: application/json

{
    "email": "user@example.com",
    "username": "username",
    "password": "password123",
    "password2": "password123",
    "date_of_birth": "1990-01-01"
}
```

**Response:**
```json
{
    "token": "your-auth-token-here",
    "user": {
        "id": 1,
        "email": "user@example.com",
        "username": "username"
    },
    "message": "Registration successful"
}
```

### Logout
```http
POST /auth/logout/
Authorization: Token your-auth-token-here
```

**Response:**
```json
{
    "message": "Logout successful"
}
```

### Get Profile
```http
GET /auth/profile/
Authorization: Token your-auth-token-here
```

**Response:**
```json
{
    "id": 1,
    "email": "user@example.com",
    "username": "username",
    "date_of_birth": "1990-01-01",
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-01T00:00:00Z"
}
```

## Usage

### 1. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 2. Start Server
```bash
python manage.py runserver
```

### 3. Test Endpoints
Use the provided `test_auth.py` script:
```bash
python test_auth.py
```

## Key Benefits

1. **No More Redirects**: Login/register endpoints return JSON responses instead of redirecting
2. **Token Authentication**: Secure token-based authentication for API access
3. **Profile Data**: Access user profile data via API endpoint
4. **Clean API**: All authentication operations return structured JSON responses

## Security Features

- Token-based authentication
- Password validation
- Login attempt limits
- Secure logout (token deletion)
- Email-based authentication 