#
# !Section 14: Python Object Oriented Programming : 
# the second project in oop lesson :
#1. exersice 1: 
class Item():
    num_of_items = 0
    all_items = []
    def __init__(self, name_item, price, quantity):
        self.name = name_item
        self.price = price
        self.quantity = quantity
        Item.num_of_items += 1
        Item.all_items.append(self)
    def __str__(self):
        Total = self.price * self.quantity
        return f'Name: {self.name}\nPrice: ${self.price}\nQuantity: {self.quantity}\nTotal: ${Total}'
    
    def __repr__(self):
        return f'Item({self.name}, {self.price}, {self.quantity})'


# Create an item
item1 = Item("Atomic Habits", 10, 2)
item2 = Item("Deep Work", 20, 1)
item3 = Item("So Good They Can't Ignore You", 15, 3) 
item4 = Item("Digital Minimalism", 12, 2)
# Display the number of items
print(f"Number of items: {Item.num_of_items}") 
# result:
# Number of items: 4

# Display all items
print(Item.all_items)
# result:
# [Item('Atomic Habits', 10, 2), Item('Deep Work', 20, 1),
# Item('So Good They Can't Ignore You', 15, 3), Item('Digital Minimalism', 12, 2)]
# print each item in all_items

for item in Item.all_items:
    print(item)
    print("##################")
# result:
# Name: Atomic Habits
# Price: $10
# Quantity: 2
# Total Price: $20
# ##################
# Name: Deep Work
# Price: $20
# Quantity: 1
# ...

#1. exersice 2 : 
class BankAccount():
    bank_name = 'Codezilla'
    num_of_accounts = 0
    all_accounts = []
    def __init__(self, id_user, balance_accout):
        self.id = id_user
        self.credit = balance_accout
        BankAccount.num_of_accounts += 1
        BankAccount.all_accounts.append(self)
    def __str__(self):
        return f'Accout Number: {self.id}\nBalance: ${self.credit}'
    def __repr__(self):
        return f'BankAccout({self.id}, {self.credit})'
    
    def display_balance(self):
        print(f'Accout {self.id} balance: {self.credit}')

    def add_money(self, added_amount):
        if added_amount >= 0:
            self.credit += added_amount
            print(f'added {added_amount} into account {self.id}.')
        else:
            print('Invalid amount. added amount must be positive.')
    
    def withdraw(self, withdraw_amount):
        if  self.credit >= withdraw_amount and withdraw_amount >= 0:
            self.credit -=  withdraw_amount
            print(f'Withdraw {withdraw_amount} from account {self.id}')
        else:
            print('Insufficient funds or invalid amount ')


# test and result
print(BankAccount.bank_name)  # Codezilla
account1 = BankAccount("5577", 1000)
account2 = BankAccount("1234", 2000)
print(BankAccount.num_of_accounts)
#2
print(BankAccount.all_accounts)
# [BankAccount('5577', 1000), BankAccount('1234', 2000)]
account1.display_balance()
# Account 5577 balance: 1000
account2.display_balance()
# Account 1234 balance: 2000
account1.add_money(500) # added 500 into account 5577. 
account1.display_balance() # Account 5577 balance: 1500
account2.withdraw(1000) # Withdrew 1000 from account 1234. 
account2.display_balance() # Account 1234 balance: 1000
account1.withdraw(2000) # Insufficient funds or invalid amount.
account1.withdraw(-1000) # Insufficient funds or invalid amount.
print(account1)
# Account Number: 5577
# Balance: $1500
print(account2)
# Account Number: 1234
# Balance: $1000