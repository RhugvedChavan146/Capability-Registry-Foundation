import re
from fastapi import HTTPException

SEMVER_PATTERN = r"^\d+\.\d+\.\d+$"


def validate_module(module):

    required_fields = [
        "name",
        "description",
        "category",
        "version",
        "author"
    ]

    for field in required_fields:

        value = getattr(module, field)

        if value is None or str(value).strip() == "":
            raise HTTPException(
                status_code=400,
                detail=f"{field} is required."
            )

    if not re.match(SEMVER_PATTERN, module.version):
        raise HTTPException(
            status_code=400,
            detail="Version must follow semantic versioning (Example: 1.0.0)"
        )

    return True