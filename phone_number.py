from pydantic import BaseModel, Field


class PhoneNumber(BaseModel):
    value: str = Field(pattern=r"^\+380\d{9}$", description="Формат: +380XXXXXXXXX")


class AthleteBase(BaseModel):
    first_name: str
    last_name: str
    phone: str = Field(pattern=r"^\+380\d{9}$", description="Формат: +380XXXXXXXXX")
    team_id: int
