from pydantic import BaseModel


class ModuleBase(BaseModel):

    name: str

    description: str

    category: str

    version: str

    author: str


class ModuleCreate(ModuleBase):
    pass


class ModuleUpdate(ModuleBase):
    pass


class ModuleResponse(ModuleBase):

    id: int

    class Config:
        from_attributes = True