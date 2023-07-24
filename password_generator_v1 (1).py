#random password generator
import random

password_length = int(input("Enter The Length Of The Password: "))
password_bank = []



ask_uppercase = input("Do You Want Uppercase Letters: ( Y / N ) ")
ask_lowercase = input("Do You Want Lowercase Letters: ( Y / N ) ")
ask_numbers = input("Do You Want Numbers: ( Y / N ) ")
ask_characters = input("Do You Want Special Characters: ( Y / N ) ")

if ask_uppercase == "y" or ask_uppercase == "Y":
    Uppercase_bank = ["A","B","C","D","E","F","G","H","I"] #adds Uppercase Characters to the password_bank array
    password_bank.extend(Uppercase_bank)
    
if ask_lowercase == "y" or ask_lowercase == "Y":
    Lowercase_bank = ["a","b","c","d","e","f","g","h","i"] #adds Lowercase Characters to the password_bank array
    password_bank.extend(Lowercase_bank)
    
if ask_numbers == "y" or ask_numbers == "Y":
    Number_bank = ["1","2","3","4","5","6","7","8","9","0"] #adds Number Characters to the password_bank array
    password_bank.extend(Number_bank)
    
if ask_characters == "y" or ask_characters == "Y":
    Character_bank = ["!","@","#","$","%","^","&","*","?"] #adds Special Characters to the password_bank array
    password_bank.extend(Character_bank)
    

random.shuffle(password_bank) #shuffles the password_bank array


for i in range(password_length):
    password = " ".join(password_bank[i])
    print(password,end = "")  #instead of printing a newline , it prints on the same line
    