from teams.exceptions import InvalidYearCupError
from teams.exceptions import NegativeTitlesError
from teams.exceptions import ImpossibleTitlesError
from datetime import datetime, timedelta


def data_processing(team_data):
    if team_data.get("titles") < 0:
        raise NegativeTitlesError("titles cannot be negative")

    first_cup_date = team_data.get("first_cup")
    first_cup_date_datetime = datetime.strptime(first_cup_date, "%Y-%m-%d")
    first_cup_date_year = int(first_cup_date_datetime.strftime("%Y"))

    first_cup_ever = int(1930)
    current_time = datetime.now()
    current_year = int(current_time.strftime("%Y"))

    if first_cup_date_year < first_cup_ever or first_cup_date_year > current_year:
        raise InvalidYearCupError("there was no world cup this year")

    titles = int(team_data.get("titles"))

    # Se o intervalo de anos entre a primeira copa de um país e a primeira
    # copa de todas NÃO for múltiplo de 4:
    if (first_cup_date_year - first_cup_ever) % 4 != 0:
        raise InvalidYearCupError("there was no world cup this year")

    if first_cup_date_year + (titles * 4) > current_year:
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")
