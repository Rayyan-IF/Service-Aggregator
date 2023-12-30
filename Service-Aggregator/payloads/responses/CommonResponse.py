def payload_response(status_code:str, message:str, data:list):
    return {
        "status_code" : status_code,
        "message" : message,
        "data" : data
    }