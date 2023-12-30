from pydantic import BaseModel

class UnitBrandRequest(BaseModel):
    supplier_id:int
    warehouse_id:int
    brand_code:str
    brand_name:str
    brand_abbreviation:str
    brand_must_withdrawal:bool
    brand_must_pdi:bool
    atpm_unit:bool
    atpm_workshop:bool
    atpm_sparepart:bool
    atpm_finance:bool
    
class UnitBrandMultiRequest(BaseModel):
    brand_id:list[int]