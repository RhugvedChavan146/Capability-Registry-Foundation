from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)
categories = []

@router.post("/")
def create_category(name: str):

    if name in categories:
        raise HTTPException(
            status_code=409,
            detail="Category already exists."
        )
    categories.append(name)
    return {
        "message": "Category created successfully.",
        "category": name
    }


# -----------------------------
# Get All Categories
# -----------------------------
@router.get("/")
def get_categories():

    return {
        "categories": categories
    }


# -----------------------------
# Update Category
# -----------------------------
@router.put("/{old_name}")
def update_category(
    old_name: str,
    new_name: str
):

    if old_name not in categories:
        raise HTTPException(
            status_code=404,
            detail="Category not found."
        )

    if new_name in categories:
        raise HTTPException(
            status_code=409,
            detail="Category already exists."
        )

    index = categories.index(old_name)

    categories[index] = new_name

    return {
        "message": "Category updated successfully."
    }


# -----------------------------
# Delete Category
# -----------------------------
@router.delete("/{name}")
def delete_category(name: str):

    if name not in categories:
        raise HTTPException(
            status_code=404,
            detail="Category not found."
        )

    categories.remove(name)

    return {
        "message": "Category deleted successfully."
    }