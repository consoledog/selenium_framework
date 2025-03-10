class Placeorder:
    def __init__(self, name: str, country: str, city: str, credit_card: str, month: str, year: str):
        self._name = name
        self._country = country
        self._city = city
        self._credit_card = credit_card
        self._month = month
        self._year = year
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def credit_card(self):
        return self._credit_card

    @credit_card.setter
    def credit_card(self, value):
        self._credit_card = value

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        self._month = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value