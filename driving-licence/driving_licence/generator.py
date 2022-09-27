from datetime import datetime

DOB_FORMAT = '%d-%b-%Y'


class DrivingLicenceGenerator:
    def format_surname(self, surname: str) -> str:
        return surname.upper()[:5].ljust(5, '9')

    def format_decade(self, dob: str) -> str:
        return dob[-2:-1]

    def format_month_of_birth(self, dob: str, gender: str) -> str:
        month_of_birth = datetime.strptime(dob, DOB_FORMAT)
        formatted_month = month_of_birth.strftime('%m')
        match gender:
            case 'F':
                month_prefix = '5' if month_of_birth.month < 10 else 6
                return f"{month_prefix}{formatted_month[1]}"
            case _:
                return formatted_month

    def format_date_within_month(self, dob: str) -> str:
        return dob[0:2]

    def format_year(self, dob: str) -> str:
        return dob[-1:]

    def format_initials(self, firstname, middlename: str):
        middlename = middlename[0:2].ljust(2, '9')
        return f"{firstname[0:2]}{middlename}".upper()
