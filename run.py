# Write your code to expect a terminal of 80 characters wide and 24 rows high.

import gspread # for accessing Google Sheets
import time # for delays
import sys # For writing to terminal with effects
import os # For terminal clearing
import random # For Generating random strong passwords
import getch # Capture and record Keypresses
import re # For checking password strength
from colorama import Fore, Back, Style, init # Colors
from google.oauth2.service_account import Credentials # Creds
from consolemenu import * # Menu Generation
from consolemenu.items import * # Menu Item Generation
from prettytable import PrettyTable # Table Display
import pyhibp # Library for interacting with 'Have I Been Pwned'
from pyhibp import pwnedpasswords as pw # Library for interacting with 'Have I Been Pwned'

from pprint import pprint # Temp, for debugging

os.system("clear")
init(autoreset=True) # Colorama styling auto reset 

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('vault_guard_db')



pyhibp.set_user_agent(ua="Awesome application/0.0.1 (An awesome description)")
my_pass = '&5LZXuF8Yi#Q3t'
resp = pw.is_password_breached(password=my_pass)
if resp:
    print("Password breached!")
    print(f"The password {my_pass} was used {resp} time(s) before.")
else:
    print(f"The password {my_pass} is clean!.")


# Load specific worksheet
x = SHEET.worksheet('test')

# Get All data 
pprint(x.get_all_values())

# Print Data with PrettyTables
table = PrettyTable()
table.field_names = ["ID", "Service", "Username", "Password"]
for i in x.get_all_values()[1:]:
    table.add_row(i)
print(table)


# Menu Generation
title = Back.GREEN + " * Title * " + Style.RESET_ALL
subtitle = Fore.RED + Back.YELLOW + " * Subtitle * " + Style.RESET_ALL
menu = ConsoleMenu(title, subtitle)
f_item = FunctionItem("Option1", None)
s_item = FunctionItem("Option2", None)
menu.append_item(f_item)
menu.append_item(s_item)
menu.show()


# My own password star display function
passw = ''
print("Please Enter your password...")
while True:
    key = getch.getch()
    if key == '\n':
        break
    sys.stdout.write('*')
    sys.stdout.flush()
    passw += str(key)
print('\n')
print(passw)


# Get specific row
print('\n')
y = x.get_all_values()
for i in y:
    if i[1] == 'yahoo':
        print(i)

# Get specific column
print('\n')
pprint(x.col_values(4)[1:])
print('\n')

# Add new row
x.append_row(['test1', 'test2', 'test3', 'test4'])
pprint(x.get_all_values())
print('\n')

for i in range(10):
    sys.stdout.write('.')
    sys.stdout.flush()
    time.sleep(0.2)
os.system("clear")
print('CHECK ADDED ROW NOW...')

# Add waiting time
print('\n')
for i in range(25):
    sys.stdout.write('.')
    sys.stdout.flush()
    time.sleep(0.2)

# Delete specific row
print('\n')
print('Deleting last row...')
x.delete_rows(len(x.get_all_values()))
pprint(x.get_all_values())

# Create New Spreadsheet
new_username = 'new-test-user'
# SHEET.add_worksheet(title=new_username, rows=1000, cols=4)

# Raise Exception
try:
    exist = SHEET.worksheet('test')
except:
    print('User Database could not be found')

# Colour Options
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

# Password Strength Checker

# 1: Length, 2: Uppercase, 3: Lowercase, 4: Number, 5: Special Character

def strong_password(password):

    # 1: Length, 2: Uppercase, 3: Lowercase, 4: Number, 5: Special Character
    strong_pass = []
    strong_pass.append(len(password) >= 8)
    strong_pass.append(bool(re.search("[A-Z]", password)))
    strong_pass.append(bool(re.search("[a-z]", password)))
    strong_pass.append(bool(re.search("[0-9]", password)))
    strong_pass.append(bool(re.search(r'[!@#$%^&*()\[\]\-=_\\|;:,.<>?/~`"]', password)))

    # Write out Password Characteristics

    if all(strong_pass):
        print(Back.GREEN + ' PASSWORD IS STRONG \n')
    else:
        print(Back.RED + ' PASSWORD IS TOO WEAK \n')

    if strong_pass[0]:
        print(Back.GREEN + ' Password is at least 8 characters long ')
    else:
        print(Back.RED + ' Password needs to be at least 8 characters long ')

    if strong_pass[1]:
        print(Back.GREEN + ' Password contains an uppercase letter ')
    else:
        print(Back.RED + ' Password does not contain an uppercase letter ')


    if strong_pass[2]:
        print(Back.GREEN + ' Password contains a lowercase letter ')
    else:
        print(Back.RED + ' Password does not contain a lowercase letter ')


    if strong_pass[3]:
        print(Back.GREEN + ' Password contains a number letter ')
    else:
        print(Back.RED + ' Password does not contain a number letter ')

    if strong_pass[4]:
        print(Back.GREEN + ' Password contains a special character ')
    else:
        print(Back.RED + ' Password does not contain a special character ' + Style.RESET_ALL)  
        print('Please include any one of these:')
        print('!@#$%^&*()-_=[]|;:,.<>?/~`"')
    print(Style.RESET_ALL)
    return ''

# Random Password Generation
password_length = 5

p1 = [i for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
p2 = [i for i in 'abcdefghijklmnopqrstuvwxyz']
p3 = [i for i in '0123456789']
p4 = [i for i in '!@#$%^&*()-_=[]|;:,.<>?/~`"']
p5 = [p1, p2, p3, p4]

for i in range(3):
    new_password = ''
    for i in range(password_length):
        item = random.choice(p5)
        new_password += random.choice(item)
    print(' Password = ' + Fore.YELLOW + ' ' + new_password + ' ')
    print(Style.RESET_ALL)
    print(strong_password(new_password))







