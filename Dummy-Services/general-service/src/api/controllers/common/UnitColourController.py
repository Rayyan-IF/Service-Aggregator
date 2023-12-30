from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from src.core.configs.database import get_db
from src.core.services.common import UnitColourService
from src.api.exceptions.RequestException import ResponseException
from src.api.payloads.responses.GeneralResponse import payload_response

router = APIRouter(tags=["Master : Unit Colour API"], prefix="/api/sales")

@router.get("/unit-colour")
async def get_unit_colour_list_all(page:int, limit:int,
                                   brand_code:str|None=None,
                                   colour_code:str|None=None,
                                   colour_commercial_name:str|None=None,
                                   colour_police_name:str|None=None,
                                   is_active:bool|None=None,
                                   sort_by:str|None=None,
                                   sort_of:str|None=None,
                                   db:Session=Depends(get_db)):

    all_params = {
        "colour_code": colour_code,
        "colour_police_name": colour_police_name,
        "colour_commercial_name": colour_commercial_name,
        "brand_code": brand_code,
        "is_active": is_active
    }

    sort_params = {
        "sort_by": sort_by,
        "sort_of": sort_of
    }
    results, err = await UnitColourService.get_unit_colour_list_all(db, page, limit, all_params, sort_params)
    if results == [] and err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=ResponseException(404))
    return payload_response(200, "Success", results)