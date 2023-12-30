from pydantic import BaseModel

class PaginationSchema(BaseModel):
    rows:list = []

    class Config:
        from_attributes = True