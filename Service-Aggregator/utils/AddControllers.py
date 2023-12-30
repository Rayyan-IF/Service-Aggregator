import os
import importlib
from fastapi import APIRouter

populate_router = APIRouter()

moduleNamesOST = os.listdir("controllers")

for moduleName in moduleNamesOST:
    name, ext = os.path.splitext(moduleName)
    if (ext == ".py"):
        module = importlib.import_module("controllers." + name)
        populate_router.include_router(module.router)