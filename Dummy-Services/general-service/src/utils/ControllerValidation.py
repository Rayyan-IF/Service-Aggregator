from fastapi import HTTPException, status
from src.exceptions.RequestException import ResponseException
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response

def get_validation(result,err):
    if err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",result)

def post_validation(result,err):
    if not result or err != None:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,detail=ResponseException(400))
    return payload_response(201,"Created",result)

def update_validation(result,err):
    if not result or err != None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=ResponseException(400))
    return payload_response(200,"Updated",result)

def delete_validation(result,err):
    if not result or err != None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=ResponseException(403))
    return payload_response(204,"Deleted",result)

def paggination_controller_validation(
        result, 
        err, 
        err_code, 
        success_code, 
        success_note,
        page,
        limit,
        npages,
        nrows
    ):
    if err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=ResponseException(err_code))
    return pagination_response(success_code, success_note,page,limit,npages,nrows,result)