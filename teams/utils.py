from .exceptions import ImpossibleTitlesError
from .exceptions import InvalidYearCupError
from .exceptions import NegativeTitlesError


def data_processing(team_data):
    if team_data.get("titles") < 0:
        raise NegativeTitlesError("titles cannot be negative")

    first_cup_date = team_data.get("first_cup")
