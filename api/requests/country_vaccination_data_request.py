from utils import auto_str


@auto_str
class CountryVaccinationDataRequest:
    def __init__(self, location, date,
                 vaccine, source_url,
                 total_vaccinations, people_vaccinated,
                 people_fully_vaccinated):
        self.location = location
        self.date = date
        self.vaccine = vaccine
        self.source_url = source_url
        self.total_vaccinations = total_vaccinations
        self.people_vaccinated = people_vaccinated
        self.people_fully_vaccinated = people_fully_vaccinated
