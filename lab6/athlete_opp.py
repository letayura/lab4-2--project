import re


class Athlete:
    def __init__(self, first_name: str, last_name: str, phone: str, team_id: int):
        self._first_name = ""
        self._last_name = ""
        self._phone = ""
        self._team_id = 0

        self.set_name(first_name, last_name)
        self.set_phone(phone)
        self.set_team(team_id)

    def set_name(self, first_name: str, last_name: str):
        if not first_name.strip() or not last_name.strip():
            raise ValueError("Імя та прізвище не можуть бути порожніми")
        self._first_name = first_name
        self._last_name = last_name

    def set_phone(self, phone: str):
        if not re.match(r"^\+380\d{9}$", phone):
            raise ValueError(f"неправильний формат телефону: {phone}")
        self._phone = phone

    def set_team(self, team_id: int):
        if team_id <= 0:
            raise ValueError("ID команди має бути додатнім числом")
        self._team_id = team_id

    def to_dict(self):
        return {
            "first_name": self._first_name,
            "last_name": self._last_name,
            "phone": self._phone,
            "team_id": self._team_id,
        }
