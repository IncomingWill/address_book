# Title: Address Book Program
# Program created by William Schaeffer
# CPS 313
# P. 519, Exercise 8, Name and Email Addresses Program - Command Prompt
# 03.01.22

import pickle

# Global Constants 
    # for menu choices
ADD = 1
CHANGE = 2
DELETE = 3
LOOKUP = 4
QUIT = 5

def get_menu_choice():
    print()
    print('Address Book Program')
    print('#===================#')
    print('1. Add email address')
    print('2. Change email address')
    print('3. Delete email address')
    print('4. Look Up email address')
    print('5. Quit Program')
    print()

    choice = int(input('Enter your choice: '))

    while choice < ADD or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    return choice

def add(email_addresses, name, email):
    
    #name = input('Enter a name: ')
    #email = input('Enter an email address: ')

    if name not in email_addresses:
        email_addresses[name] = email
    else:
        print('That entry already exists, cannot have duplicates.')

    print(f'Added email address for {name} as {email_addresses.get(name)}')

def change(email_addresses, name, email):
    
    #name = input('Enter a name: ')

    if name in email_addresses:
        #email = input('Enter a new email address: ')

        email_addresses[name] = email
    else:
        print('That name is not found.')

    print(f'Changed email address for {name} to {email_addresses.get(name)}')


def delete(email_addresses, name):
    #name = input('Enter a name: ')

    if name in email_addresses:
        del email_addresses[name]
    else:
        print('That name is not found.')

    print(f'Deleted email address for {name}')



def lookup(email_addresses, name):
    #name = input('Enter a name: ')

    print(f'Email address for {name} is {email_addresses.get(name, "not found.")}')