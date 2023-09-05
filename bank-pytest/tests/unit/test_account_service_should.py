def test_add_deposit(account_service, mocked_transaction_repository) -> None:
    account_service.deposit(100)
    mocked_transaction_repository.add_transaction.assert_called_once()


def test_withdraw(account_service, mocked_transaction_repository) -> None:
    account_service.withdraw(100)
    mocked_transaction_repository.add_transaction.assert_called_once()


def test_print_statement(account_service, mocked_statement_printer) -> None:
    account_service.print_statement()
    mocked_statement_printer.print.assert_called_once()
