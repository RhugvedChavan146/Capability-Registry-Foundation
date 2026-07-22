# Capability Registry Foundation - API Documentation

## Overview

The Capability Registry exposes RESTful APIs for managing reusable software modules.

Base URL

```
http://localhost:8000
```

Swagger Documentation

```
http://localhost:8000/docs
```

---

# Modules API

## Register Module

POST

```
/modules
```

Request

```json
{
  "name": "Authentication Module",
  "category": "Security",
  "author": "John Doe",
  "version": "1.0.0",
  "tags": [
    "auth",
    "security"
  ]
}
```

Response

```json
{
  "id": 1,
  "message": "Module registered successfully"
}
```

---

## Get All Modules

GET

```
/modules
```

Response

```json
[
  {
    "id": 1,
    "name": "Authentication Module",
    "version": "1.0.0"
  }
]
```

---

## Get Module by ID

GET

```
/modules/{id}
```

---

## Update Module

PUT

```
/modules/{id}
```

---

## Delete Module

DELETE

```
/modules/{id}
```

---

# Category API

## Create Category

POST

```
/categories
```

---

## Get Categories

GET

```
/categories
```

---

## Update Category

PUT

```
/categories/{id}
```

---

## Delete Category

DELETE

```
/categories/{id}
```

---

# Search API

GET

```
/modules/search
```

Query Parameters

| Parameter | Description |
|------------|-------------|
| keyword | Search keyword |
| category | Module category |
| author | Module author |
| version | Module version |
| tag | Module tag |

Example

```
GET /modules/search?category=Security
```

---

# Validation

The application validates:

- Required fields
- JSON Schema
- Pydantic models
- Duplicate modules

---

# Status Codes

| Code | Description |
|------|-------------|
|200|Success|
|201|Created|
|400|Bad Request|
|404|Not Found|
|409|Duplicate Resource|
|500|Internal Server Error|

---

# Error Response

```json
{
  "detail": "Validation failed"
}
```

---

# OpenAPI Documentation

Interactive documentation is automatically generated using Swagger UI.

Available at:

```
/docs
```

Alternative documentation:

```
/redoc
```
