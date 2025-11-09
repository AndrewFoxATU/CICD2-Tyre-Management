from pydantic import BaseModel, constr, conint, condecimal, field_validator
from typing import Literal, Optional
from decimal import Decimal, ROUND_HALF_UP

class TyreBase(BaseModel):
    brand: constr(min_length=1, max_length=50)
    model: constr(min_length=1, max_length=50)
    size: constr(min_length=1, max_length=20)
    load_rate: conint(gt=0)
    speed_rate: Literal[
        "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8",
        "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M",
        "N", "P", "Q", "R", "S", "T", "U", "V", "W", "Y", "ZR"
    ]
    season: Literal["Summer", "Winter", "All Season"]
    supplier: constr(min_length=2, max_length=100)
    fuel_efficiency: Literal["A", "B", "C", "D", "E"]
    noise_level: conint(gt=0)
    weather_efficiency: Literal["A", "B", "C", "D", "E"]
    ev_approved: bool
    cost: condecimal(gt=0)
    quantity: conint(ge=0)
    retail_cost: Optional[condecimal(gt=0)] = None

    @field_validator("retail_cost", mode="before")
    @classmethod
    def calculate_retail_cost(cls, v, values):
        if v is None and "cost" in values:
            return (Decimal(str(values["cost"])) * Decimal("1.35")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        return v

class TyreCreate(TyreBase):
    pass

class Tyre(TyreBase):
    id: int

    class Config:
        orm_mode = True
        json_encoders = {
            Decimal: lambda v: float(v)
        }
