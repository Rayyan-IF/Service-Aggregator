def payload_response(status_code:str, message:str, data:list):
    return {
        "status_code" : status_code,
        "message" : message,
        "data" : data
    }

def payload_response_detail(status_code:str, message:str, obj:object):
    return {
        "status_code" : status_code,
        "message" : message,
        "data" : obj
    }