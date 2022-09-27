from datetime import datetime


class DrivingLicenceGenerator:
    def format_surname(self, surname: str) -> str:
        return surname.upper()[:5].ljust(5, '9')

    def format_year(self, dob: str) -> str:
        return datetime \
            .strptime(dob, '%m-%b-%Y') \
            .strftime('%y')[0]

    def format_month_of_birth(self, dob: str, gender: str) -> str:
        month_of_birth = datetime.strptime(dob, '%m-%b-%Y')
        formatted_month = month_of_birth.strftime('%m')
        match gender:
            case 'F':
                month_prefix = '5' if month_of_birth.month < 10 else 6
                return f"{month_prefix}{formatted_month[1]}"
            case _:
                return formatted_month
