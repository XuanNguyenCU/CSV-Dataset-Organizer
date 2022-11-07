# T028 Xuan Nguyen 101228417
# Testing functions 5 and 6

import csv
from unit_testing import check_equal
from load_data import load_dataset
from csv_sorting import sort_books_pageCount, sort_books_category


# Testing sort_books_pageCount. Function written by Omar Top.

def test_sort_books_pageCount () -> None:
    
    """ Test case for function sort_books_pageCount.
    
    
    >>>test_sort_books_pageCount()
    
    sort_books_pageCount(load_dataset('Google_Books_Unsorted2.csv')) PASSED
    ------
    sort_books_pageCount(load_dataset('Google_Books_Unsorted2.csv')) PASSED
    ------

    """
    infile = csv.DictReader(open('Google_Books_pageCount.csv'))
    
    book_list = []
    
    for row in infile:
        row.pop('')
        book_list += [row]    
            
     
    infile2 = csv.DictReader(open('Google_Books_pageCount2.csv'))
                                    
    book_list2 = []
                                    
    for row2 in infile2:
        row2.pop('')
        book_list2 += [row2]  
        
    
    check_equal("sort_books_pageCount(load_dataset('Google_Books_Unsorted.csv'))", sort_books_pageCount(load_dataset('Google_Books_Unsorted.csv')), book_list) 
    check_equal("sort_books_pageCount(load_dataset('Google_Books_Unsorted2.csv'))", sort_books_pageCount(load_dataset('Google_Books_Unsorted2.csv')), book_list2) 



# Testing sort_books_category. Function written by Omar Top.

def test_sort_books_category () -> None:
    
    """Test case for function sort_books_category.
    
    
    >>>test_sort_books_category()
    
    sort_books_category(load_dataset('Google_Books_Unsorted.csv')) PASSED
    ------
    sort_books_category(load_dataset('Google_Books_Unsorted2.csv')) PASSED
    ------

    """
    
    infile = csv.DictReader(open('Google_Books_Category.csv'))
    
    book_list = []
    
    for row in infile:
        row.pop('')
        book_list += [row]    
            
     
    infile2 = csv.DictReader(open('Google_Books_Category2.csv'))
                                        
    book_list2 = []
                                        
    for row2 in infile2:
        row2.pop('')
        book_list2 += [row2]   
           
    check_equal("sort_books_category(load_dataset('Google_Books_Unsorted.csv'))", sort_books_category(load_dataset('Google_Books_Unsorted.csv')), book_list)
    check_equal("sort_books_category(load_dataset('Google_Books_Unsorted2.csv'))", sort_books_category(load_dataset('Google_Books_Unsorted2.csv')), book_list2) 


# Main Script

test_sort_books_pageCount ()
test_sort_books_category ()