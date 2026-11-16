import pytest
from athlete_opp import Athlete


def test_athlete_creation_success():
    athlete = Athlete("Юрій", "Лета", "+380501234567", 1)
    assert athlete._first_name == "Юрій"


def test_athlete_invalid_phone():
    with pytest.raises(ValueError):
        Athlete("Юрій", "Лета", "12345", 1)


def test_athlete_invalid_team_id():
    with pytest.raises(ValueError):
        Athlete("Юрій", "Лета", "+380501234567", -5)


def test_athlete_empty_name():
    with pytest.raises(ValueError):
        Athlete("   ", "Лета", "+380501234567", 1)
