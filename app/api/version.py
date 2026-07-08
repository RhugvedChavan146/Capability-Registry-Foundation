from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import re

router = APIRouter(
    prefix="/versions",
    tags=["Version Management"]
)

# Temporary in-memory storage
versions = []


# -----------------------------
# Pydantic Model
# -----------------------------
class Version(BaseModel):
    version: str


# -----------------------------
# Validate Semantic Version
# Example: 1.0.0
# -----------------------------
def validate_version(version: str):

    pattern = r"^\d+\.\d+\.\d+$"

    return re.match(pattern, version)


# -----------------------------
# Create Version
# -----------------------------
@router.post("/")
def create_version(data: Version):

    if not validate_version(data.version):
        raise HTTPException(
            status_code=400,
            detail="Invalid version format. Use x.y.z"
        )

    if data.version in versions:
        raise HTTPException(
            status_code=409,
            detail="Version already exists."
        )

    versions.append(data.version)

    return {
        "message": "Version created successfully.",
        "version": data.version
    }


# -----------------------------
# Get All Versions
# -----------------------------
@router.get("/")
def get_versions():

    return {
        "versions": versions
    }


# -----------------------------
# Update Version
# -----------------------------
@router.put("/{old_version}")
def update_version(
    old_version: str,
    data: Version
):

    if old_version not in versions:
        raise HTTPException(
            status_code=404,
            detail="Version not found."
        )

    if not validate_version(data.version):
        raise HTTPException(
            status_code=400,
            detail="Invalid version format."
        )

    index = versions.index(old_version)

    versions[index] = data.version

    return {
        "message": "Version updated successfully.",
        "version": data.version
    }


# -----------------------------
# Delete Version
# -----------------------------
@router.delete("/{version}")
def delete_version(version: str):

    if version not in versions:
        raise HTTPException(
            status_code=404,
            detail="Version not found."
        )

    versions.remove(version)

    return {
        "message": "Version deleted successfully."
    }