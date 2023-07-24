#random password generator
import random
import string

password_length = int(input("Enter The Length Of The Password: "))
password_bank = [] #stores all Characters



ask_uppercase = input("Do You Want Uppercase Letters: ( Y / N ) ")
ask_lowercase = input("Do You Want Lowercase Letters: ( Y / N ) ")
ask_numbers = input("Do You Want Numbers: ( Y / N ) ")
ask_characters = input("Do You Want Special Characters: ( Y / N ) ")

if ask_uppercase == "y" or ask_uppercase == "Y":
     password_bank += string.ascii_uppercase #adds all Uppercase Characters to the password_bank array
    
if ask_lowercase == "y" or ask_lowercase == "Y":
    password_bank += string.ascii_lowercase #adds all Lowercase Characters to the password_bank array
    
if ask_numbers == "y" or ask_numbers == "Y": 
     password_bank += string.digits ##adds all Number Characters to the password_bank array
    
if ask_characters == "y" or ask_characters == "Y":
     password_bank += string.punctuation #adds all Special Characters to the password_bank array
    

random.shuffle(password_bank)


for i in range(password_length):
    password = " ".join(password_bank[i]) 
    print(password,end = "") #instead of printing a newline , it prints on the same line
    