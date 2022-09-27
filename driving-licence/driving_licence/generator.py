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

    def format_initials(self, firstname: str, middlename: str):
        middlename = middlename[0] if len(middlename) > 0 else '9'
        return f"{firstname[0]}{middlename}".upper()

    def generate(self, data: list) -> str:
        return f"{self.format_surname(surname=data[2])}" \
               f"{self.format_decade(dob=data[3])}" \
               f"{self.format_month_of_birth(dob=data[3], gender=data[4])}" \
               f"{self.format_date_within_month(dob=data[3])}" \
               f"{self.format_year(dob=data[3])}" \
               f"{self.format_initials(firstname=data[0], middlename=data[1])}" \
               f"9AA"

