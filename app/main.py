# Project Structure:
# project/
# ├── app/
# │   ├── __init__.py
# │   ├── main.py
# │   ├── config.py
# │   ├── database.py
# │   ├── models/
# │   │   ├── __init__.py
# │   │   └── user.py
# │   ├── schemas/
# │   │   ├── __init__.py
# │   │   └── user.py
# │   ├── api/
# │   │   ├── __init__.py
# │   │   ├── deps.py
# │   │   └── v1/
# │   │       ├── __init__.py
# │   │       ├── endpoints/
# │   │       │   ├── __init__.py
# │   │       │   ├── users.py
# │   │       │   └── health.py
# │   │       └── api.py
# │   ├── core/
# │   │   ├── __init__.py
# │   │   ├── security.py
# │   │   └── logging.py
# │   └── middleware/
# │       ├── __init__.py
# │       └── logging.py
# ├── tests/
# │   ├── __init__.py
# │   └── test_api.py
# ├── alembic/
# │   └── versions/
# ├── .env.example
# ├── .gitignore
# ├── requirements.txt
# ├── Dockerfile
# ├── docker-compose.yml
# └── README.md

# ============= app/main.py =============

# ============= app/config.py =============


# ============= app/database.py =============


# ============= app/models/user.py =============

# ============= app/schemas/user.py =============


# ============= app/core/security.py =============

# ============= app/core/logging.py =============


# ============= app/middleware/logging.py =============


# ============= app/api/deps.py =============


# ============= app/api/v1/endpoints/health.py =============


# ============= app/api/v1/endpoints/users.py =============


# ============= app/api/v1/api.py =============


# ============= requirements.txt =============
# fastapi==0.104.1
# uvicorn[standard]==0.24.0
# sqlalchemy==2.0.23
# alembic==1.12.1
# psycopg2-binary==2.9.9
# pydantic==2.5.0
# pydantic-settings==2.1.0
# python-jose[cryptography]==3.3.0
# passlib[bcrypt]==1.7.4
# python-multipart==0.0.6
# redis==5.0.1
# httpx==0.25.2
# pytest==7.4.3
# pytest-asyncio==0.21.1


# ============= Dockerfile =============


# ============= docker-compose.yml =============


# ============= .env.example =============
# PROJECT_NAME="FastAPI Production App"
# VERSION="1.0.0"
# API_V1_STR="/api/v1"
# 
# DATABASE_URL="postgresql://postgres:postgres@localhost:5432/fastapi_db"
# 
# SECRET_KEY="your-secret-key-here-change-this"
# ALGORITHM="HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES=30
# 
# ALLOWED_ORIGINS=["http://localhost:3000"]
# ALLOWED_HOSTS=["*"]
# 
# ENVIRONMENT="development"
# DEBUG=True
# 
# REDIS_URL="redis://localhost:6379"


# ============= .gitignore =============
# __pycache__/
# *.py[cod]
# *$py.class
# *.so
# .env
# .venv
# env/
# venv/
# .pytest_cache/
# .coverage
# htmlcov/
# dist/
# build/
# *.egg-info/
# .DS_Store