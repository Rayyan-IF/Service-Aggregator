from src.core.configs.database import Base
from sqlalchemy import Column, Boolean, Integer, String

class MtrColour(Base):
    __tablename__ = "mtr_colour"
    is_active = Column(Boolean, nullable=False, default=True)
    colour_id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    colour_code = Column(String(100), nullable=False, unique=True)
    colour_commercial_name = Column(String(100), nullable=True, default="")
    colour_police_name = Column(String(100), nullable=True, default="")
    brand_id = Column(Integer, nullable=False)