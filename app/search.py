from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.models import Module


def search_modules(
    db: Session,
    keyword: str = None,
    category: str = None,
    version: str = None,
    author: str = None
):
    """
    Search and filter modules based on:
    - keyword (name or description)
    - category
    - version
    - author
    """

    query = db.query(Module)

    # Search by keyword in name or description
    if keyword:
        query = query.filter(
            or_(
                Module.name.ilike(f"%{keyword}%"),
                Module.description.ilike(f"%{keyword}%")
            )
        )

    # Filter by category
    if category:
        query = query.filter(Module.category == category)

    # Filter by version
    if version:
        query = query.filter(Module.version == version)

    # Filter by author
    if author:
        query = query.filter(Module.author == author)

    return query.all()


def search_by_name(db: Session, name: str):
    """Search modules by exact name."""
    return db.query(Module).filter(Module.name == name).all()


def get_modules_by_category(db: Session, category: str):
    """Get all modules in a category."""
    return db.query(Module).filter(Module.category == category).all()


def get_modules_by_version(db: Session, version: str):
    """Get all modules with a specific version."""
    return db.query(Module).filter(Module.version == version).all()


def get_modules_by_author(db: Session, author: str):
    """Get all modules created by a specific author."""
    return db.query(Module).filter(Module.author == author).all()