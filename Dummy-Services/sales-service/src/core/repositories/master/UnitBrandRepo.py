import ast
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.core.entities.master.BrandEntity import MtrBrand

async def get_unit_brand_all(db:Session, page:int, limit:int, all_params=dict(), sort_params=dict()):
    try:
        query_set = select(MtrBrand).order_by(MtrBrand.brand_id).offset(page*limit).limit(limit)
        results = db.scalars(query_set).all()
        return results, None
    except Exception as err:
        return None, err
    
async def get_brand_multi_id(db:Session, brand_idstr:str):
    try:
        res_str = ast.literal_eval(brand_idstr)
        header_check_query = select(MtrBrand).where(MtrBrand.brand_id.in_(res_str))
        header_result = db.execute(header_check_query)
        return header_result.scalars().fetchall(), None
    except Exception as err:
        return None, err