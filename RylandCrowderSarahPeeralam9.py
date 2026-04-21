from accounts import *


def get_bank_total(accounts):
    total = 0
    for account in accounts:
        total += account.get_balance()
    return total

def main():
    a1 = Account('John')
    print(a1)                    # Account name = John, Account balance = 0.00
    a1.deposit(-20.50)
    a1.deposit(0)
    a1.deposit(50)
    a1.withdraw(10.5)
    print(a1)                   # Account name = John, Account balance = 39.50

    a2 = SavingAccount('Jane')
    print(a2)                   # SAVING ACCOUNT: Account name = Jane, Account balance = 100.00
    a2.deposit(-20.50)
    a2.deposit(0)
    a2.deposit(50)
    a2.withdraw(10)
    print(a2)                   # SAVING ACCOUNT: Account name = Jane, Account balance = 140.00
    a2.deposit(50)
    a2.deposit(10.5)
    a2.deposit(5)
    a2.deposit(100)
    print(a2)                   # SAVING ACCOUNT: Account name = Jane, Account balance = 311.61
    a2.withdraw(212)
    print(a2)                   # SAVING ACCOUNT: Account name = Jane, Account balance = 311.61
    a2.withdraw(211.61)
    print(a2)                   # SAVING ACCOUNT: Account name = Jane, Account balance = 100.00

    accounts = [a1, a2]
    a3 = Account('Rekha')
    a3.deposit(135.32)
    accounts.append(a3)
    a4 = Account('Julio')
    a4.deposit(98.76)
    accounts.append(a4)
    a5 = SavingAccount('Yasmin')
    a5.deposit(200.00)
    accounts.append(a5)
    a6 = SavingAccount('Tao')
    a6.deposit(178.64)
    accounts.append(a6)
    print(f'Total at the bank is ${get_bank_total(accounts):.2f}') # Total at the bank is $952.22


if __name__ == '__main__':
    main()
    