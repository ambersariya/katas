export default interface AccountServiceInterface {
    deposit(amount: number): void
    withdraw(amount: number): void
    printStatement(): void
}