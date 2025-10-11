from pydantic import BaseModel, constr, condecimal, conint, field_validator
from typing import Literal

class Tyre(BaseModel):
    id: conint(gt=0)
    brand: constr(min_length=1, max_length=50)
    model: constr(min_length=1, max_length=50)
    size: constr(min_length=1, max_length=20)
    season: constr(min_length=3, max_length=20)
    quantity: conint(ge=0)
    supplier: constr(min_length=2, max_length=100)
    fuel_efficiency: Literal["A", "B", "C", "D", "E"]
    noise_level: conint(gt=0)  # dB
    weather_efficiency: Literal["A", "B", "C", "D", "E"]
    cost: condecimal(gt=0)
    retail_cost: condecimal(gt=0)

    # convert input to uppercase before validation
    @field_validator("fuel_efficiency", "weather_efficiency", mode="before")
    @classmethod
    def uppercase_grades(cls, v: str) -> str:
        if isinstance(v, str):
            return v.upper()
        return v
