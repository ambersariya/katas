import { instance, mock, verify } from "ts-mockito";
import Console from "../Console";
import StatementPrinter from "../StatementPrinter";
import Transaction from "../Transaction";
import { TransactionType } from "../TransactionType";

describe("statement printer tests", () => {
    let console: Console;
    let mockConsole: Console;
    let statementPrinter: StatementPrinter;

    beforeAll(() => {
        mockConsole = mock(Console);
        console = instance(mockConsole);
        statementPrinter = new StatementPrinter(console);
    });

    test("always prints header", () => {
        let transactions: Transaction[] = [];
        statementPrinter.print(transactions);
        verify(mockConsole.printLine("Date || Amount || Balance")).once();
    });

    test("always prints in reverse chronological order", () => {
        let transactions: Transaction[] = [
            deposit("2021/09/30", 100),
            withdraw("2021/09/30", 10)
        ];
        statementPrinter.print(transactions);
        verify(mockConsole.printLine("Date || Amount || Balance")).called();
        verify(mockConsole.printLine("2021/09/30 || -10 || 90")).called();
        verify(mockConsole.printLine("2021/09/30 || 100 || 100")).called();
    });
});

function deposit(date: string, amount: number): Transaction {
    return new Transaction(TransactionType.Deposit, amount, date);
}

function withdraw(date: string, amount: number): Transaction {
    return new Transaction(TransactionType.Withdraw, -amount, date);
}
