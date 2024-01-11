import sys 
sys.path.append("..")
from services import ItemService
from fastapi import APIRouter, HTTPException, status
from exceptions.RequestException import ResponseException
from payloads.responses.CommonResponse import payload_response

router = APIRouter(tags=["Event Item"], prefix="/item")

@router.get("/item", status_code=200)
async def get_all_item(page:int, limit:int, item_code:str|None=None, item_name:str|None=None, item_type:str|None=None, item_class_code:str|None=None, 
                       item_group_code:str|None=None, supplier_code:str|None=None, supplier_name:str|None=None, is_active:bool|None=None, sort_by:str|None=None, sort_of:str|None=None):
    all_params = {
        "item_code":item_code,
        "item_name":item_name,
        "item_type":item_type,
        "item_class_code":item_class_code,
        "item_group_code":item_group_code,
        "supplier_code":supplier_code,
        "supplier_name":supplier_name,
        "is_active_item":is_active,
    }
    sort_params = {
        "sort_by":sort_by,
        "sort_of":sort_of
    }
    get_results, err = await ItemService.get_all_item(page, limit, all_params, sort_params)
    if get_results == [] or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=ResponseException(404))
    return payload_response(200, "Success", get_results)