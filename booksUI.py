#John Coronado, Connor Faucher, Xuan Nguyen, Omar Top

import csv
from load_data import load_dataset
from search_modify_dataset import *
from csv_sorting import *

# UI Functions

def display():
    print("\
\n1. Command Line L)oad file\
\n2. Command Line A)dd book\
\n3. Command Line R)emove book\
\n4. Command Line F)ind book by title\
\n5. Command Line NC) Number of books in a category\
\n6. Command Line CA) Categories for an author\
\n7. Command Line CB) Categories for a book title\
\n8. Command Line G)et book\
\n9. Command Line S)ort book\
\n10. Command line Q)uit")
    
def display_G():
    print("R)ate  A)uthor  P)ublisher  C)ategory\
\nCT) Category and Title  CR) Category and Rate")

def display_S():
    print("T)itle  R)ate  P)ublisher  C)ategory  PA)geCount")

def prompt():
    init = input("\n: ")
    return init.upper()

def check_quit(command):
    if command == 'Q':
        return 1
    return 0

def check_valid(command):
    valid_commands = ['L', 'A', 'R', 'F', 'NC', 'CA', 'CB', 'G', 'S', 'Q']
    if command in valid_commands:
        return 1
    print("No such command.")
    return 0

# Command Functions

def command_L():
    file = input("Please input file: ")
    dataset = load_dataset(file)
    print(dataset)
    return dataset

def command_A(data):
    book = input("Please input book. Enter 'help' to display accepted book format: ")
    i = 0
    while i == 0:
        if book != 'help':
            book = tuple(map(str, book.split(', ')))
            dataset = add_book(data, book)
            print(dataset)
            return dataset        
        print("Enter book information in the following order: title, author, language, publisher, category, rating, and page count.")
        print("Example: To Kill a Mockingbird, Harper Lee, English, J.B. Lippincott, Fiction, 5, 281")        
        book = input("\nPlease input book: ")
        
def command_R(data):
    title = input("Please input book title: ")
    category = input("Please input category: ")
    dataset = remove_book(title, category, data)
    print(dataset)
    return dataset    
            
def command_F(data):
    title = input("Please input book title: ")
    find_books_by_title(title, data)
    return data

def command_NC(data):
    category = input("Please input category: ")
    print_dictionary_category(category, data)
    return data

def command_CA(data):
    author = input("Please input author: ")
    get_author_categories(author, data)
    return data

def command_CB(data):
    title = input("Please input book title: ")
    all_categories_for_book_title(title, data)
    return data

def command_G(data):
    """
    """
    display_G()
    subcommand = prompt()
    
    if check_quit(subcommand) == 1:
        return subcommand
    
    if subcommand == 'R':
        rate = input("Please input rate: ")
        rate = float(rate)
        get_books_by_rate(rate, data)
        return data

    if subcommand == 'A':
        author = input("Please input author: ")
        get_books_by_author(data, author)
        return data
    
    if subcommand == 'P':
        publisher = input("Please input publisher: ")
        get_books_by_publisher(publisher, data)
        return data
    
    if subcommand == 'C':
        category = input("Please input category: ")
        get_books_by_category(data, category)
        return data
    
    if subcommand == 'CT':
        category = input("Please input category: ")
        title = input("Please input book title: ")
        check_category_and_title(category, title, data)
        return data

    if subcommand == 'CR':
        category = input("Please input category: ")
        rate = input("Please input rate: ")
        rate = float(rate)        
        get_book_by_category_and_rate(category, rate, data)
        return data
                
def command_S(data):
    """
    """
    display_S()
    subcommand = prompt()
    
    if check_quit(subcommand) == 1:
        return subcommand   
    
    if subcommand == 'T':
        print(sort_books_title(data))
        return data
        
    if subcommand == 'R':
        ratecommand = input("Please input order: ")
        
        if ratecommand == "ascending":
            sort_books_ascending_rate(data)
            return data
        
        elif ratecommand == "descending":  
            sort_books_descending_rate(data)
            return data
        
        else:                
            print("Invalid order. Accepted orders are 'ascending' or 'descending'.")
            return data
        
    if subcommand == 'P':
        sort_books_publisher(data)
        return data
            
    if subcommand == 'C':
        sort_books_category(data)
        return data
                                   
    if subcommand == 'PA':
        sort_books_pageCount(data)
        return data
      
def select(command, data):
    if command == 'L':
        return command_L()
    if command == 'A':
        return command_A(data)
    if command == 'R':
        return command_R(data)
    if command == 'F':
        return command_F(data)
    if command == 'NC':
        return command_NC(data)
    if command == 'CA':
        return command_CA(data)
    if command == 'CB':
        return command_CB(data)
    if command == 'G':
        return command_G(data)
    if command == 'S':
        return command_S(data)
    
# Main Script    

data = None
cont = ''

while cont != 'Q':
    display()
    command = prompt()
    if check_quit(command) == 1:
        cont = 'Q'
    elif command != 'L' and data == None:
        print("No file loaded.")
    else:
        if check_valid(command) == 1:
            data = select(command, data)
            if data == 'Q': # subcommand quit
                cont = 'Q'
                
