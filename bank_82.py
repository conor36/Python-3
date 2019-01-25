class BankAccount(object):
 
    next_account_number = 16555232
    total_lodgements = 0
    interest_rate = 0.043
 
    def __init__(self, forename, surname, balance=0, num=16555232):
       self.forename = forename
       self.surname = surname
       self.balance = balance
       self.num = BankAccount.next_account_number
       BankAccount.next_account_number += 1
 
    def lodge(self, amount):
       self.balance = self.balance + amount
       BankAccount.total_lodgements += 1
 
    def apply_interest(self, amount=0.043):
       self.balance = self.balance * (1 + amount)
       BankAccount.total_lodgements += 1
 
    def __iadd__(self, amount):
       z = self.balance + amount
       self.balance = z
       return self
 
    def __str__(self):
      return 'Name: {}\nAccount number: {}\nBalance: {:.2f}'.format(self.forename + ' ' + self.surname, self.num, self.balance)