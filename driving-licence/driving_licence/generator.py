import datetime


class DrivingLicenceGenerator:
    def format_surname(self, surname: str) -> str:
        return surname.upper()[:5].ljust(5, '9')

    def format_year(self, dob: str) -> str:
        return datetime.datetime \
            .strptime(dob, '%m-%d-%Y') \
            .strftime('%y')[0]
