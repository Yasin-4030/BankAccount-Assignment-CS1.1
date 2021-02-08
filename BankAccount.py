class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance = 0):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f'Amount Deposited:  ${amount}')
        print(f'Current balance is:  ${self.balance}')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'Amount Withdrawn:  ${amount}')
            print(f'Current balance is:  ${self.balance}')
        else:
            self.balance = self.balance - 10
            print(f'Insufficient founds!')
            print(f'You have been charged $10 for this attempt, your balance is ${self.balance} now.')

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
        print(user1.__dict__)


user1 = BankAccount('Joi Anderson', 9438754975, 4565659880, 8000)
# user1.withdraw(300)
# user1.get_balance()
# user1.add_interest()
user1.ATM_withdraw(200)
user1.print_reciept()