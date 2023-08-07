from json import dumps, loads
from random import randint
from datetime import datetime
#! Path data users and books in file json you can change bath :
path_data_books = r'/Users/mohamedbloul/Desktop/codezilla-cours/Section 20/project_library/data-library.json'
path_data_user = r'/Users/mohamedbloul/Desktop/codezilla-cours/Section 20/project_library/data_user.json'
#📛⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️📛⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️📛⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️📛
#! load data from json 
with open(path_data_books, 'r') as db : 
    load_books_from_json = loads(db.read())

with open(path_data_user, 'r') as du : 
    load_user_from_json = loads(du.read())
#?##############################################################################################
#? create class Book : 


class Book():
    #! def init return self value user in class
    name_library = "The British Library"

    def __init__(self, book_name=False, category=False, author=False, year_of_publication=False) :
        self.category = category
        self.name = book_name
        self.author = author
        self.year = year_of_publication
        
    #! def str return informaation library 
    def __str__(self):
        if self.name == "information library":
            count_book = len(load_books_from_json["data_books"])
            count_user = len(load_user_from_json["data_users"])
            return f'__{Book.name_library}__:\ncount book: {count_book} Books\ncount user: {count_user} Users'


    #! function to search book and return details :
    def search(self):
        for book in load_books_from_json["data_books"]:
            if self.name == book["Details"]["Book_Name"]:
                if (book["Status"]["status"] == True):
                    return f'''
        ✅ Available Now :
            - Name Book: {book["Details"]["Book_Name"]}
            - Category Book: {book["Details"]["Category"]}
            - Author: {book["Details"]["Author"]}
            - Year Of Publication: {book["Details"]["Year_of_Publication"]}
            - The Nmber Copies : {book["Status"]["number_available"]}'''
                else:
                    return 'All copies finished 💢'
            
        return 'Not found in library data, Please add this book 🛑'
    #! function to add new details book :
    def add_book(self, number_copies):
        new_book = {
        "Details": {
            "Category": self.category,
            "Book_Name": self.name,
            "Author": self.author,
            "Year_of_Publication": self.year
        },
        "Status": {
            "status": True,
            "number_available": number_copies
        }
        }
        load_books_from_json["data_books"].append(new_book)
        return 'Add successfully ✅'
    
    #! this function for user take book and added to list books : 
    def take_book(self,name_user, id_user):
        for user in load_user_from_json["data_users"]:
            if name_user == user["Name"] and id_user == user["ID"]:
                # only three books are allowed to be borrowed
                if len(user["History_books"]["Taken"]) < 4:
                    for book in load_books_from_json["data_books"]:
                        if self.name == book["Details"]["Book_Name"] and book["Status"]["number_available"] > 0 :
                            user["History_books"]["Taken"].append(self.name)
                            book["Status"]["number_available"] -= 1
                            return "added book to list user successfully ✅ "
                    return "Not found in library, Please check copies or add this book 🛑"
                # in the case of four oe more books, the accout will be closed :
                else:
                    user["Status_accout"] = False
                    return "oops your accout has been banned please return book and try again! 💤"
            
        return "Please check your information"
    #! function save data new book :
    def save_to_json(self):
    
        with open(path_data_books, 'w') as sdb:
            sdb.write(dumps(load_books_from_json, indent=4))
        return 'data book save successfully ✅ '
        

#?########################################################################################################################################################################
#? create class User space : 

class User():
    def __init__(self, user_name=False, user_id=False):
        self.user = user_name
        self.id  = user_id
    #! search in data file json id name user register or not : 
    def search(self):
        
        for user in load_user_from_json["data_users"]:
            if self.user == user["Name"] and self.id == user["ID"]:
                info = f'__Found User__:\n- User Name: {user["Name"]}\n- User ID: BL-{user["ID"]}'
                books_and_status = f'\n__Books and Status__:\n- Books Taken:\n{"| ".join(user["History_books"]["Taken"])} \n- Books Retriever:\n{"| ".join(user["History_books"]["Retriever"])} \n- Status: {"".join(["✅ Activate" if user["Status_accout"]== True else "Closed 🚫"])}'
                print(info, books_and_status)
                return 
        print(f'{self.user} Not Found!!')
    
        #! this function for user return book and remove for list books :
    def return_book(self):
        for user in load_user_from_json["data_users"]:
            if self.user == user["Name"] and self.id == user["ID"]:
                if user["History_books"]["Taken"]:
                    set_number = enumerate(user["History_books"]["Taken"])
                    print(f'__Book in your list:__')
                    for rank, name_book in set_number:
                        print(f'{rank+1}- {name_book}')
                    return_choice = int(input('Please enter number book return: '))
                    user["History_books"]["Retriever"].append(user["History_books"]["Taken"][return_choice-1])
                    for book in load_books_from_json["data_books"]:
                        if user["History_books"]["Taken"][return_choice-1] == book["Details"]["Book_Name"]:
                            book["Status"]["number_available"] += 1
                    user["History_books"]["Taken"].remove(user["History_books"]["Taken"][return_choice-1])
                    print('return successfully ✅')
                    return
                else: 
                    print('You don\'t have book in your list')
                    return
        print('Please check your information 🔖 ')
        return

    #! add data user and register : 
    def user_registration(self):
        make_id = randint(1000000, 10000000)
        new_user = {
            "Name": self.user,
            "ID": make_id,
            "History_books": {"Taken":[], "Retriever":[]},
            "Status_accout": True
        }
        load_user_from_json["data_users"].append(new_user)
        return f'Add successfully ✅\n__Iformation Accout__:\nName:{self.user}\nID:{make_id}'
    
    def payment_active(self, user_id):
        for user in load_user_from_json["data_users"]:
            if user_id == user["ID"] and user["Status_accout"]==False:
                while True: 
                    card_number = input("CARD NUMBER 💳 🪪 (1234-5678-1234-5678): ")
                    if (len(card_number.replace('-', '')) != 16) or not card_number.replace('-', '').isnumeric():
                        print('please enter a correct number and enter correct format(1234-5678-1234-5678)' )
                        continue
                    while True:    
                        date_card = input("EXPIRATION ON THE CARD  💳(MM/YY): ")
                        try:
                            month, year = map(int, date_card.split('/'))
                            expiration_date = datetime(year=2000 + year, month=month, day=1)
                            current_date = datetime.now()
                            if expiration_date <= current_date:
                                print("Card has already expired.")
                                continue
                        except ValueError:
                            print("Invalid date format. Please use MM/YY format.")
                            continue
                        break
                        
                    while True:    
                        pass_card = input("CVC  💳 (123): ")
                        if (len(pass_card) != 3 ) or not pass_card.isnumeric():
                            print("Please enter a three numbers!! ")
                            continue
                        break
                    while True:    
                        name_card = input("NAME ON THE CARD 🪪 : ").strip()
                        if not name_card.replace(' ', '').isalpha():
                            print('Please enter correct name!!')
                            continue
                        user["Status_accout"] = True
                        return f'{"-"*20}\
                        \n✅ Your accout is activate 🔓\
                        \nCARD NUMBER: {card_number}\nEXPIRATION ON THE CARD: {date_card}\
                        \nNAME ON THE CARD: {name_card.title()}\
                        \n✅ The amount has been deducted 20$'
            else:
                return "please check status accout or user id"
                
        
    #! save all edit in files json and return message successfuly :
    def save_to_json(self):
        with open(path_data_user, 'w') as sdu:
            sdu.write(dumps(load_user_from_json, indent=4))
        return 'data user save successfully ✅'


#?###############################################################################################################################################

def library_run():
    while True:
        try :    
            
            massege_setup = f'''
            __Hello In The British Library__
            |1 - Space Library And Books 💾
            |2 - Space User 🔏 
            |3 - Exit 🔌
            |Please choice A Option : '''
            user_setup = int(input(massege_setup))
            if  user_setup > 3 or user_setup < 1 :
                raise IndexError()
            #! option sapce library and setup : 
            if user_setup == 1:
                massege_sapace_library = '''
            __Hello In Space Library__: 
            |1 - Search For A Book 📚
            |2 - Take Book 📖 
            |3 - Information Library
            |4 - Add New Book
            |5 - Exit 🔌
            |Please choice A Option : '''
                sapace_library = int(input(massege_sapace_library))
                if  sapace_library > 5 or sapace_library < 1 :
                    raise IndexError()
                if sapace_library == 1:
                    name_book = input('Please enter name book: ')
                    class_Book = Book(name_book)
                    print(class_Book.search())
                elif sapace_library == 2:
                    name_book = input('Please enter name book: ')
                    class_Book = Book(name_book)
                    check = class_Book.search()
                    if check == "All copies finished 💢" or check == "Not found in library data, Please add this book 🛑":
                        print("All copies finished 💢 or Not found in library data!!")
                    else : 
                        name_user = input('Please enter name user: ')
                        id_user = int(input('Please enter ID user: '))
                        print(class_Book.take_book(name_user, id_user))
                elif sapace_library == 3:
                    class_Book = Book("information library")
                    print(class_Book)
                elif sapace_library == 4:
                    name_book = input("Please enter name book: ")
                    type_book = input('Please enter category book: ')
                    author_book = input("Please enter author: ")
                    year_book = int(input("Please enter year of publication: "))
                    number_copie = int(input("Please enter number copie: "))
                    class_Book = Book(name_book, type_book, author_book, year_book)
                    print(class_Book.add_book(number_copie))
                else:
                    continue
            #! option sapce user and setup : 
            elif user_setup == 2:
                massege_sapace_user = '''
            __Hello In Space Users__: 
            |1 - Search User 👨🏼 / 👩🏻
            |2 - Registration New User 👤
            |3 - Return Book 📒
            |4 - Unlock Accout For 20$ 🔓
            |5 - Exit 🔌
            |Please choice A Option : '''
                sapace_user = int(input(massege_sapace_user))
                if  sapace_user > 5 or sapace_user < 1 :
                    raise IndexError()
                if sapace_user == 1:
                    name_user = input('Please enter name user: ')
                    id_user = int(input('Please enter ID user: '))
                    class_User = User(name_user, id_user)
                    class_User.search()
                elif sapace_user == 2:
                    name_user = input('Please enter name user: ')
                    class_User = User(name_user)
                    print(class_User.user_registration())
                elif sapace_user == 3:
                    name_user = input('Please enter name user: ')
                    id_user = int(input('Please enter ID user: '))
                    class_User = User(name_user, id_user)
                    class_User.return_book()


                elif sapace_user == 4:
                    id_user = int(input('Please enter ID user for activate: '))
                    class_User = User()
                    print(class_User.payment_active(id_user))
                    
            #! end programe
            else:
                while True:
                    save_modifications = input('you need save new data [Y/N]: ').upper()
                    if save_modifications == 'Y':
                        save_data_user = User()
                        save_data_book = Book()
                        print(save_data_user.save_to_json())
                        print(save_data_book.save_to_json())
                    elif save_modifications == 'N':
                        print('save failed 🗑️')
                    else: 
                        continue
                    print("Thank for using the program |The British Library| ")
                    return
        except ValueError:
            print("| Please enter a number type!! |")
        except IndexError:
            print('| Please enter a number in option!! |')
library_run()
