import { TransactionType } from "./TransactionType";

export default class Transaction {
    getAmount() {
        return this.amount;
    }
    getDate() {
        return this.date;
    }
    getType() {
        return this.type;
    }
    constructor(
        private type: TransactionType,
        private amount: number,
        private date: string
    ) {}
}
