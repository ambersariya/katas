namespace Bank;

public interface IStatementPrinter
{
    public void PrintStatement(List<Transaction> allTransactions);
}