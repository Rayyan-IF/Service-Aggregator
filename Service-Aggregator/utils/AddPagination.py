def pagination(dataframe, page:int, limit:int):
    start_index = page * limit
    last_index = start_index + limit
    return dataframe.iloc[start_index:last_index]

def filtering(dataframe, all_params:dict()):
    df = dataframe
    for key, value in all_params.items():
        if value == None:
            continue
        df.query(f"{key} == '{value}'", inplace=True)
    return df