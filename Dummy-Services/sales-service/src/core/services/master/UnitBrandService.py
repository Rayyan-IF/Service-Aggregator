from sqlalchemy.orm import Session
from src.core.repositories.master import UnitBrandRepo

async def get_unit_brand_all(db:Session, page:int, limit:int, all_params=dict(), sort_params=dict()):
    results, err = await UnitBrandRepo.get_unit_brand_all(db, page, limit, all_params, sort_params) 
    if err != None:
        results = None
    return results, err

async def get_brand_multi_id(db:Session, brand_idstr:str):
    header_result, err = await UnitBrandRepo.get_brand_multi_id(db, brand_idstr)
    if err == None:
        return header_result, None
    else:
        return None, err