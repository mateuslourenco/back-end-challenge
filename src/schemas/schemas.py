"""
Um schema é o formato de dados que a respota irá retornar no endpoint.
"""

from typing import Optional, List

from pydantic import BaseModel


class News(BaseModel):
    id: Optional[int] = None
    featured: bool
    title: str
    url: str
    imageUrl: str
    newsSite: str
    summary: str
    publishedAt: str
    launches: Optional[List]
    events: Optional[List]

    class Config:
        orm_mode = True
