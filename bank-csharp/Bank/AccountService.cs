namespace Bank;

public class AccountService(
    ITransactionRepository transactionRepository,
    DateTimeGenerator datetimeGenerator,
    IStatementPrinter statementPrinter)
{
    public void Deposit(int amount)
    {
        transactionRepository.AddTransaction(new Transaction(datetimeGenerator.Today(), amount));
    }

    public void Withdraw(int amount)
    {
        transactionRepository.AddTransaction(new Transaction(datetimeGenerator.Today(), -amount));
    }

    public void PrintStatement()
    {
        statementPrinter.PrintStatement(transactionRepository.AllTransactions());
    }
}