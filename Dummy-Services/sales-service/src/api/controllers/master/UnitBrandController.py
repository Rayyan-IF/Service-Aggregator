from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from src.core.configs.database import get_db
from src.core.services.master import UnitBrandService
from src.api.payloads.responses.CommonResponse import payload_response 

router = APIRouter(tags=["Master : Unit Brand API"], prefix="/api/sales")

@router.get("/unit-brand", status_code=status.HTTP_200_OK)
async def get_unit_brand_all(page:int, limit:int,                   
                             brand_code:str|None=None,
                             brand_name:str|None=None,
                             is_active:bool|None=None,
                             sort_by:str|None=None,
                             sort_of:str|None=None,
                             db:Session=Depends(get_db)):
    
    all_params = {
        "brand_code":brand_code,
        "brand_name":brand_name,
        "is_active":is_active
    }

    sort_params = {
        "sort_by":sort_by,
        "sort_of":sort_of
    }

    results, err = await UnitBrandService.get_unit_brand_all(db, page, limit, all_params, sort_params)
    if results == [] and err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))
    return payload_response(200, "Success", results)

@router.get("/brand-multi-id/{brand_idstr}")
async def get_brand_multi_id(brand_idstr:str, db:Session=Depends(get_db)):
    results, err = await UnitBrandService.get_brand_multi_id(db, brand_idstr)
    if results == None and err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))
    return payload_response(200, "Success", results)