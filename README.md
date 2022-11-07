Contact Information
--------------------
The project can be reached through: Omar Top
Email: omartop@cmail.carleton.ca

Date
-----
December 10, 2021

Software’s Name and Version
----------------------------
ECOR1042 T028_data_analyzer Project Version 1.0 10/12/2021

Description
------------
The project consists of a basic user interface as well as multiple modules within the interface. The modules contain functions within them. The user interface prompts the user of the program to provide a CSV file containing the dataset of different books and to then select one of ten commands, all of which are displayed in the shell. 
The project is made up of four files:
- load_dataset.py
- search_modify_dataset.py
- csv_sorting.py
- booksUI.py

Installation
-------------
Python 3.9.1 or later must be installed.
Only built-in Python modules are used. Module “csv” is imported in the files. No other external modules are used. 

Usage
-------
> python T028_P4_booksUI.py
When prompted, enter the letter(s) that are displayed on the shell. For all commands, both upper-case and lower-case letters are accepted.
The application will display the error message "No file loaded" if you attempt to use one of the 
commands before you have loaded a file into the editor.
Press Q to quit and end the program.

Credits
--------
Omar Top:
- Functions find_books_by_title, get_books_by_publisher, and get_author_categories in T028_P2_search_modify_dataset.py
- Functions sort_books_pageCount and sort_books_category in T028_P3_sorting.py
- Command Line L)oad file, Command Line A)dd book, Command Line R)emove book, and Command Line F)ind book by title in T028_P4_booksUI.py

Connor Faucher:
- P5_T028_load_dataset.py
- Functions check_category_and_title, all_categories_for_book_title, and get_book_by_category_and_rate in T028_P2_search_modify_dataset.py
- Functions sort_books_descending_rate and sort_books_publisher in T028_P3_sorting.py
- Command Line NC), Command Line CA), and Command Line CB), and Command line Q)uit in T028_P4_booksUI.py

Xuan Nguyen:
- Functions print_dictionary_category, remove_book,and get_books_by_rate in T028_P2_search_modify_dataset.py
- Function sort_books_ascending_rate in T028_P3_sorting.py
- Command Line S)ort book and its subcommands in T028_P4_booksUI.py

John Coronado:
- P5_T028_load_dataset.py
- Functions add_book, get_books_by_author, and get_books_by_category in T028_P2_search_modify_dataset.py
- Function sort_books_title in T028_P3_sorting.py
- Command Line G)et book and its subcommands in T028_P4_booksUI.py 

License
--------
Copyright 2021 ECOR1042. All rights reserved.
T028_data_analyzer Project Version 1.0 and its use are subject to a license agreement and are also subject to copyright, trademark, patent and/or other laws.
