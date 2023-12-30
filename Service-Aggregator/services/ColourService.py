import json
import pandas as pd
from messaging.Client import Colours, Brands
from utils.AddPagination import pagination, filtering

async def get_all_colour(page:int, limit:int, all_params=dict(), sort_params=dict()):
    # Calling call method to send request (event) and convert the response to python object
    getColour = json.loads(Colours().call())
    getBrand = json.loads(Brands().call())
    # Dataframes with inner-join
    colourDF = pd.DataFrame(getColour)
    brandDF =  pd.DataFrame(getBrand)
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
    # Pagination with page & limit for the data
    dataPagination = pagination(filteredDF, page, limit)
    # Column selection for the response
    selectedData  = dataPagination[["colour_id", "colour_code", "colour_commercial_name", "colour_police_name", "brand_id", "brand_name", "is_active_colour"]].to_json(orient="records")
    finalResult = json.loads(selectedData)
    return finalResult, None