#
# !Section 14: Python Object Oriented Programming : 
# the first project in oop lesson :
#1. exersice 1: Fix the information Class
class information():
    def __init__(self, name, age, job_title):
        self.name = name
        self.age = age
        self.job = job_title

    def stupid(self):
        print(f'{self.name} is stupid')

# make an instance of the class information
create_object = information("Hamada", 25,"creator")

# print the attributes of the instance
print(create_object.name) #output : Hamada
print(create_object.age) #output : 25
print(create_object.job) #output : creater

# call the method stupid() of the instance
create_object.stupid()  #output : 

# add an attribute to the instance create_object
create_object.phonenumber = '0123456789'
# print the attribute phonenumber of the instance
print(create_object.phonenumber) #output:  0123456789

# Edit the attribute age of the instance create_object
create_object.age = 35
# print the attribute age of the instance
print(create_object.age)  #output  : 35
#----------------------------------------------------------------------
#1. exersice 2:
class Item():
    def __init__(self, name_book, price, quantity):
        self.name = name_book
        self.price = price
        self.quantity = quantity
    
    def display(self):
        total = self.price * self.quantity
        print(f'Name: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}\nTotal Price: ${total}')
    

item1 = Item("Atomic Habits", 10, 2) 
item2 = Item("Deep Work", 20, 1)
# Display item information
item1.display()
item2.display()
# Output : 
# # Result item1:
# Name: Atomic Habits
# Price: $10
# Quantity: 2
# Total Price: $20
#-----------------
# # Result item2:
# Name: Deep Work
# Price: $20
# Quantity: 1
# Total Price: $20
#----------------------------------------------------------------------
#1. exersice 3: 
class BankAccount():
    def __init__(self, id_accout, balance_accout):
        self.id = id_accout
        self.credit = balance_accout
    
    def display_balance(self):
        print(f'Accout {self.id} balance: {self.credit}')
    
    def add_money(self, added_amount):
        if added_amount >= 0:
            self.credit += added_amount
            print(f'added {added_amount} into account {self.id}.')
        else:
            print('Invalid amount. added amount must be positive.')
    def withdraw(self, withdraw_amount):
        if  self.credit >= withdraw_amount:
            reverse_withdraw = abs(withdraw_amount)
            self.credit -=  reverse_withdraw
            print(f'Withdrew {reverse_withdraw} from account {self.id}')
        else:
            print('Insufficient funds or invalid amount ')


account1 = BankAccount("5577", 1000)
account1.display_balance() # Account 5577 balance: 1000 
account1.add_money(500) # added 500 into account 5577.
account1.display_balance() # Account 5577 balance: 1500 
account1.add_money(-100)# Invalid amount. added amount must be positive.
account1.display_balance() # Account 5577 balance: 1500
account1.withdraw(200) # Withdrew 200 from account 5577. 
account1.display_balance() # Account 5577 balance: 1300
account1.withdraw(1500) # Insufficient funds or invalid amount.
account1.display_balance() # Account 5577 balance: 1300
