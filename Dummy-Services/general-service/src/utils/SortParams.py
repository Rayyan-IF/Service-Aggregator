from sqlalchemy import column

def SortDataList(query_check: object, sort_params: dict(), default_sort_value: any):
    if (
        sort_params["sort_by"] == None
        or sort_params["sort_of"] == None
        or sort_params == None
    ):
        query_check = query_check.order_by(default_sort_value.asc())
        return query_check
    else:
        if sort_params["sort_of"] == "asc":
            query_check = query_check.order_by(column(sort_params["sort_by"]).asc())
        else:
            query_check = query_check.order_by(column(sort_params["sort_by"]).desc())
        return query_check
