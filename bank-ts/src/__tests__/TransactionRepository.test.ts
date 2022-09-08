import Transaction from "../Transaction";
import { instance, mock, when } from "ts-mockito";
import Clock from "../Clock";
import TransactionRepository from "../TransactionRepository";
import { TransactionType } from "../TransactionType";

describe("creates and stores transactions", () => {
    let mockedClock = mock(Clock);
    let clock = instance(mockedClock);
    const TRANSACTION_DATE = "2021/09/30";
    let transactionRepository: TransactionRepository;

    beforeAll(() => {
        when(mockedClock.todayAsString()).thenReturn(TRANSACTION_DATE);
    });

    test("create and store deposit transaction", () => {
        transactionRepository = new TransactionRepository(clock);

        transactionRepository.addDeposit(100);

        let transactions = transactionRepository.allTransactions();
        expect(transactions.length).toBe(1);
        expect(transactions[0]).toBeInstanceOf(Transaction);
        expect(transactions[0].getType()).toBe(TransactionType.Deposit);
        expect(transactions[0].getAmount()).toBe(100);
        expect(transactions[0].getDate()).toBe(TRANSACTION_DATE);
    });

    test("create and store withdraw transaction", () => {
        transactionRepository = new TransactionRepository(clock);

        transactionRepository.addWithdrawal(100);
        let transactions = transactionRepository.allTransactions();
        expect(transactions.length).toBe(1);
        expect(transactions[0]).toBeInstanceOf(Transaction);
        expect(transactions[0].getType()).toBe(TransactionType.Withdraw);
        expect(transactions[0].getAmount()).toBe(-100);
        expect(transactions[0].getDate()).toBe(TRANSACTION_DATE);
    });
});
