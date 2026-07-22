# Capability Registry Foundation - Deployment Guide

## Overview

This guide explains how to deploy and run the Capability Registry Foundation locally.

---

# Prerequisites

- Python 3.10+
- pip
- Git

---

# Clone Repository

```bash
git clone <repository-url>

cd capability-registry-foundation
```

---

# Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Application

```bash
uvicorn app.main:app --reload
```

Example

```
http://localhost:8000
```

---

# Access API Documentation

Swagger

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

# Database

Database

```
SQLite
```

The SQLite database is automatically created during application startup if it does not already exist.

---

# Environment Variables

Example

```env
DATABASE_URL=sqlite:///database.db
```

---

# Production Deployment

Recommended server

```
Uvicorn
```

Example

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

---

# Recommended Improvements

- Docker
- PostgreSQL
- Nginx
- Gunicorn
- HTTPS
- CI/CD
- Monitoring

---

# Health Check

Verify server availability

```
GET /
```

or

```
GET /docs
```

---

# Troubleshooting

## Missing Dependencies

```bash
pip install -r requirements.txt
```

## Port Already in Use

```bash
uvicorn app.main:app --port 8001
```

## Database Errors

Delete the SQLite database and restart the application.

---

# Deployment Workflow

```
Clone Repository

↓

Create Virtual Environment

↓

Install Dependencies

↓

Run Uvicorn

↓

Database Initialization

↓

Application Ready
```
