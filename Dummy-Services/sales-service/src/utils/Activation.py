from sqlalchemy.orm import Session

def activation(db:Session,table_query:object):
    active_status = db.scalars(table_query).first()
    active_status.is_active = not active_status.is_active
    db.commit()
    db.refresh(active_status)
    return active_status

def activation_general_service(db:Session,table_query:object):
    if hasattr(table_query, 'is_active'):
        table_query.is_active = not table_query.is_active
        db.commit()
        db.refresh(table_query)
        return table_query
    raise f'table {table_query.__class__.__name__} has not column is_active'
