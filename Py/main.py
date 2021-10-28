#Imports everything from the users.py file .
from users import *

#Sets a while loop so the programm repeats itself on false login.
while True:

    #Create variables for the users input.
    login_username = input("Username: ")
    login_password = input("Password: ")

    #Compares input with the username_passwords dictionary from the users.py file.
    #If username and pw get a match it prints success and ask the user if he wants to restart the Programm.
    if username_password.get(login_username) == login_password:
        print("Login successfull.")
        x = input("Again? (y/n): ")
        if x == ("n"):
            break
        
    #If login false it prints failed and starts over bc the while loop is still true.
    else:
        print("Login failed.")

            
    

