import pandas as pd
import requests
import json
from sqlalchemy import column

def GetUrlDataframe(api_url: str, params: dict):
     
     response = requests.get(api_url, params=params)

     json_data = response.json()

     data = json_data["data"]
     
     df = pd.DataFrame(data)

     return df 


def CreateWhereStatement(query_str: object, all_params: dict()) -> object:
    query_check = query_str
    n = len(all_params)
    idx = []
    for i in range(0, n):
        if list(all_params.values())[i] != None:
            idx.append(i)
    if idx != None:
        for j in range(len(idx)):
            key = list(all_params.keys())[idx[j]]
            value = list(all_params.values())[idx[j]]
            query_check = query_check.where(column(key) == value)
    return query_check
          