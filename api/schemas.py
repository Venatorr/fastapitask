from datetime import date
from pydantic import BaseModel


class SmartphoneBase(BaseModel):
    brand: str
    model: str
    specs: str
    release_date: date


class SmartphoneCreate(SmartphoneBase):
    pass


class Smartphone(SmartphoneBase):
    id: int

    class Config:
        orm_mode = True
