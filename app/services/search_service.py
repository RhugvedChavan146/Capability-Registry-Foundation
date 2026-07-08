from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.models import Module


class SearchService:

    @staticmethod
    def search_modules(
        db: Session,
        keyword: str = None,
        category: str = None,
        version: str = None,
        author: str = None
    ):

        query = db.query(Module)

        if keyword:
            query = query.filter(
                or_(
                    Module.name.ilike(f"%{keyword}%"),
                    Module.description.ilike(f"%{keyword}%")
                )
            )

        if category:
            query = query.filter(Module.category == category)

        if version:
            query = query.filter(Module.version == version)

        if author:
            query = query.filter(Module.author == author)

        return query.all()