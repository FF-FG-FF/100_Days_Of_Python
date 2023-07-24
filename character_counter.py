#Character Counter

user_string = input("Enter Your Sentence: ")
letter = input("Enter A Letter: ")

letter_occurence = 0

for i in range(len(user_string)):
    if user_string[i] == letter:
        letter_occurence += 1
        
print(f"The letter '{letter}' appears {letter_occurence} times")        