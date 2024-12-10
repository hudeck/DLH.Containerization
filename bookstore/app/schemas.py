from typing import ClassVar
from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    price: float

    ConfigDict: ClassVar[dict] = {"from_attributes": True}  # Correctly annotated as ClassVar

class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id: int

    ConfigDict: ClassVar[dict] = {"from_attributes": True}  # Correctly annotated as ClassVar
