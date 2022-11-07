# T028 Xuan Nguyen 101228417
# Testing functions 8, 10, and 12: check_category_and_title, get_books_by_category, get_author_categories

from load_data import load_dataset

import search_modify_dataset

# from T028_P2_search_modify_dataset import check_category_and_title, get_books_by_category, get_author_categories


def check_equal(description: str, outcome, expected) -> None:
    """
    Prints a "PASSED" message if outcome and expected have same type and are equal (as determined by the == operator); otherwise, print a "FAILED" message.
    
    Parameter "description" provides information that will interpret the test results; e.g., the call expression that yields outcome.
    
    Parameters "outcome" and "expected" are typically the actual value returned by a call expression and the value we expect a correct implementation of the function to return, respectively. 
    Both parameters must have the same type, which must be a type for which == is used to determine if two values are equal.
    Don't use this function to check if floats, lists of floats, tuples of floats, etc. are equal. 
    """
    
    outcome_type = type(outcome)
    expected_type = type(expected)
    if outcome_type != expected_type:
        
        print("{0} FAILED: expected ({1}) has type {2}, " \
              "but outcome ({3}) has type {4}".
              format(description, expected, str(expected_type).strip('<class> '), 
                      outcome, str(outcome_type).strip('<class> ')))
        
    elif outcome != expected:
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, outcome))
        
    else:
        print("{0} PASSED".format(description))
    print("------")
    


# Testing Function 8: check_category_and_title. Tested by Xuan Nguyen. Function written by Connor Faucher.
def test_check_category_and_title () -> None:
    
    """Test case for function check_category_and_title.
    
    
    >>>test_check_category_and_title()
    
    The category 'Horror' has the book title 'The Mysterious Affair at Styles'.
    (check_category_and_title('Horror', 'The Mysterious Affair at Styles', load_dataset('Google_Books_Dataset.csv')) PASSED
    ------

    """
    check_equal("(check_category_and_title('Horror', 'The Mysterious Affair at Styles', load_dataset('Google_Books_Dataset.csv'))" , (check_category_and_title("Horror", "The Mysterious Affair at Styles", load_dataset("Google_Books_Dataset.csv"))), True)



# Testing Function 10: get_books_by_category. Tested by Xuan Nguyen. Function written by John Coronado.
def test_books_by_category() -> None:
    
    """ Test case for function get_books_by_category.
    
    >>>test_books_by_category()
    The category Epic has the following books:
    1 - A Feast for Crows (A Song of Ice and Fire, Book 4)
    2 - The Tower of the Swallow: Witcher 6
    3 - A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)
    4 - The Way Of Shadows: Book 1 of the Night Angel
    get_books_by_category('Epic', load_dataset('Google_Books_Dataset.csv')) PASSED
    ------
       
    """
    check_equal("get_books_by_category(load_dataset('Google_Books_Dataset.csv'), 'Fantasy')", get_books_by_category(load_dataset('Google_Books_Dataset.csv'), 'Fantasy'), ['The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'The Name of the Wind: The Kingkiller Chronicle:, Book 1', 'Mistborn Trilogy: The Final Empire, The Well of Ascension, The Hero of Ages', 'A Feast for Crows (A Song of Ice and Fire, Book 4)', 'The Tower of the Swallow: Witcher 6', 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)', 'The Way Of Shadows: Book 1 of the Night Angel', 'The Lord of the Rings: The Fellowship of the Ring, The Two Towers, The Return of the King', 'The Weight of Honor (Kings and Sorcerers--Book 3)', 'Night of the Bold (Kings and Sorcerers--Book 6)', 'The Vagrant (The Vagrant Trilogy)', 'We', 'Prince of Thorns (The Broken Empire, Book 1)', "Chronicle of the Unhewn Throne: (The Emperor's Blades, The Providence of Fire, The Last Mortal Bond)", 'The Painted Man (The Demon Cycle, Book 1)'])



# Testing Function 12: get_author_categories. Tested by Xuan Nguyen. Function written by Omar Top.
def test_get_author_categories():
    """ Test case for function get_author_categories.
    
    >>>test_get_author_categories()
    
    The author Blake Pierce has published books under the following categories:
	1- Detective
	2- Fiction
	3- Mystery
	4- Thrillers
    get_author_categories('Blake Pierce', dataset) PASSED
    ------
    
    """
    check_equal("get_author_categories('Blake Pierce', dataset)", get_author_categories('Blake Pierce', load_dataset('Google_Books_Dataset.csv')), ['Detective', 'Fiction', 'Mystery', 'Thrillers'])



# Main Script

test_check_category_and_title()
test_books_by_category()
test_get_author_categories()
