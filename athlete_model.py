from pydantic import BaseModel


class AthleteBase(BaseModel):
    first_name: str
    last_name: str
    phone: str
    team_id: int
