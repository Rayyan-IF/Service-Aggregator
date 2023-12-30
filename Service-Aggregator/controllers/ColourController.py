import sys 
sys.path.append("..")
from services import ColourService
from fastapi import APIRouter, HTTPException, status
from exceptions.RequestException import ResponseException
from payloads.responses.CommonResponse import payload_response

router = APIRouter(tags=["Event Colour"], prefix="/colour")

@router.get("/colour", status_code=200)
async def get_all_colour(page:int, limit:int, colour_code:str|None=None, colour_commercial_name:str|None=None,
                         colour_police_name:str|None=None, brand_name:str|None=None, sort_by:str|None=None, sort_of:str|None=None):
    
    all_params = {
        "brand_name":brand_name,
        "colour_code":colour_code,
        "colour_police_name":colour_police_name,
        "colour_commercial_name":colour_commercial_name,
    }
    sort_params = {
        "sort_by":sort_by,
        "sort_of":sort_of
    }
    get_results, err = await ColourService.get_all_colour(page, limit, all_params, sort_params)
    if get_results == [] or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=ResponseException(404))
    return payload_response(200, "Success", get_results)