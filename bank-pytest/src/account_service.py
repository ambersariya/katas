class AccountService:
    def deposit(self, amount: int) -> None:
        raise NotImplementedError()

    def withdraw(self, amount: int) -> None:
        raise NotImplementedError()

    def print_statement(self) -> None:
        raise NotImplementedError()
