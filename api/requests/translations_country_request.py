from utils import auto_str


@auto_str
class TranslationsCountryRequest:
    def __init__(self, country, de, es, fr, ja, it, br, pt, nl, hr, fa):
        self.country = country
        self.de = de
        self.es = es
        self.fr = fr
        self.ja = ja
        self.it = it
        self.br = br
        self.pt = pt
        self.nl = nl
        self.hr = hr
        self.fa = fa
