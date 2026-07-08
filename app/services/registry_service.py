from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models import Module


class RegistryService:

    @staticmethod
    def register_module(db: Session, module):

        existing = db.query(Module).filter(
            Module.name == module.name
        ).first()

        if existing:
            raise HTTPException(
                status_code=409,
                detail="Module already exists."
            )

        new_module = Module(
            name=module.name,
            description=module.description,
            category=module.category,
            version=module.version,
            author=module.author
        )

        db.add(new_module)
        db.commit()
        db.refresh(new_module)

        return new_module

    @staticmethod
    def get_all_modules(db: Session):

        return db.query(Module).all()

    @staticmethod
    def get_module(db: Session, module_id: int):

        module = db.query(Module).filter(
            Module.id == module_id
        ).first()

        if module is None:
            raise HTTPException(
                status_code=404,
                detail="Module not found."
            )

        return module

    @staticmethod
    def delete_module(db: Session, module_id: int):

        module = db.query(Module).filter(
            Module.id == module_id
        ).first()

        if module is None:
            raise HTTPException(
                status_code=404,
                detail="Module not found."
            )

        db.delete(module)
        db.commit()

        return {
            "message": "Module deleted successfully."
        }