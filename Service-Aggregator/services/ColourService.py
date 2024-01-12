import json
import pandas as pd
from messaging.Client import Rpc
from utils.AddPagination import filtering

async def get_all_colour(page:int, limit:int, all_params=dict(), sort_params=dict()):
    try:
        # Calling call method to send request (event) and convert the response to python object
        pagination = json.dumps({"page":page, "limit":limit})
        getColour = json.loads(Rpc("colour_queue", pagination).call())
        colourDF = pd.DataFrame(getColour)
        brandID = json.dumps(colourDF.get("brand_id").tolist())
        getBrand = json.loads(Rpc("brand_queue", brandID).call())
        brandDF =  pd.DataFrame(getBrand)
        # Dataframes with inner-join
        colourBrand = pd.merge(colourDF, brandDF, on='brand_id', how="inner", suffixes=("_colour", "_brand"))
        # Query filtering with pandas
        filteredDF = filtering(colourBrand, all_params)
        # Data sorting
        if sort_params["sort_by"] == None or sort_params["sort_of"] == None:
            filteredDF.sort_values(by="colour_id", ascending=True, inplace=True)
        else:
            if sort_params["sort_of"] == "desc":
                filteredDF.sort_values(by=f"{sort_params['sort_by']}", ascending=False, inplace=True)
            else:
                filteredDF.sort_values(by=f"{sort_params['sort_by']}", ascending=True, inplace=True)
        # Column selection for the response
        selectedData  = filteredDF[["colour_id", "colour_code", "colour_commercial_name", "colour_police_name", "brand_id", "brand_name", "is_active_colour"]].to_json(orient="records")
        finalResult = json.loads(selectedData)
        return finalResult, None
    except Exception as err:
        return None, err