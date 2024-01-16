namespace Bank.Tests.Unit;

public class ConsoleStatementPrinterShould
{
    [Fact]
    public void Print_Header_Only_When_There_Are_No_Transactions()
    {
        var expectedStatement = "Date | Amount | Balance";

        VerifyStatementWithTransactions([], expectedStatement);
    }

    [Fact]
    public void Prints_Transactions_In_Reverse_Order()
    {
        var expectedStatement = """
                                Date | Amount | Balance
                                2022-10-31 | 200 | 300
                                2022-10-28 | 100 | 100
                                """;

        VerifyStatementWithTransactions(
            [new Transaction("2022-10-28", 100), new Transaction("2022-10-31", 200)],
            expectedStatement
        );
    }

    private static void VerifyStatementWithTransactions(List<Transaction> transactions, string expectedStatement)
    {
        var originalConsoleOut = Console.Out;
        var consoleStatementPrinter = new ConsoleStatementPrinter();
        try
        {
            // Create a StringWriter to capture the output
            using var stringWriter = new StringWriter();
            // Redirect Console.Out to the StringWriter
            Console.SetOut(stringWriter);

            // Your code that uses Console.Write()
            consoleStatementPrinter.PrintStatement(transactions);

            // Get the captured output from the StringWriter
            var capturedOutput = stringWriter.ToString();

            // Assert the captured output
            Assert.Equal(expectedStatement, capturedOutput);
        }
        finally
        {
            // Restore the original Console.Out
            Console.SetOut(originalConsoleOut);
        }
    }
}