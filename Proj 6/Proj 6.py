###############################################################################
#    Computer Project #6
#
#    Program that reads over files and filters out information \n
#    basde on the input given by the user
#
#    The first part of the program initializes the constants
#
#    After the constants are made, the menu, user inputs, and header \n
#    / format variables are made
#
#    The next part of the program defines the functions needed to \n
#    make the program work. The key functions would be the open and read file \n
#
#    Once the functions are made, the program goes into the main function
#
#    The main function is where the user enters an input from 1 to 4 and \n
#    the program
#    gives information based on the option entered
#    
#    If the user enters an invalid input, an error message will appear and \n
#    a reprompt 
#
#    If the user enters 4, the program will close
#
#    The program will always reprompt the user for another option after the \n
#    information is given
##############################################################################



import csv
from operator import itemgetter

# Constants needed to filtering information
NAME = 0
ELEMENT = 1
WEAPON = 2
RARITY = 3
REGION = 4

# Menu option for user to select
MENU = "\nWelcome to Genshin Impact Character Directory\n\
        Choose one of below options:\n\
        1. Get all available regions\n\
        2. Filter characters by a certain criteria\n\
        3. Filter characters by element, weapon, and rarity\n\
        4. Quit the program\n\
        Enter option: "


# Error message when there is an invalid input
INVALID_INPUT = "\nInvalid input"

# User selects a criteria from the list
CRITERIA_INPUT = "\nChoose the following criteria\n\
                 1. Element\n\
                 2. Weapon\n\
                 3. Rarity\n\
                 4. Region\n\
                 Enter criteria number: "

# User enters value after selecting criteria
VALUE_INPUT = "\nEnter value: "


ELEMENT_INPUT = "\nEnter element: "
WEAPON_INPUT = "\nEnter weapon: "
RARITY_INPUT = "\nEnter rarity: "

# Format for displaying characters
HEADER_FORMAT = "\n{:20s}{:10s}{:10s}{:<10s}{:25s}"
ROW_FORMAT = "{:20s}{:10s}{:10s}{:<10d}{:25s}"


# Opens the file entered
def open_file():
    file_data = input("Enter file name: ")

    x = 0
    while x == 0:
        try:
            file_pointer = open(file_data)
            break
        except:
            print("\nError opening file. Please try again.")
            file_data = input("Enter file name: ") 

    return file_pointer
    
# Reads the file that is entered and returns a tuple
def read_file(fp):
    reader = csv.reader(fp)
    next(reader,None)
    my_tup_data = []
    for each_line in reader:
        name = str(each_line[0])
        rarity = int(each_line[1])
        element = str(each_line[2])
        weapon = str(each_line[3])
        region = str(each_line[4])

        
        if region == "":
            region = None

        my_tuple = (name,element,weapon,rarity,region)

        my_tup_data.append(my_tuple)

        
        
    return my_tup_data

# Retrieves the characters that match the given criteria
def get_characters_by_criterion (list_of_tuples, criteria, value):
    emp_list = []
    for each_line in list_of_tuples:    
        if criteria == ELEMENT and type(value) == str:
            if each_line[criteria] != None:
                if each_line[criteria].lower() == value.lower():
                    emp_list.append(each_line)

        if criteria == WEAPON and type(value) == str:
            if each_line[criteria] != None:
                if each_line[criteria].lower() == value.lower():
                    emp_list.append(each_line)

        if criteria == RARITY and type(value) == int:
            if each_line[criteria] != None:
                if each_line[criteria] == value:
                    emp_list.append(each_line)
        
        if criteria == REGION and type(value) == str:
            if each_line[criteria] != None:
                if each_line[criteria].lower() == value.lower():
                    emp_list.append(each_line)

    return emp_list

# Takes the parameter of the lsit of tuples from the read_file function       
def get_characters_by_criteria(master_list, element, weapon, rarity):
    char_list = []
    char_list = get_characters_by_criterion(master_list, ELEMENT, element)
    char_list = get_characters_by_criterion(char_list, WEAPON, weapon)
    char_list = get_characters_by_criterion(char_list, RARITY, rarity)

    return char_list

# retrieves all available regions into a list
def get_region_list(master_list):
    reg_list = []

    for i in master_list:
        if i[REGION] != None and i[REGION] not in reg_list:
            reg_list.append(i[REGION])

# Sorted region list     
    return sorted(reg_list)

# Creates a new list where the characters are sorted
def sort_characters (list_of_tuples):

    list_of_tuples = sorted(list_of_tuples)
    list_of_tuples = sorted(list_of_tuples, key=itemgetter(3), reverse = True)
    return list_of_tuples
    

# Displays characters with their information
def display_characters (list_of_tuples):
    if list_of_tuples == []:
        print('\nNothing to print.')

    else:
        print(HEADER_FORMAT.format("Character","Element","Weapon", "Rarity", "Region"))
        for i in list_of_tuples:
            if i[4] == None:
                print(ROW_FORMAT.format(i[0],i[1],i[2],i[3],"N/A"))
            else:
                print(ROW_FORMAT.format(i[0],i[1],i[2],i[3],i[4]))
        

# Prompts the user for the menu options
def get_option():
    menu_options = int(input(MENU))

    if menu_options >= 1 and menu_options <= 4:
        return menu_options
    
    else:
        print(INVALID_INPUT)
def main():
    fp = open_file()
    my_tup_data = read_file(fp)

    opt = 0

# while loop for the different options
    while opt != 4:
        opt = get_option()
        if opt == 1:
            print("\nRegions:")
            region = get_region_list(my_tup_data)
            print(", ".join(region)) 
            continue           

# If user enters option 2, the program will retrieve the criteria and value.
# Then the program will call a list of functions to sort and display the \n
# characters
# IF user enters an invalid input, a reprompt will occur
        if opt == 2:
            while True:
                try:
                    crit_prompt = int(input(CRITERIA_INPUT))
                    if crit_prompt >= 1 and crit_prompt <= 4:
                        if crit_prompt == 3:
                            val_inp = int(input(VALUE_INPUT))
                            break
                        else:
                            val_inp = input(VALUE_INPUT)
                            break
                    

                except:
                    print(INVALID_INPUT)
                    crit_prompt = int(input(CRITERIA_INPUT))

            
    
                
            list_crit = get_characters_by_criterion(my_tup_data, crit_prompt, val_inp)
            sort_crit = sort_characters(list_crit)
            display_characters(sort_crit)

            
# If user enters option 3, the program will retrieve the element, weapon, \n
# and rarity

# Then the program will turn the rarity input into an int. If it cant, \n
# an error 
# message will show anda reprompt

# Then the characters will be sorted and displayed
        if opt == 3:
            el_inp = input(ELEMENT_INPUT)
            weap_inp = input(WEAPON_INPUT)
            rar_inp = input(RARITY_INPUT)

            try:
                rar_inp = int(rar_inp)
            except:
                print(INVALID_INPUT)
                rar_inp = int(input(RARITY_INPUT))

            get_char = get_characters_by_criteria(my_tup_data,el_inp,weap_inp,rar_inp)
            sort_c = sort_characters(get_char)
            display_characters(sort_c)

# If user enters 4, the program will quit
        if opt == 4:
            quit()



# DO NOT CHANGE THESE TWO LINES
#These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__":
    main()
    
