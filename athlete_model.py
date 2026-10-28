from pydantic import BaseModel

from phone_number import PhoneNumber


class AthleteBase(BaseModel):
    first_name: str
    last_name: str
    phone: PhoneNumber
    team_id: int
