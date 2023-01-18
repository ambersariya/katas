import datetime


class SystemClock:
    def __call__(self):
        return datetime.datetime.now()
