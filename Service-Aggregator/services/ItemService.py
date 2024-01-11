import json
import pandas as pd
from messaging.Client import Rpc
from utils.AddPagination import filtering

async def get_all_item(page:int, limit:int, all_params=dict(), sort_params=dict()):
    try:
        # Calling call method to send request (event) and convert the response to python object
        paginationData = json.dumps({"page": page, "limit": limit})
        getItem = json.loads(Rpc("item_queue", paginationData).call())
        getSupplier = json.loads(Rpc("supplier_queue", paginationData).call())
        # Dataframes with inner-join
        itemDF =  pd.DataFrame(getItem)
        supplierDF = pd.DataFrame(getSupplier)
        itemSupplier = pd.merge(itemDF, supplierDF, on='supplier_id', how="inner", suffixes=("_item", "_supplier"))
        # Query filtering with pandas
        filteredDF = filtering(itemSupplier, all_params)
        # Data sorting
        if sort_params["sort_by"] == None or sort_params["sort_of"] == None:
            filteredDF.sort_values(by="item_id", ascending=True, inplace=True)
        else:
            if sort_params["sort_of"] == "desc":
                filteredDF.sort_values(by=f"{sort_params['sort_by']}", ascending=False, inplace=True)
            else:
                filteredDF.sort_values(by=f"{sort_params['sort_by']}", ascending=True, inplace=True)
        # Column selection for the response
        selectedData  = filteredDF[["item_id", "item_code", "item_name", "item_type", "item_class_code", 
                                    "item_group_code", "supplier_name", "supplier_code", "is_active_item"]].to_json(orient="records")
        finalResult = json.loads(selectedData)
        return finalResult, None
    except Exception as err:
        return None, err