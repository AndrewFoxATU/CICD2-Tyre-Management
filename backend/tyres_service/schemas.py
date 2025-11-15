# backend/tyres_service/schemas.py
from pydantic import BaseModel, StringConstraints
from typing import Annotated, Literal, Optional
from decimal import Decimal
from annotated_types import Ge, Gt

class TyreSchema(BaseModel):
    brand: Annotated[str, StringConstraints(min_length=1, max_length=50)]
    model: Annotated[str, StringConstraints(min_length=1, max_length=50)]
    size: Annotated[str, StringConstraints(min_length=1, max_length=20)]
    load_rate: Annotated[int, Gt(0)]
    speed_rate: Literal[
        "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8",
        "B", "C", "D", "E", "F", "G", "H", "J", "K", "L",
        "M", "N", "P", "Q", "R", "S", "T", "U", "V", "W", "Y", "ZR"
    ]
    season: Literal["Summer", "Winter", "All Season"]
    supplier: Annotated[str, StringConstraints(min_length=2, max_length=100)]
    fuel_efficiency: Literal["A", "B", "C", "D", "E"]
    noise_level: Annotated[int, Gt(0)]
    weather_efficiency: Literal["A", "B", "C", "D", "E"]
    ev_approved: bool
    cost: Annotated[Decimal, Gt(0)]
    quantity: Annotated[int, Ge(0)]
    retail_cost: Optional[Decimal] = None


class TyreCreate(TyreSchema):
    pass

class TyreUpdate(BaseModel):
    brand: Optional[str] = None
    model: Optional[str] = None
    size: Optional[str] = None
    load_rate: Optional[int] = None
    speed_rate: Optional[str] = None
    season: Optional[str] = None
    supplier: Optional[str] = None
    fuel_efficiency: Optional[str] = None
    noise_level: Optional[int] = None
    weather_efficiency: Optional[str] = None
    ev_approved: Optional[bool] = None
    cost: Optional[Decimal] = None
    quantity: Optional[int] = None