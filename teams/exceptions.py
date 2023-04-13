class NegativeTitlesError(Exception):
    ...


class InvalidYearCupError(Exception):
    print("there was no world cup this year")


class ImpossibleTitlesError(Exception):
    print("impossible to have more titles than disputed cups")
