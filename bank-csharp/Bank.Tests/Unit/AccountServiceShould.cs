using Moq;

namespace Bank.Tests.Unit;

public class AccountServiceShould
{
    private readonly Mock<ITransactionRepository> _mockTransactionRepository;
    private readonly Mock<DateTimeGenerator> _mockedDatetimeProvider;
    private readonly Mock<IStatementPrinter> _mockStatementPrinter;
    private readonly AccountService _accountService;

    public AccountServiceShould()
    {
        _mockTransactionRepository = new Mock<ITransactionRepository>();
        _mockedDatetimeProvider = new Mock<DateTimeGenerator>(MockBehavior.Strict);
        _mockStatementPrinter = new Mock<IStatementPrinter>();
        _accountService = new AccountService(_mockTransactionRepository.Object, _mockedDatetimeProvider.Object,
            _mockStatementPrinter.Object);
    }

    [Fact]
    public void Add_Deposit()
    {
        _mockedDatetimeProvider.Setup(m => m.Today()).Returns("2023-10-21");

        _accountService.Deposit(100);

        _mockTransactionRepository.Verify(
            repository => repository.AddTransaction(It.IsAny<Transaction>()),
            Times.Once
        );
    }

    [Fact]
    public void Withdraw_Amount()
    {
        _mockedDatetimeProvider.Setup(m => m.Today()).Returns("2023-10-21");

        _accountService.Withdraw(15);

        _mockTransactionRepository.Verify(
            repository => repository.AddTransaction(It.IsAny<Transaction>()),
            Times.Once
        );
    }

    [Fact]
    public void Print_Statement()
    {
        _accountService.PrintStatement();

        _mockStatementPrinter.Verify(printer => printer.PrintStatement(It.IsAny<List<Transaction>>()));
    }
}