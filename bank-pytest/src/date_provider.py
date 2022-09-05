import datetime

from src.constants import TRANSACTION_DATE_FORMAT


class DateProvider:
    @staticmethod
    def today() -> str:
        return datetime.datetime.now().strftime(TRANSACTION_DATE_FORMAT)  # pragma: no cover
