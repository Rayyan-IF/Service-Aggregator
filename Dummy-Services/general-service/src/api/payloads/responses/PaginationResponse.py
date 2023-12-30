def pagination_response(status_code:str, 
                        message:str, 
                        page:int, 
                        page_limit:int, 
                        npages:int,
                        nrows:int, 
                        data:list):
    return {
        "status_code" : status_code,
        "message" : message,
        "page" : page,
        "page_limit" : page_limit,
        "total_rows" : nrows,   
        "total_pages" : npages,
        "data" : data
    }