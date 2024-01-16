using System.Collections.Immutable;

namespace Bank.Tests.Unit;

public class InMemoryTransactionRepositoryShould
{
    private Transaction FIRST_TRANSACTION = new Transaction("2021-10-10", 50);
    private Transaction SECOND_TRANSACTION = new Transaction("2022-01-20", 100);

    [Fact]
    public void Add_Transactions()
    {
        var transactionRepository = new InMemoryTransactionRepository();
        var expectedTransactions = ImmutableList.Create(FIRST_TRANSACTION, SECOND_TRANSACTION);

        transactionRepository.AddTransaction(FIRST_TRANSACTION);
        transactionRepository.AddTransaction(SECOND_TRANSACTION);

        Assert.Equal(transactionRepository.AllTransactions(), expectedTransactions);
    }
}