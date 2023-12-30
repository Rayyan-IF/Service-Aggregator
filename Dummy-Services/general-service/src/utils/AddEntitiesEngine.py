import os
import importlib
from src.core.configs.database import engine

path_common = "src/core/entities/common"
path_master = "src/core/entities/master"

def addentities(dest_path):
    moduleNamesOST = os.listdir(dest_path)
    for moduleName in moduleNamesOST:
        name, ext = os.path.splitext(moduleName)
        if (ext == ".py"):
            importlib.import_module(dest_path.replace("/",".") + "." + name)

def addentitiesengine(migration:bool):

    if migration == True:
        #add the entire entities in advance
        addentities(path_common)
        addentities(path_master)

        #add the entire entities' Base.metadata and binding the DB engine
        moduleNamesOST = os.listdir(path_common)
        for moduleName in moduleNamesOST:
            name, ext = os.path.splitext(moduleName)
            if (ext == ".py"):
                module = importlib.import_module(path_common.replace("/",".") + "." + name)
                module.Base.metadata.create_all(bind=engine)

        moduleNamesOST = os.listdir(path_master)
        for moduleName in moduleNamesOST:
            name, ext = os.path.splitext(moduleName)
            if (ext == ".py"):
                module = importlib.import_module(path_master.replace("/",".") + "." + name)
                module.Base.metadata.create_all(bind=engine)
    else:
        #add the entire entities in advance
        addentities(path_common)
        addentities(path_master)