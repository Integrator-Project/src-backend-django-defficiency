from utils import auto_str


@auto_str
class CountryDataRequest:
    def __init__(self, name, top_level_domain,
                 alpha2_code, alpha3_code, calling_codes,
                 capital, alt_spellings, region,
                 subregion, population, latlng,
                 demonym, area, gini, timezones,
                 borders, native_name, numeric_code,
                 currencies, languages, translations,
                 flag, regional_blocs, cioc):
        self.name = name
        self.top_level_domain = top_level_domain
        self.alpha2_code = alpha2_code
        self.alpha3_code = alpha3_code
        self.calling_codes = calling_codes
        self.capital = capital
        self.alt_spellings = alt_spellings
        self.region = region
        self.subregion = subregion
        self.population = population
        self.latlng = latlng
        self.demonym = demonym
        self.area = area
        self.gini = gini
        self.timezones = timezones
        self.borders = borders
        self.native_name = native_name
        self.numeric_code = numeric_code
        self.currencies = currencies
        self.languages = languages
        self.translations = translations
        self.flag = flag
        self.regional_blocs = regional_blocs
        self.cioc = cioc
