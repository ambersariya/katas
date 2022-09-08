import Console from "./Console";
import Transaction from "./Transaction";

export default class StatementPrinter {
    private HEADER = `Date || Amount || Balance`;
    constructor(private console: Console) {}
    print(transactions: Array<Transaction>): void {
        this.console.printLine(this.HEADER);
        let runningBalance = 0;
        let statementLines = transactions.map((transaction) => {
            runningBalance += transaction.getAmount();
            return this.statementLine(transaction, runningBalance);
        });

        statementLines.reverse().forEach((element) => {
            // @ts-ignore
            this.console.printLine(element);
        });
    }

    protected statementLine(
        transaction: Transaction,
        runningBalance: number
    ): string {
        return `${transaction.getDate()} || ${transaction.getAmount()} || ${runningBalance}`;
    }
}
