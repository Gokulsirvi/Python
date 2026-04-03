# Bank, Customer, Account classes

class Customer:
    def __init__(self, name):
        self.name = name

class Account:
    def __init__(self, customer, balance=0):
        self.customer = customer
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Balance:", self.balance)

class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, customer):
        acc = Account(customer)
        self.accounts.append(acc)
        return acc

# Example usage
c1 = Customer("Gokul")
bank = Bank()
acc1 = bank.create_account(c1)

acc1.deposit(1000)
acc1.withdraw(500)
acc1.show_balance()
