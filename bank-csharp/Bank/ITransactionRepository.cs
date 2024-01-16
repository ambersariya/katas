namespace Bank;

public interface ITransactionRepository
{
    void AddTransaction(Transaction transaction);
    List<Transaction> AllTransactions();
}