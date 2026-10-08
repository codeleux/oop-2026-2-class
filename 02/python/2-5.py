from enum import Enum

class AccountType(Enum):
    savings = "Ahorros"
    checking = "Corriente"

class BankAccount:
    def __init__(
        self,
        firstName: str,
        lastName: str,
        accountNumber: str,
        accountType: AccountType,
    ):
        self.firstName = firstName
        self.lastName = lastName
        self.accountNumber = accountNumber
        self.accountType = accountType
        self.balance = 0.0

    def getFirstName(self):
        return self.firstName

    def setFirstName(self, firstName: str):
        self.firstName = firstName

    def getLastName(self):
        return self.lastName

    def setLastName(self, lastName: str):
        self.lastName = lastName

    def getAccountNumber(self):
        return self.accountNumber

    def setAccountNumber(self, accountNumber: str):
        self.accountNumber = accountNumber

    def getAccountType(self):
        return self.accountType

    def setAccountType(self, accountType: AccountType):
        self.accountType = accountType

    def getBalance(self):
        return self.balance

    def deposit(self, amount: float):
        if amount <= 0:
            print('El valor a consignar debe ser mayor a cero.')
        else:
            self.balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            print('El valor a retirar debe ser mayor a cero.')
        elif amount > self.balance:
            print('Fondos insuficientes. No se puede realizar el retiro.')
        else:
            self.balance -= amount

    def showInfo(self):
        print(f'Nombres del titular: {self.firstName}')
        print(f'Apellidos del titular: {self.lastName}')
        print(f'Número de cuenta: {self.accountNumber}')
        print(f'Tipo de cuenta: {self.accountType.value}')
        print(f'Saldo actual: ${self.balance:.2f}\n')

def main():
    account = BankAccount(
        firstName='Carlos',
        lastName='Gómez',
        accountNumber='1234567890',
        accountType=AccountType.savings,
    )

    account.showInfo()

    account.deposit(500000)
    print(f'Saldo tras consignar $500,000: ${account.getBalance():.2f}')

    account.withdraw(150000)
    print(f'Saldo tras retirar $150,000: ${account.getBalance():.2f}')

    account.withdraw(400000)
    print(f'Saldo tras intentar retirar $400,000: ${account.getBalance():.2f}')

main()