# backend/tyres_service/models.py
from sqlalchemy import Column, Integer, String, Boolean, Numeric
from database import Base

class TyreModel(Base):
    __tablename__ = "tyres"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    size = Column(String, nullable=False)
    load_rate = Column(Integer, nullable=False)
    speed_rate = Column(String, nullable=False)
    season = Column(String, nullable=False)
    supplier = Column(String, nullable=False)
    fuel_efficiency = Column(String, nullable=False)
    noise_level = Column(Integer, nullable=False)
    weather_efficiency = Column(String, nullable=False)
    ev_approved = Column(Boolean, nullable=False)
    cost = Column(Numeric(10,2), nullable=False)
    quantity = Column(Integer, nullable=False)
    retail_cost = Column(Numeric(10,2), nullable=False)
