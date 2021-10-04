import { mock, when } from "ts-mockito";
import Account from "../../src/Account";
import Clock from "../../src/Clock";
import Console from "../../src/Console";
import StatementPrinter from "../../src/StatementPrinter";
import TransactionRepository from "../../src/TransactionRepository";

// jest.spyOn(console, "log").mockImplementation();

describe("Feature: statement printer", () => {
    let account: Account;
    let transactionRepository: TransactionRepository;
    let statementPrinter: StatementPrinter;
    let clock: Clock;
    let systemConsole: Console;

    beforeAll(() => {
        jest.spyOn(console, "log").mockImplementation();
        const mockDate1 = new Date("2021-09-01T00:00:00Z");
        const mockDate2 = new Date("2021-09-15T00:00:00Z");
        const mockDate3 = new Date("2021-09-30T00:00:00Z");

        const spy = jest
            .spyOn(global, "Date")
            .mockImplementation()
            // @ts-ignore
            .mockReturnValueOnce(mockDate1)
            // @ts-ignore
            .mockReturnValueOnce(mockDate2)
            // @ts-ignore
            .mockReturnValueOnce(mockDate3);
    });

    beforeEach(() => {
        clock = new Clock();
        transactionRepository = new TransactionRepository(clock);
        systemConsole = new Console();
        statementPrinter = new StatementPrinter(systemConsole);

        account = new Account(transactionRepository, statementPrinter);
    });

    test("print statement containing all transactions", () => {
        account.deposit(1000);
        account.deposit(2000);
        account.withdraw(500);
        account.printStatement();

        expect(console.log).toHaveBeenCalledTimes(4);
        expect(console.log).toBeCalledWith("Date || Amount || Balance");
        expect(console.log).toBeCalledWith("2021/09/30 || -500 || 2500");
        expect(console.log).toBeCalledWith("2021/09/15 || 2000 || 3000");
        expect(console.log).toBeCalledWith("2021/09/01 || 1000 || 1000");
    });
});
