from sqlalchemy.orm import Session
from app import models, schemas


def create_module(db: Session, module: schemas.ModuleCreate):

    db_module = models.Module(**module.model_dump())

    db.add(db_module)

    db.commit()

    db.refresh(db_module)

    return db_module


def get_modules(db: Session):

    return db.query(models.Module).all()


def get_module(db: Session, module_id: int):

    return db.query(models.Module).filter(
        models.Module.id == module_id
    ).first()


def update_module(db: Session, module_id: int, module):

    db_module = get_module(db, module_id)

    if db_module:

        for key, value in module.model_dump().items():
            setattr(db_module, key, value)

        db.commit()

        db.refresh(db_module)

    return db_module


def delete_module(db: Session, module_id: int):

    db_module = get_module(db, module_id)

    if db_module:

        db.delete(db_module)

        db.commit()

    return db_module