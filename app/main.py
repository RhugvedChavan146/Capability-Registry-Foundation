from fastapi import FastAPI, Depends, HTTPException
from fastapi.openapi.utils import get_openapi
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app import models, schemas, crud
from app.validators import validate_version
from app.search import search_modules

from app.api.category import router as category_router
from app.api.version import router as version_router


# -----------------------------
# Create Database Tables
# -----------------------------
Base.metadata.create_all(bind=engine)


# -----------------------------
# FastAPI Application
# -----------------------------
app = FastAPI(
    title="Capability Registry Foundation",
    description="Reusable Capability Registry API",
    version="1.0.0"
)


# -----------------------------
# Remove 422 Validation Error from Swagger
# -----------------------------
def custom_openapi():

    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )

    # Remove 422 Validation Error
    for path in openapi_schema["paths"].values():
        for operation in path.values():
            if "responses" in operation:
                operation["responses"].pop("422", None)

    app.openapi_schema = openapi_schema

    return app.openapi_schema


app.openapi = custom_openapi


# -----------------------------
# Include Routers
# -----------------------------
app.include_router(category_router)
app.include_router(version_router)


# -----------------------------
# Home
# -----------------------------
@app.get("/")
def home():

    return {
        "message": "Capability Registry Foundation API is Running"
    }


# -----------------------------
# Register Module
# -----------------------------
@app.post("/modules", response_model=schemas.ModuleResponse)
def register_module(
    module: schemas.ModuleCreate,
    db: Session = Depends(get_db)
):

    if not validate_version(module.version):
        raise HTTPException(
            status_code=400,
            detail="Invalid version format. Use x.y.z"
        )

    existing = db.query(models.Module).filter(
        models.Module.name == module.name
    ).first()

    if existing:
        raise HTTPException(
            status_code=409,
            detail="Module already exists."
        )

    return crud.create_module(db, module)


# -----------------------------
# Get All Modules
# -----------------------------
# -----------------------------
# Get All Modules
# -----------------------------
@app.get("/modules", response_model=list[schemas.ModuleResponse])
def get_all_modules(db: Session = Depends(get_db)):
    return crud.get_modules(db)


# -----------------------------
# Search & Filter Modules
# -----------------------------
@app.get("/modules/search")
def search(
    keyword: str = None,
    category: str = None,
    version: str = None,
    author: str = None,
    db: Session = Depends(get_db)
):
    return search_modules(
        db=db,
        keyword=keyword,
        category=category,
        version=version,
        author=author
    )


# -----------------------------
# Get Module By ID
# -----------------------------
@app.get("/modules/{module_id}", response_model=schemas.ModuleResponse)
def get_module(
    module_id: int,
    db: Session = Depends(get_db)
):
    module = crud.get_module(db, module_id)

    if module is None:
        raise HTTPException(
            status_code=404,
            detail="Module not found."
        )

    return module


# -----------------------------
# Update Module
# -----------------------------
@app.put("/modules/{module_id}", response_model=schemas.ModuleResponse)
def update_module(
    module_id: int,
    module: schemas.ModuleUpdate,
    db: Session = Depends(get_db)
):
    if not validate_version(module.version):
        raise HTTPException(
            status_code=400,
            detail="Invalid version format. Use x.y.z"
        )

    updated = crud.update_module(db, module_id, module)

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Module not found."
        )

    return updated


# -----------------------------
# Delete Module
# -----------------------------
@app.delete("/modules/{module_id}")
def delete_module(
    module_id: int,
    db: Session = Depends(get_db)
):
    deleted = crud.delete_module(db, module_id)

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Module not found."
        )

    return {
        "message": "Module deleted successfully."
    }

# -----------------------------
# Health Check
# -----------------------------
@app.get("/health")
def health_check():

    return {
        "status": "Healthy",
        "application": "Capability Registry Foundation"
    }