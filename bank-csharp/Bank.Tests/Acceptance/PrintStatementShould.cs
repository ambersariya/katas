using Moq;

namespace Bank.Tests.Acceptance;

public class PrintStatementShould
{
    [Fact]
    public void print_transactions()
    {
        var expectedStatement = """
                                Date | Amount | Balance
                                2012-01-14 | -500 | 2500
                                2012-01-13 | 2000 | 3000
                                2012-01-10 | 1000 | 1000
                                """;
        var transactionRepository = new InMemoryTransactionRepository();
        var mockedDatetimeProvider = new Mock<DateTimeGenerator>(MockBehavior.Strict);
        mockedDatetimeProvider.SetupSequence(m => m.Today())
            .Returns("2012-01-10")
            .Returns("2012-01-13")
            .Returns("2012-01-14")
            ;

        var statementPrinter = new ConsoleStatementPrinter();
        var accountService = new AccountService(
            transactionRepository: transactionRepository,
            datetimeGenerator: mockedDatetimeProvider.Object,
            statementPrinter: statementPrinter
        );


        accountService.Deposit(1000);
        accountService.Deposit(2000);
        accountService.Withdraw(500);
        VerifyPrintedStatement(accountService, expectedStatement);
    }

    private static void VerifyPrintedStatement(AccountService accountService, string expectedStatement)
    {
        var originalConsoleOut = Console.Out;
        try
        {
            // Create a StringWriter to capture the output
            using var stringWriter = new StringWriter();
            // Redirect Console.Out to the StringWriter
            Console.SetOut(stringWriter);

            // Your code that uses Console.WriteLine()
            accountService.PrintStatement();

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