#for loops in python

#both for loops do the same thing, print all the letters in the word
word = input("Enter A Word: ")

for letter in word: #you dont have to use 'letter' you can name it whatever you want
    print(letter)
    
print("\n") #prints a newline
 
for i in range(len(word)):
    print(word[i])
    
word_bank = ["bank","movie","crown","sword","seas"]  

for values in word_bank:  #you dont have to use 'word_bank' you can name it whatever you want
    print(values)
    
#for loop that prints all the numbers    
number = int(input("Enter A number: "))
for i in range(number): #code starts counting at zero
    print(i)
else: #executes after the loop finishes
    print("The for loop is done")
    
#break #stops the program, used in loops to stop them    
    