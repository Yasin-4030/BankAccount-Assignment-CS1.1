import random

class BankAccount:
    def __init__(self, full_name, balance = 0):
        self.full_name = full_name
        self.account_number = random.randint(10000000, 99999999)
        self.routing_number = random.randint(10000000, 99999999)
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f'Amount Deposited:  ${amount}')
        print(f'Current balance is:  ${self.balance}')

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'Amount Withdrawn:  ${amount}')
            print(f'Current balance is:  ${self.balance}')
        else:
            self.balance -= amount + 10
            print(f'Insufficient founds!')
            print(f'You have been charged $10 for this transaction, your balance is ${self.balance} now.')

    def get_balance(self):
        print(f'Hi {self.full_name}! Your current balance is:  ${self.balance}')

    def add_interest(self):
        monthly_interest = self.balance * 0.00083
        print(f'Monthly interest on your account is ${monthly_interest}, your current balance is: ${self.balance + monthly_interest}')

    def ATM_withdraw(self, amount):
        self.balance = self.balance - amount - 2
        print(f'Amount Withdrawn: ${amount}')
        print(f'You were charged $2 for using this ATM, your current balance is: ${self.balance}')

    def print_reciept(self):
        for key in self.__dict__:
            # print(f"{key}")
	        print(f"{key}: {self.__dict__[key]}")
            
user1 = BankAccount('Jay Lowe', 1800)
# user1.deposit(100)
# user1.withdraw(850) 
# user1.get_balance()
# user1.add_interest()
# user1.ATM_withdraw(200)
# user1.print_reciept()
