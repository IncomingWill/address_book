# Title: Address Book Program
# Program created by William Schaeffer
# CPS 313
# P. 519, Exercise 8, Name and Email Addresses Program - Command Prompt
# 03.01.22

# This program will keep the names and email addresses in a dictionary as key-value pairs in a pickled file
    # the program will pickle the file every time it is edited, and unpickle it every time it is opened

# imports for functions

import sys, add_book_func, pickle, os.path

# Global Constants 
    # for menu choices
ADD = 1
CHANGE = 2
DELETE = 3
LOOKUP = 4
QUIT = 5

# Main Function

def main():
   
    #choice = 0                                             # initialize user choice
    
    eof = False                                             # to indicate end of file


    choice = sys.argv[1]
    name = sys.argv[2]

    if len(sys.argv) == 3:                                  # test number of arguments
        email = ""
    elif len(sys.argv) == 4:
        email = sys.argv[3]
    else:
        print('Incorrect number of arguments. Please reload program and try again')
        quit()

    if os.path.exists('address_book.pickle'):               # check to see if file exists, if it does, open as read and 
        address_file = open('address_book.pickle', 'rb')
        while not eof:
            try:
                email_addresses = pickle.load(address_file)

            except EOFError:                                # Set the flag to indicate the end of the file has been reached
                eof = True

    else:
        address_file = open('address_book.pickle', 'wb')    # create the .pickle if it doesn't exist
        email_addresses = {}                                # initialize empty dictionary for email addresses. key:value, name:email

    address_file.close()                                    # close the file

    #while choice != QUIT:                                  # PLEASE NOTE indentation retracted for COMMENTED OUT WHILE LOOP
        #choice = add_book_func.get_menu_choice()           # display choices and get choice from user
                                                            # not used in command line version
    if choice == 'add':
        add_book_func.add(email_addresses, name, email)
    elif choice == 'change':
        add_book_func.change(email_addresses, name, email)
    elif choice == 'delete':
        add_book_func.delete(email_addresses, name)
    elif choice == 'lookup':
        add_book_func.lookup(email_addresses, name)
    else:
        print('Invalid first argument. Ending program')
        quit()
            
    print('Pickling the email address dictionary, saving the file, and closing the file and program.')

    address_file = open('address_book.pickle', 'wb')        # reopen address_file

    pickle.dump(email_addresses, address_file)              # put pickled dictionary into address_file
    
    address_file.close()

main()                                                      # call main function

