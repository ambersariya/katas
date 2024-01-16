using System.Collections;

namespace Bank;

public class InMemoryTransactionRepository : ITransactionRepository
{
    private List<Transaction> _transactions = [];

    public void AddTransaction(Transaction transaction)
    {
        _transactions.Add(transaction);
    }

    public List<Transaction> AllTransactions()
    {
        return _transactions;
    }
}