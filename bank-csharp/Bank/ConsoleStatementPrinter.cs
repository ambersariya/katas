namespace Bank;

public class ConsoleStatementPrinter : IStatementPrinter
{
    private const string Header = "Date | Amount | Balance";

    public void PrintStatement(List<Transaction> allTransactions)
    {
        List<string> statementLines = [];
        var balanceAtTheTime = 0;

        foreach (var transaction in allTransactions)
        {
            balanceAtTheTime += transaction.Amount;
            statementLines.Add($"{transaction.Date} | {transaction.Amount} | {balanceAtTheTime}");
        }

        statementLines.Reverse();
        statementLines.Insert(0, Header);

        Console.Write(string.Join(Environment.NewLine, statementLines));
    }
}