import random

choice = input("Do you Want To Play Multiplayer ( Y / N ) : ")

if choice == "y" or choice == "Y":
    a = int(input("Enter Your first Number: "))
    b = int(input("Enter Your Second Number: "))
    target_number = random.randint(a,b)
if choice == "n" or choice == "N":
    a = 1 
    b = 100
    target_number = random.randint(a,b)
    
attempts = 0
    
while True:
    guess = int(input(f"Guess a number between {a} and {b}: "))
    attempts += 1
    
    if guess > target_number:
        print(f"Your guess '{guess}' is too high")
    elif guess < target_number:
        print(f"Your Guess '{guess}' is too low")
    else:
        print(f"Congrats You guessed The Number {target_number} in {attempts} attempts")
        break