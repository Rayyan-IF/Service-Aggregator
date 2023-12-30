from typing import List
from pydantic import BaseModel

class PaginationSchema(BaseModel):
    page_limit:int
    page:int
    total_rows:int
    total_pages:int
    rows:list = []

    class Config:
        from_attributes = True