def pagination_response(status_code:str, message:str, page:int, page_limit:int, npages:int, nrows:int, data:list):
    return {
        "status_code" : status_code,
        "message" : message,
        "page_limit" : page_limit,
        "page" : page,
        "total_rows" : nrows,
        "total_pages" : npages,
        "data" : data
    }

def pagination_response_detail(status_code:str, message:str, page:int, page_limit:int, npages:int, nrows:int, data:object):
    return {
        "status_code" : status_code,
        "message" : message,
        "page_limit" : page_limit,
        "page" : page,
        "total_rows" : nrows,
        "total_pages" : npages,
        "data" : data
    }