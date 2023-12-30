from pydantic import BaseModel

class UnitColourRequest(BaseModel):
    brand_id:int
    colour_code:str
    colour_commercial_name:str
    colour_police_name:str

class UnitColourRequestUpdate(BaseModel):
    colour_commercial_name:str
    colour_police_name:str

class UnitColourResponse(UnitColourRequest):
    colour_id: int
    is_active: bool
    brand_name: str