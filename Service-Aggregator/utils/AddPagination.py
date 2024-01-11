def filtering(dataframe, all_params:dict()):
    df = dataframe
    for key, value in all_params.items():
        if value == None:
            continue
        df.query(f"{key} == '{value}'", inplace=True)
    return df