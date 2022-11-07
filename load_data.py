import csv

def load_dataset(file_name: str) -> dict[list[dict]]:
    """
    Function written by Connor Faucher: 101235048
    
    Returns a dictionary of the Google Books Dataset (csv file type) organized 
    with the books' genres/categories as the dictionary keys. 
    The value of each key is a list of dictionaries for each book within the 
    dataset.
    
    >>> load_dataset("test_file.csv")
    {'Adventure': [], 'Biography': [], 'Business': [], 'Classics': [], 'Comics': [{'title': 'Deadpool Kills the Marvel Universe', 'authors': 'Cullen Bunn', 'language': 'English', 'rating': '4.2', 'publisher': 'Marvel Entertainment', 'page count': '96'}], 'Crime': [], 'Detective': [], 'Economics': [{'title': 'How To Win Friends and Influence People', 'authors': 'Dale Carnegie', 'language': 'English', 'rating': '4.3', 'publisher': 'Simon and Schuster', 'page count': '320'}], 'Epic': [], 'Fantasy': [], 'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'authors': 'Barbara Allan', 'language': 'English', 'rating': '3.3', 'publisher': 'Kensington Publishing Corp.', 'page count': '288'}], 'Finance': [], 'Horror': [], 'Humor': [], 'Information Technology': [], 'Investing': [], 'Legal': [], 'Management': [], 'Money Management': [], 'Mystery': [], 'Mythical Creatures': [], 'Psychology': [], 'Social Science': [], 'Superheroes': [], 'Thrillers': [], 'Traditional': []}
    """
    # Below, are empty lists of genres for dictionaries of the books' data to be added.
    adven_list = []
    bio_list = []
    busi_list = []
    class_list = []
    comics_list = []
    crime_list = []
    detect_list = []
    eco_list = []
    epic_list = []
    fant_list = []
    fiction_list = []
    fin_list = []
    horror_list = []
    humor_list = []
    tech_list = []
    invest_list = []
    legal_list = []
    manage_list = []
    money_list = []
    myst_list = []
    mythic_list = []
    psy_list = []
    sosci_list = []
    super_list = []
    thrill_list = []
    trad_list = []
    
    book_dictionary = {"Adventure": adven_list, "Biography": bio_list, "Business": busi_list, "Classics": class_list, "Comics": comics_list, "Crime": crime_list, "Detective": detect_list, "Economics": eco_list, "Epic": epic_list, "Fantasy": fant_list, "Fiction": fiction_list, "Finance": fin_list, "Horror": horror_list, "Humor": humor_list, "Information Technology": tech_list, "Investing": invest_list, "Legal": legal_list, "Management": manage_list, "Money Management": money_list, "Mystery": myst_list, "Mythical Creatures": mythic_list,  "Psychology": psy_list, "Social Science": sosci_list, "Superheroes": super_list, "Thrillers": thrill_list, "Traditional": trad_list}
    
    infile = open(file_name, "r")
    file_list = csv.reader(infile)
    
    for line in file_list:
        line_dict = [{"title":line[1], "authors":line[2], "language":line[7], "rating":line[3], "publisher":line[4], "page count":line[5]}]
      
        for category in book_dictionary:
            if line[6] == category:
                book_dictionary[category] += line_dict
                book_dictionary.update()
               
                
    infile.close() # code would still run without this line

    return book_dictionary

if __name__ == '__main__':        
    print(load_dataset("Google_Books_Dataset.csv"))