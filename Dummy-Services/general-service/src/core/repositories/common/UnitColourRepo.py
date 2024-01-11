from sqlalchemy import select
from sqlalchemy.orm import Session
from src.core.entities.common.UnitColourEntity import MtrColour

async def get_unit_colour_list_all(db:Session, page:int, limit:int, all_params=dict(), sort_params=dict()):
    try:
        query_set = select(MtrColour).order_by(MtrColour.colour_id).offset(page*limit).limit(limit)
        results = db.scalars(query_set).all()
        return results, None
    except Exception as err:
        return None, err