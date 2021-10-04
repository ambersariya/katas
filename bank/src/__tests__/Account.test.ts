import { TransactionType } from "..//TransactionType";
import { anything, instance, mock, resetCalls, verify, when } from "ts-mockito";
import Account from "../Account";
import StatementPrinter from "../StatementPrinter";
import Transaction from "../Transaction";
import TransactionRepository from "../TransactionRepository";

describe("Add transactions to account", () => {
    let account: Account;
    let mockedTransactionRepository = mock(TransactionRepository);
    let mockedStatementPrinter = mock(StatementPrinter);
    let transactionRepository: TransactionRepository = instance(
        mockedTransactionRepository
    );
    let statementPrinter: StatementPrinter = instance(mockedStatementPrinter);

    beforeAll(() => {
        resetCalls(mockedTransactionRepository);
        resetCalls(mockedStatementPrinter);
        account = new Account(transactionRepository, statementPrinter);
    });

    test("should store a deposit transaction", () => {
        account.deposit(1000);
        verify(mockedTransactionRepository.addDeposit(1000)).once();
    });

    test("should store a withdrawl transaction", () => {
        account.withdraw(100);
        verify(mockedTransactionRepository.addWithdrawal(100)).once();
    });

    test("should print a statement", () => {
        when(mockedTransactionRepository.allTransactions()).thenReturn([
            new Transaction(TransactionType.Deposit, 1000, new Date().toISOString()),
            new Transaction(TransactionType.Withdraw, 100, new Date().toISOString()),
        ]);

        account.printStatement();

        verify(mockedStatementPrinter.print(anything())).once();
    });
});
