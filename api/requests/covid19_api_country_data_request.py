from utils import auto_str


@auto_str
class Covid19CountryDataRequest:
    def __init__(self, ID, country, country_code,
                 province, city, city_code, lat,
                 lon, confirmed, deaths, recovered,
                 active, date):
        self.ID = ID
        self.country = country
        self.country_code = country_code
        self.province = province
        self.city = city
        self.city_code = city_code
        self.lat = lat
        self.lon = lon
        self.confirmed = confirmed
        self.deaths = deaths
        self.recovered = recovered
        self.active = active
        self.date = date
