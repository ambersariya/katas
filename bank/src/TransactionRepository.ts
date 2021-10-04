import Clock from "./Clock";
import Transaction from "./Transaction";
import { TransactionType } from "./TransactionType";

export default class TransactionRepository {
    private transactions: Transaction[];
    constructor(private clock: Clock) {
        this.transactions = [];
    }

    allTransactions(): any {
        return this.transactions;
    }

    addDeposit(amount: number): void {
        let deposit = new Transaction(
            TransactionType.Deposit,
            amount,
            this.clock.todayAsString()
        );
        this.transactions.push(deposit);
    }

    addWithdrawal(amount: number): void {
        let widthdraw = new Transaction(
            TransactionType.Withdraw,
            -amount,
            this.clock.todayAsString()
        );
        this.transactions.push(widthdraw);
    }
}
