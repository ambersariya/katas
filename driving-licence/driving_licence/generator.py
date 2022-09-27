class DrivingLicenceGenerator:
    def generate(self, data: list) -> str:
        _, _, surname, _, _ = data
        return surname.upper()[:5].ljust(5, '9')
