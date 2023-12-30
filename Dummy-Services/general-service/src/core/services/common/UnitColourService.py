from sqlalchemy.orm import Session
from src.core.repositories.common import UnitColourRepo

async def get_unit_colour_list_all(db:Session, page:int, limit:int, all_params=dict(), sort_params=dict()):
    results, err = await UnitColourRepo.get_unit_colour_list_all(db, page, limit, all_params, sort_params)
    if err != None:
       results = None
    return results, err