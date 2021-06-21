from utils import auto_str


@auto_str
class Covid19APICountryRequest:
    def __init__(self, country, slug, ISO2):
        self.country = country
        self.slug = slug
        self.ISO2 = ISO2
