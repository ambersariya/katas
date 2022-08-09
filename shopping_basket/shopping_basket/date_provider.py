from datetime import datetime


class DateProvider:
    def current_date(self):
        now = datetime.now()

        return now.strftime("%d/%m/%Y")
