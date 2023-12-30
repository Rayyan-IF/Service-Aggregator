from src.core.configs.database import Base
from sqlalchemy import Column, Boolean, Integer, String

class MtrBrand(Base):
    __tablename__ = "mtr_brand"
    is_active = Column(Boolean, nullable=False, default=True)
    brand_id = Column(Integer, primary_key=True, autoincrement=True)
    supplier_id = Column(Integer, nullable=False) # FK with general/master service and connect using API/RabbitMQ (event-driven SAGA Pattern)
    warehouse_id = Column(Integer, nullable=False) # FK with aftersales service and connect using API/RabbitMQ (event-driven SAGA Pattern)
    brand_code = Column(String(10), nullable=False, unique=True)
    brand_name = Column(String(50), nullable=False, default="")
    brand_abbreviation = Column(String(3), nullable=False)
    brand_must_withdrawal = Column(Boolean, nullable=False, default=False)
    brand_must_pdi = Column(Boolean, nullable=False, default=False)
    atpm_unit = Column(Boolean, nullable=False, default=False)
    atpm_workshop = Column(Boolean, nullable=False, default=False)
    atpm_sparepart = Column(Boolean, nullable=False, default=False)
    atpm_finance = Column(Boolean, nullable=False, default=False)