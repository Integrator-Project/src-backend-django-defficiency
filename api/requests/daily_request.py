from utils import auto_str


@auto_str
class DailyRequest:
    def __init__(self, date_field, total, country):
        self.date_field = date_field
        self.total = total
        self.country = country
