from .exceptions import ImpossibleTitlesError
from .exceptions import InvalidYearCupError
from .exceptions import NegativeTitlesError
from datetime import datetime, timedelta


def data_processing(team_data):
    if team_data.get("titles") < 0:
        raise NegativeTitlesError("titles cannot be negative")

    first_cup_date = team_data.get("first_cup")

    first_cup_ever = 1930
    current_time = datetime.now()
    current_year = current_time.strftime("%Y")

    for year in range(first_cup_ever, int(current_year) + 1):
        first_cup_ever += 4
        print(first_cup_ever)

        if first_cup_ever != first_cup_date:
            raise InvalidYearCupError("there was no world cup this year")

    # raise ImpossibleTitlesError("impossible to have more titles than disputed cups")
