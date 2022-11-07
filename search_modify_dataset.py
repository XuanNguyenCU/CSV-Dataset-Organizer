from load_data import load_dataset

book_dictionary = load_dataset("Google_Books_Dataset.csv")


# Function 1 written by Xuan Nguyen

def print_dictionary_category (category: str, dataset: dict) -> int:
    """ Prints the details of each book in the category. Returns the number of elements (books) associated with that key in the dictionary.
    
    >>>print_dictionary_category("Classics", book_dictionary)
    
    The category Classics has 2 books. This is the list of books in the category Classics: [{'title': 'The Memoirs of Sherlock Holmes', 'authors': 'Arthur Conan Doyle', 'language': 'English', 'rating': '4.2', 'publisher': 'Simon and Schuster', 'page count': '320'}, {'title': 'The Mysterious Affair at Styles', 'authors': 'Agatha Christie', 'language': 'English', 'rating': '4.4', 'publisher': 'HarperCollins UK', 'page count': '208'}]
    
    2
    
    """
    
    list_books = dataset.get(category)
    
    count = 0
    for dictionary in list_books:
        count += 1
    print( "The category " + category + " has " + str(count) + " books. This is the list of books in the category", category + " : " + str(list_books))

    return count



# Function 2 written by John Coronado

def add_book(book_dictionary: dict, book:tuple) -> dict:
    """ Returns the given dictionary with the tuple argument added. Tuple
    must have seven arguments in this order: title, author, language, publisher,
    category, rating, and page count.
    
    >>> add_book(load_dataset('Google_Books_Dataset.csv'), ('Little Girl Lost: A Lucy Black Thriller', 'Brian McGilloway', 'English', 'Harper Collins', 'Adventure', 4, 336))
    {'Adventure': [{'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'authors': 'Andrzej Sapkowski', 'language': 'English', 'rating': '4.8', 'publisher': 'Hachette UK', 'page count': '400'}, {'title': 'A Feast for Crows (A Song of Ice and Fire, Book 4)', 'authors': 'George R.R. Martin', 'language': 'English', 'rating': '4.5', 'publisher': 'HarperCollins UK', 'page count': '864'}, {'title': 'After Anna', 'authors': 'Alex Lake', 'language': 'English', 'rating': '4.1', 'publisher': 'HarperCollins UK', 'page count': '416'}, {'title': 'The Way Of Shadows: Book 1 of the Night Angel', 'authors': 'Brent Weeks', 'language': 'English', 'rating': '4.7', 'publisher': 'Hachette UK', 'page count': '688'}, {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)', 'authors': 'George R.R. Martin', 'language': 'English', 'rating': '4.5', 'publisher': 'HarperCollins UK', 'page count': '4544'}, {'title': 'Edgedancer: From the Stormlight Archive', 'authors': 'Brandon Sanderson', 'language': 'English', 'rating': '4.8', 'publisher': 'Tor Books', 'page count': '226'}, {'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'authors': 'Andrzej Sapkowski', 'language': 'English', 'rating': '4.8', 'publisher': 'Hachette UK', 'page count': '96'}, ('Little Girl Lost: A Lucy Black Thriller', 'Brian McGilloway', 'English', 'Harper Collins', 'Adventure', 4, 336)], ... }
    """
    if book[4] in book_dictionary: # adds book to dictionary if the category was found
        book_dictionary[book[4]].append(book) 
    else:
        book_dictionary[book[4]] = [book]
    count = 0
    if book[4] in book_dictionary:
        if book in book_dictionary[book[4]]: # verification that the book was added
            count += 1
    if count == 0: # if there was a problem with the verification
        print("There was an error adding the book")
    else:
        print("The book has been added correctly")
    return book_dictionary



# Function 3 written by Xuan Nguyen

def remove_book(title: str, category: str) -> str:
    """ Prints the updated list of dictionaries in the cateory and returns a message stating whether or not there was an error.
    
    >>>remove_book("The Memoirs of Sherlock Holmes", "Classics")
    
    Updated: [{'title': 'The Mysterious Affair at Styles', 'authors': 'Agatha Christie', 'language': 'English', 'rating': '4.4', 'publisher': 'HarperCollins UK', 'page count': '208'}]
    The book has been removed correctly.
    
    
    >>>remove_book("", "Comics")
    There was an error removing the book.
    
    """         
    
    list_books = book_dictionary.get(category)
    
    for dictionary in list_books:
        
        if dictionary["title"] == title:
            list_books.remove(dictionary)
            print ("Updated: " + str(list_books) )
            return "The book has been removed correctly."  
        
    else:
        return 'There was an error removing the book.'           



# Function 4 written by Xuan Nguyen

def get_books_by_rate(rate: int, book_dataset: dict) -> dict:
    """ Prints out a list of details from each book whose rating fit the range between the rate inputted and 1 int higher of the rate inputted.
    Returns a dictionary of the titles of all the books within the list and their rating.
    
    >>>get_books_by_rate(3, load_dataset("Google_Books_Dataset.csv"))
    
    [ ('Title: How to Understand Business Finance: Edition 2', 'Authors: Bob Cinnamon', 'Language: English', 'Rating: 3.5', 'Publisher: Kogan Page Publishers', 'Category: Business', 'Page Count: 176'), (...) ]
    
    {'How to Understand Business Finance: Edition 2': '3.5', 'The Infinite Game': '3.8', ... }
    
    
    """
    dict_list = {}
    counter = 0
    books = []
    dict_books = {}
    for i in range(len(book_dataset)):
        for dictionary in list(book_dataset.values())[i]:
            if dictionary["rating"] == "": # if book does not have a rating
                rating = 0.0
            else:
                book_rating = float(dictionary["rating"])
                if book_rating >= rate and book_rating < rate + 1:
                    counter += 1
                    dict_list[counter] = dictionary
                    books += [("Title: " + dictionary["title"], "Authors: " + dictionary["authors"], "Language: " + dictionary["language"], "Rating: " + dictionary["rating"], "Publisher: " + dictionary["publisher"], "Category: " + list(book_dataset.keys())[i], "Page Count: "+ dictionary["page count"])]
                    dict_books[dictionary["title"]] = dictionary["rating"]                    
    print(books)
    return dict_books


# Function 5
def find_books_by_title(title: str, dictionary: dict) -> bool:
    """
    Returns Boolean where value is True if a given title exists in the
    dictionary where the books are stored. False otherwise.
    
    >>> find_books_by_title('Total Control', dataset)
    True
    >>> find_books_by_title('The Catcher in the Rye', dataset)
    False
    """
    items = dictionary.items()
    
    for item in items:
        key, value = item
        for i in range(len(value)):
            book_title = value[i].get('title')
            if book_title == title:
                print("The book has been found")
                return True
            
    print("The book has NOT been found")
    return False


# Function 6: get_books_by_publisher

def get_books_by_author(book_dictionary: dict, author_name: str) -> list[str]:
    """ Returns a list of the books from book_dictionary writtem by the 
    given author.
    
    >>> get_books_by_author(load_dataset('Google_Books_Dataset.csv'), ('Agatha Christie'))
    The author Dale Carnegie has published the following books:
    1 - How To Win Friends and Influence People
    Thank you
    """
    count = 1
    books = []
    print ('The author', author_name, 'has published the following books:')
    items = book_dictionary.items()
    
    for item in items:
        key, val = item
        
        for i in range(len(val)):
            dict_author = val[i].get('authors')
            if dict_author == author_name:
                dict_title = val[i].get('title') # takes the title of book
                if dict_title not in books: # adds book title to list if it isn't already there
                    books += [dict_title]
                    print(str(count) + ' - ' + str(dict_title))
                    count += 1
    if books == []: # if there is no book written by the given author
        print('No books were found for this author.')
    return books


# Function 7
def get_books_by_publisher(publisher: str, dictionary: dict) -> list:
    """
    Returns a list of books by a publisher, given the publisher's name
    and the dictionary where the books are stored.
    
    >>> get_books_by_publisher('DC', dataset)
    ['Young Justice Vol. 1', 'The Joker']
    >>> get_books_by_publisher('Penguin', dataset)
    ['Boy Erased: A Memoir', 'No One Is Too Small to Make a Difference', 'The Infinite Game', 'The Magic of Thinking Big', 'Getting Things Done: The Art of Stress-Free Productivity']
    """
    print('The publisher', publisher, 'has published the following books:')    
    
    books = []
    items = dictionary.items()
        
    count = 1    
    for item in items:
        key, value = item
        for i in range(len(value)):
            book_publisher = value[i].get('publisher')
            if book_publisher == publisher:
                book_title = value[i].get('title')
                if book_title not in books:
                    books += [book_title]
                    print('\t' + str(count) + '- ' + str(book_title))
                    count += 1
    
    if books == []:
        print('No books found.')
        
    return books


# Function 8
def check_category_and_title (category: str, title: str, dataset: dict) -> bool:
    """
    Function written by Connor Faucher: 101235048
    
    Returns True if the title of the inputed book exists within the given 
    category of the given dictionary.
    
    >>> check_category_and_title("Horror", "The Mysterious Affair at Styles")
    The category 'Horror' has the book title 'The Mysterious Affair at Styles'.
    True
    
    >>> check_category_and_title("Horror", "Boy Erased: A Memoir", Google_B_Dict)
    The category 'Horror' does not have the book title Boy Erased: A Memoir.
    False
    
    >>> check_category_and_title("abc", "Spider-Verse: Volume 1", Google_B_Dict)
    The book category 'abc' does not exist. 
    """
    book_category_list = dataset.get(category)
    
    if book_category_list == None:
        print("The book category '"+category+"' does not exist.")
        return False
    
    for book in book_category_list:
        if title == book["title"]:
            print("The category '"+category+"' has the book title '"+title+"'.")
            return True
        else:
            print("The category '"+category+"' does not have the book title '"+title+"'.")
            return False
        

#Function 9  
def  all_categories_for_book_title (title: str, dataset: dict) -> list:
    """
    Function written by Connor Faucher: 101235048
    
    Returns a list of the categories, from the given dictionary, in which the 
    inputed book is within. 
    
    >>> all_categories_for_book_title("The Name of the Wind: The Kingkiller Chronicle:, Book 1", Google_B_Dict)
    The book title 'The Name of the Wind: The Kingkiller Chronicle:, Book 1' has the following categories:
    1 - Fantasy
    2 - Fiction
    ['Fantasy', 'Fiction']
    
    >>> all_categories_for_book_title("abc", Google_B_Dict)
    The book title 'abc' has the following categories:
    []
    """
    key_list = dataset.keys()
    cat_list = []
    
    for category in key_list:
        for book in dataset.get(category):
            if title == book["title"]:
                cat_list += [category]
    print("The book title '"+title+"' has the following categories:")
    for i in range(len(cat_list)):
        print(i+1, "-", cat_list[i])
    return cat_list 



# Function 10: get_books_by_category 

def get_books_by_category(book_dictionary:dict, category_name:str) -> list[str]:
    """ Returns a list of the books from book_dictionary for the given 
    category.
    
    >>> get_books_by_category(load_dataset('Google_Books_Dataset.csv'), 'Epic')
    The category Adventure has the following books:
    1 - Sword of Destiny: Witcher 2: Tales of the Witcher
    2 - A Feast for Crows (A Song of Ice and Fire, Book 4)
    3 - After Anna
    4 - The Way Of Shadows: Book 1 of the Night Angel
    5 - A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)
    6 - Edgedancer: From the Stormlight Archive
    7 - The Malady and Other Stories: An Andrzej Sapkowski Sampler
    """
    count = 1
    books = []
    print ('The category', category_name, 'has the following books:')
    items = book_dictionary.items()
    
    for item in items:
        key, val = item
        
        for i in range(len(val)):
            if key == category_name:
                dict_title = val[i].get('title') # takes the title of the book
                if dict_title not in books: # adds book title to list if it isn't already there
                    books += [dict_title]
                    print(str(count) + ' - ' + str(dict_title))
                    count += 1
    if books == []: # if there is no book written by the given author
        print('No books were found for this category.')
    return books


# Function 11 
def get_book_by_category_and_rate (category: str, rate: int, dataset: dict) -> list:
    """
    Function written by Connor Faucher: 101235048
    
    Returns a list of books from the given dictionary, that match the given 
    category and rate interval: (rate - (rate+1)).
    
    >>> get_book_by_category_and_rate("Comics", 4, Google_B_Dict)
    The category 'Comics' and rate 4 has the following books:
    1 - Deadpool Kills the Marvel Universe
    2 - Young Justice Vol. 1
    3 - Ultimate Spider-Man Vol. 11: Carnage
    4 - Immortal Hulk Vol. 1: Or Is He Both?
    5 - Watchmen (2019 Edition)
    6 - The Joker
    7 - Venomized
    ['Deadpool Kills the Marvel Universe', 'Young Justice Vol. 1', 'Ultimate Spider-Man Vol. 11: Carnage', 'Immortal Hulk Vol. 1: Or Is He Both?', 'Watchmen (2019 Edition)', 'The Joker', 'Venomized']

    >>> get_book_by_category_and_rate("no category", 4, Google_B_Dict)
    The book category 'no category' does not exist
    """
    book_category_list = dataset.get(category)
    book_cat_rate_list = []
    
    if book_category_list == None:
        return print("The book category '"+category+"' does not exist")
    
    for book in book_category_list:
        if rate <= float(book["rating"]) < rate+1:
            book_cat_rate_list += [book["title"]]
    print("The category '"+category+"' and rate "+str(rate)+" has the following books:")
    for i in range(len(book_cat_rate_list)):
        print(i+1, "-", book_cat_rate_list[i])        
    return book_cat_rate_list


# Function 12
def get_author_categories(author: str, dictionary: dict) -> list:
    """
    Returns a list of book categories that an author has published under,
    given the author's name and the dictionary where the books are stored.
    
    >>> get_author_categories('Blake Pierce', dataset)
    ['Detective', 'Fiction', 'Mystery', 'Thrillers']
    >>> get_author_categories('George R.R. Martin', dataset)
    ['Adventure', 'Epic', 'Fantasy', 'Fiction']
    """
    print('The author', author, 'has published books under the following categories:')    
    
    categories = []
    items = dictionary.items()
        
    count = 1    
    for item in items:
        key, value = item
        for i in range(len(value)):
            book_author = value[i].get('authors')
            if book_author == author:
                if key not in categories:
                    categories += [key]
                    print('\t' + str(count) + '- ' + str(key))
                    count += 1
    
    if categories == []:
        print('No categories found.')
    
    return categories



# Manual Testing
if __name__ == '__main__':  
    print_dictionary_category("Classics", book_dictionary)
    print(add_book(load_dataset('Google_Books_Dataset.csv'), ('Little Girl Lost: A Lucy Black Thriller', 'Brian McGilloway', 'English', 'Harper Collins', 'Adventure', 4, 336)))
    print(remove_book("The Memoirs of Sherlock Holmes", "Classics"))
    print(get_books_by_rate(5, load_dataset("Google_Books_Dataset.csv")))
    print(find_books_by_title('Total Control', load_dataset("Google_Books_Dataset.csv")))
    print(get_books_by_author(load_dataset('Google_Books_Dataset.csv'), ('Agatha Christie')))
    print(get_books_by_publisher('DC', load_dataset('Google_Books_Dataset.csv')))
    print(check_category_and_title("Horror", "The Mysterious Affair at Styles", book_dictionary))
    print(get_books_by_category(load_dataset('Google_Books_Dataset.csv'), 'Epic'))
    