from sqlalchemy import select, column
from sqlalchemy.orm import Session
from datetime import datetime

# please use this for header search
async def get_the_pagination_search(db:Session,query_str:object,all_params:dict()) -> object:
    query_check = query_str
    counter = len(db.scalars(query_check).all())
    n = len(all_params)
    idx = []
    for i in range(0,n):
        if list(all_params.values())[i]!=None:
            idx.append(i)
    if (idx != None):
        for j in range(len(idx)):
            key = list(all_params.keys())[idx[j]]
            value = list(all_params.values())[idx[j]]
            if (key.__contains__("date_from")):
                key_from = key.split("_from")
                value_from = datetime.strftime(value,"%Y-%m-%d")
                print(value_from)
                query_check = query_check.where(column(key_from[0]) >= value_from)
            elif (key.__contains__("date_to")):
                key_from = key.split("_to")
                value_to = datetime.strftime(value,"%Y-%m-%d")
                print(value_to)
                query_check = query_check.where(column(key_from[0]) <= value_to)
            else:
                query_check = query_check.where(column(key)==value)  
    return query_check,counter

async def get_the_pagination_search_list(db:Session,query_str:object,all_params:dict()) -> object:
    query_check = query_str
    counter = len(db.scalars(query_check).all())
    n = len(all_params)
    idx = []
    for i in range(0,n):
        if list(all_params.values())[i]!=None:
            idx.append(i)
    if (idx != None):
        for j in range(len(idx)):
            key = list(all_params.keys())[idx[j]]
            value = list(all_params.values())[idx[j]]
            if key != "is_active":
                query_check = query_check.where(column(key).contains(value))  
            else:
                query_check = query_check.where(column(key)==value)  
    return query_check,counter

# please use this for header search only for pop spm take to assign spm
async def get_the_pagination_search_spm(db:Session,query_str:object,all_params:dict()) -> object:
    query_check = query_str
    counter = len(db.scalars(query_check).all())
    n = len(all_params)
    idx = []
    for i in range(0,n):
        if list(all_params.values())[i]!=None:
            idx.append(i)
    if (idx != None):
        for j in range(len(idx)):
            key = list(all_params.keys())[idx[j]]
            value = list(all_params.values())[idx[j]]
            if (key.__contains__("spm_document_number_from")):
                key_from = key.split("_from")
                query_check = query_check.where(column(key_from[0]) >= value)
            elif (key.__contains__("spm_document_number_to")):
                key_to = key.split("_to")
                query_check = query_check.where(column(key_to[0]) <= value)
            else:
                query_check = query_check.where(column(key)==value)  
    return query_check,counter

#for pagination purposes with table also included
async def get_the_pagination(db:Session,basetable:object,query_str:object,all_params:dict())-> object:
    query_check = query_str
    count_data = select(basetable)
    counter = len(db.scalars(count_data).all())
    n = len(all_params)
    idx = []
    for i in range(0,n):
        if list(all_params.values())[i]!=None:
            idx.append(i)
    if (idx != None):
        for j in range(len(idx)):
            key = list(all_params.keys())[idx[j]]
            value = list(all_params.values())[idx[j]]
            if (key.__contains__("date_from")):
                key_from = key.split("_from")
                value_from = value.strftime("%Y-%m-%d")
                query_check = query_check.where(column(key_from[0]) >= value_from)
            elif (key.__contains__("date_to")):
                key_from = key.split("_to")
                value_to = value.strftime("%Y-%m-%d")
                query_check = query_check.where(column(key_from[0]) <= value_to)
            else:
                query_check = query_check.where(column(key)==value)  
    return query_check,counter

def get_the_pagination_search_with_join(query_str: object, all_params: dict, main_table: object, join_tables: list) -> object:
    query_check = query_str
    n = len(all_params)
    idx = []
    for i in range(n):
        if all_params.get(list(all_params.keys())[i]) is not None:
            idx.append(i)
    if (idx != None):
        for j in idx:
            key = list(all_params.keys())[j]
            value = list(all_params.values())[j]     
            key_column = None
            if (key.__contains__("date_from")):
                key_from = key.split("_from")
                value_from = value.strftime("%Y-%m-%d")
                print(value,value_from)
                query_check = query_check.where(column(key_from[0]) >= value_from)
            elif (key.__contains__("date_to")):
                key_from = key.split("_to")
                value_to = value.strftime("%Y-%m-%d")
                print(value,value_to)
                query_check = query_check.where(column(key_from[0]) <= value_to)
            else:
                for table in join_tables:
                    if key in [column.name for column in table.__table__.columns]:
                        key_column = getattr(table, key)
                        break   
                if not key_column:
                    key_column = getattr(main_table, key)
                query_check = query_check.where(key_column == value)  
    return query_check

def get_the_pagination_search_with_join_new(query_str: object, all_params: dict, tables: list) -> object:
    query_check = query_str
    n = len(all_params)
    idx = []
    for i in range(n):
        if all_params.get(list(all_params.keys())[i]) is not None:
            idx.append(i)
    if (idx != None):
        for j in idx:
            key = list(all_params.keys())[j]
            value = list(all_params.values())[j]     
            key_column = None
            if (key.__contains__("date_from")):
                key_from = key.split("_from")
                value_from = value.strftime("%Y-%m-%d")
                print(value,value_from)
                query_check = query_check.where(column(key_from[0]) >= value_from)
            elif (key.__contains__("date_to")):
                key_from = key.split("_to")
                value_to = value.strftime("%Y-%m-%d")
                print(value,value_to)
                query_check = query_check.where(column(key_from[0]) <= value_to)
            else:
                for table in tables:
                    if key in [column.name for column in table.__table__.columns]:
                        key_column = getattr(table, key)
                        break   
                if not key_column:
                    key_column = getattr(table, key)
                query_check = query_check.where(key_column == value)  
    return query_check