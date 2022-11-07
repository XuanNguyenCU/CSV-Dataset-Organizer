# Group: T028
# Group Members: John Coronado 101230184, Connor Faucher 101235048, Xuan Nguyen 101228417, Omar Top 


from load_data import load_dataset


# Function 1: sort_books_title. Written by John Coronado.

def sort_books_title(book_dictionary: dict) -> list:
    book_list = []
    for Category in book_dictionary:
        for book_info in book_dictionary[Category]:
            book_info["genres"] = Category
            book_list.append(book_info) # adds values from dictionary to list
            
    sorted_books = book_list # sets book info to another list before sorting
    
    num_books = len(sorted_books)
    
    for item in range(num_books - 1):
        for i in range(0, num_books - item - 1): 
            # iterates from 0 to num_book - item - 1
            # swap if the element found is greater than the next element
            if sorted_books[i]['title'] > sorted_books[i+1]['title']:
                sorted_books[i], sorted_books[i+1] = sorted_books[i+1], \
                    sorted_books[i]
    print(sorted_books)            
    return sorted_books


# Function 2: sort_books_ascending_rate. Written by Xuan Nguyen.

def sort_books_ascending_rate (dataset: dict) -> list:
    """ Creates a list with the book data. Each element of the list is a dictionary where all book data is stored. 
    Returns a list with the book data stored as a dictionary book where the books are sorted by the rate in ascending order. The function will also print the data.

    >>> sort_books_ascending_rate((load_dataset("Google_Books_Dataset.csv")))
    
    [ ... {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'authors': 'Andrzej Sapkowski', 'language': 'English', 'rating': '4.8', 'publisher': 'Hachette UK', 'page count': '400'} ... {'title': 'The Red Signal: An Agatha Christie Short Story', 'authors': 'Agatha Christie', 'language': 'English', 'rating': '5', 'publisher': 'HarperCollins UK', 'page count': '40'} ]

    
    """
    book_list = []

    for key in dataset:
        for category in dataset.keys():
            books = dataset.get(category)
            for book in books:
                book["genres"] = category    
            
        for dictionary in dataset[key]:
            book_list += [dictionary] # adds every dictionary of books to the list
            
            num = len(book_list)
          
                
            for dic in range(num): # for every index that contains the dictionary of books in the list
                        
                for j in range(0, num-dic-1):
                            # Traverse the array from 0 to num-dic-1
                            # Swap if the element found is greater than the next eleement.
                    
                    if book_list[j]["rating"] == "": # if book does not have a rating
                        book_list[j]["rating"] = "0"                   
                        
                    if book_list[j]['rating'] >= book_list[j + 1]['rating']:
                        book_list[j], book_list[j + 1] = book_list[j + 1], book_list[j]            
    print(book_list)                                          
    return book_list   


# Function 3: sort_books_descending_rate Written by Connor Faucher.

def sort_books_descending_rate (book_dictionary: dict) -> list[dict]:
    """
    Function takes a dictionary in which books are stored by their category.
    Returns a list of the individual books (organized in dictionary form) 
    organized based on the book's rating in descending order; from highest to 
    lowest. 
    Note: Due to the original inputed dictionary, some books may appear multiple
    times because they appear in multiple categories.
    
    >>> books_dict = load_dataset("test_file1.csv")
    {'Comics': [{'title': 'Deadpool Kills the Marvel Universe', 'authors': 'Cullen Bunn', 'language': 'English', 'rating': '4.2', 'publisher': 'Marvel Entertainment', 'page count': '96'}], 'Economics': [{'title': 'How To Win Friends and Influence People', 'authors': 'Dale Carnegie', 'language': 'English', 'rating': '4.3', 'publisher': 'Simon and Schuster', 'page count': '320'}], 'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'authors': 'Barbara Allan', 'language': 'English', 'rating': '3.3', 'publisher': 'Kensington Publishing Corp.', 'page count': '288'}]}
    >>> sort_books_descending_rate(books_dict)
    [{'title': 'How To Win Friends and Influence People', 'authors': 'Dale Carnegie', 'language': 'English', 'rating': '4.3', 'publisher': 'Simon and Schuster', 'page count': '320'}, {'title': 'Deadpool Kills the Marvel Universe', 'authors': 'Cullen Bunn', 'language': 'English', 'rating': '4.2', 'publisher': 'Marvel Entertainment', 'page count': '96'}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'authors': 'Barbara Allan', 'language': 'English', 'rating': '3.3', 'publisher': 'Kensington Publishing Corp.', 'page count': '288'}]

    """
    key_list = book_dictionary.keys()
    book_list = []
    for key in key_list:
        for book in book_dictionary[key]:
            if book["rating"] == "":
                book["rating"] = "0"
            book["genres"] = key
            book_list += [book]
    
    n = len(book_list)
    for i in range(n):
        for j in range(n - i - 1):
            if book_list[j]["rating"] < book_list[j+1]["rating"]:
                book_list[j], book_list[j+1] = book_list[j+1], book_list[j]
   
    print(book_list)
    return book_list



# Function 4: sort_books_publisher. Written by Connor Faucher.
 
def sort_books_publisher (book_dictionary: dict) -> list[dict]:
    """
    Function takes a dictionary in which books are stored by their category.
    Returns a list of the individual books (organized in dictionary form) in 
    alphabetical order based on the book's given publisher. If multiple books 
    have the same publisher, those books will appear in alphabetical orser based
    on their title.
    Note: Due to the original inputed dictionary, some books may appear multiple
    times because they appear in multiple categories.
    
    >>> books_dict = load_dataset("test_file2.csv")
    {'Business': [{'title': 'Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 'authors': 'T. Harv Eker', 'language': 'English', 'rating': '4.6', 'publisher': 'Harper Collins', 'page count': '224'}], 'Detective': [{'title': 'The Memoirs of Sherlock Holmes', 'authors': 'Arthur Conan Doyle', 'language': 'English', 'rating': '4.2', 'publisher': 'Simon and Schuster', 'page count': '320'}], 'Fiction': [{'title': 'The Painted Man (The Demon Cycle, Book 1)', 'authors': 'Peter V. Brett', 'language': 'English', 'rating': '4.5', 'publisher': 'HarperCollins UK', 'page count': '544'}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'authors': 'Brian McGilloway', 'language': 'English', 'rating': '4', 'publisher': 'Harper Collins', 'page count': '336'}, {'title': 'Bring Me Back', 'authors': 'B A Paris', 'language': 'English', 'rating': '3.8', 'publisher': 'HarperCollins UK', 'page count': '368'}],  'Psychology': [{'title': 'How To Win Friends and Influence People', 'authors': 'Dale Carnegie', 'language': 'English', 'rating': '4.3', 'publisher': 'Simon and Schuster', 'page count': '320'}]}
    >>> sort_books_descending_rate(books_dict)
    [{'title': 'Little Girl Lost: A Lucy Black Thriller', 'authors': 'Brian McGilloway', 'language': 'English', 'rating': '4', 'publisher': 'Harper Collins', 'page count': '336'}, {'title': 'Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 'authors': 'T. Harv Eker', 'language': 'English', 'rating': '4.6', 'publisher': 'Harper Collins', 'page count': '224'}, {'title': 'Bring Me Back', 'authors': 'B A Paris', 'language': 'English', 'rating': '3.8', 'publisher': 'HarperCollins UK', 'page count': '368'}, {'title': 'The Painted Man (The Demon Cycle, Book 1)', 'authors': 'Peter V. Brett', 'language': 'English', 'rating': '4.5', 'publisher': 'HarperCollins UK', 'page count': '544'}, {'title': 'How To Win Friends and Influence People', 'authors': 'Dale Carnegie', 'language': 'English', 'rating': '4.3', 'publisher': 'Simon and Schuster', 'page count': '320'}, {'title': 'The Memoirs of Sherlock Holmes', 'authors': 'Arthur Conan Doyle', 'language': 'English', 'rating': '4.2', 'publisher': 'Simon and Schuster', 'page count': '320'}]
    """
    key_list = book_dictionary.keys()
    book_list = []
    for key in key_list:
        for book in book_dictionary[key]:
            book["genres"] = key
            book_list += [book]
    
    n = len(book_list)
    for i in range(n):
        for j in range(n-i-1):
            temp_list1 = [book_list[j]["publisher"], book_list[j+1]["publisher"]] 
            temp_list1.sort()
            if temp_list1 == [book_list[j+1]["publisher"], book_list[j]["publisher"]]:
                book_list[j], book_list[j+1] = book_list[j+1], book_list[j]
    
    for i in range(n):
        for j in range(n- i-1):
            if book_list[j]["publisher"] == book_list[j+1]["publisher"]:
                temp_list2 = [book_list[j]["title"], book_list[j+1]["title"]]
                temp_list2.sort()
                if temp_list2 == [book_list[j+1]["title"], book_list[j]["title"]]:
                    book_list[j], book_list[j+1] = book_list[j+1], book_list[j]
                
    print(book_list)
    return book_list



# Function 5: sort_books_pageCount. Written by Omar Top.

def sort_books_pageCount(book_dictionary: dict) -> list:
    """
    Returns a list with the book data stored as a dictionary book, books sorted by page count in ascending order.
    
    >>> sort_books_pageCount(load_dataset("Google_Books_Dataset.csv"))
    [{'title': 'Summary: Think and Grow Rich', 'authors': 'Nine99 Innovation Lab', 'language': 'English', 'rating': '', 'publisher': 'Nine99 Innovation Lab (OPC) Pvt Ltd', 'page count': '14', 'genres': 'Business'}, ... {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)', 'authors': 'George R.R. Martin', 'language': 'English', 'rating': '4.5', 'publisher': 'HarperCollins UK', 'page count': '4544', 'genres': 'Fiction'}]
    
    """
    book_list = []
    
    keys = book_dictionary.keys()
    for key in keys:
        for book in book_dictionary[key]:
            book['genres'] = key
            book_list += [book]
            
    n = len(book_list)
    for i in range(n):
        for j in range(n - i - 1):
            book1, book2 = book_list[j], book_list[j + 1]
            if int(book1['page count']) > int(book2['page count']):
                book_list[j], book_list[j + 1] = book_list[j + 1], book_list[j]
            elif int(book1['page count']) == int(book2['page count']) and book1['title'] > book2['title']:
                book_list[j], book_list[j + 1] = book_list[j + 1], book_list[j]                    
                    
    print(book_list)
    return book_list



# Function 6: sort_books_category. Written by Omar Top.

def sort_books_category(book_dictionary: dict) -> list:
    """
    Returns a list with the book data stored as a dictionary book, books sorted category in alphabetical order.
    
    >>> sort_books_category(load_dataset("Google_Books_Dataset.csv"))
    [{'title': 'A Feast for Crows (A Song of Ice and Fire, Book 4)', 'authors': 'George R.R. Martin', 'language': 'English', 'rating': '4.5', 'publisher': 'HarperCollins UK', 'page count': '864', 'genres': 'Adventure'}, ... {'title': 'The Red Signal: An Agatha Christie Short Story', 'authors': 'Agatha Christie', 'language': 'English', 'rating': '5', 'publisher': 'HarperCollins UK', 'page count': '40', 'genres': 'Traditional'}]
    
    """
    book_list = []
    
    keys = book_dictionary.keys()
    for key in keys:
        for book in book_dictionary[key]:
            book['genres'] = key
            book_list += [book]
            
    n = len(book_list)
    for i in range(n):
        for j in range(n - i - 1):
            book1, book2 = book_list[j], book_list[j + 1]
            if book1['genres'] > book2['genres']:
                book_list[j], book_list[j + 1] = book_list[j + 1], book_list[j]
            elif book1['genres'] == book2['genres'] and book1['title'] > book2['title']:
                book_list[j], book_list[j + 1] = book_list[j + 1], book_list[j]
                    
    print(book_list)
    return book_list


if __name__ == '__main__':
    sort_books_title(load_dataset("Google_Books_Dataset.csv"))
    sort_books_ascending_rate(load_dataset("Google_Books_Dataset.csv"))
    sort_books_descending_rate(load_dataset("Google_Books_Dataset.csv"))
    sort_books_publisher(load_dataset("Google_Books_Dataset.csv"))
    sort_books_pageCount(load_dataset("Google_Books_Dataset.csv"))
    sort_books_category(load_dataset("Google_Books_Dataset.csv"))
