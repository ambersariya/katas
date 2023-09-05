import AccountServiceInterface from "./AccountServiceInterface";
import StatementPrinter from "./StatementPrinter";
import TransactionRepository from "./TransactionRepository";

export default class Account implements AccountServiceInterface {
    constructor(
        private transactionRepository: TransactionRepository,
        private statementPrinter: StatementPrinter
    ) {}

    deposit(amount: number): void {
        this.transactionRepository.addDeposit(amount);
    }

    withdraw(amount: number): void {
        this.transactionRepository.addWithdrawal(amount);
    }

    printStatement(): void {
        this.statementPrinter.print(
            this.transactionRepository.allTransactions()
        );
    }
}
