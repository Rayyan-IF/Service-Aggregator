from sqlalchemy.orm import Session
from src.core.repositories.master import UnitBrandRepo

async def get_unit_brand_all(db:Session, page:int, limit:int, all_params=dict(), sort_params=dict()):
    results, err = await UnitBrandRepo.get_unit_brand_all(db, page, limit, all_params, sort_params) 
    if err != None:
        results = None
    return results, err