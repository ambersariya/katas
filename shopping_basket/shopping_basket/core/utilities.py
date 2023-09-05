import uuid


class IdGenerator:
    @staticmethod
    def next() -> str:
        return str(uuid.uuid4())
