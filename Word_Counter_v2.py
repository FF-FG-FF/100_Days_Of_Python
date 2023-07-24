#word counter, by counting the spaces were able to count the words in a sentence

sentence = input("Enter Your sentence: ")

#removes the beggining or ending spaces using the strip function
sentence = sentence.strip()

spaces = 1 #we start at 1 , to count for the space not included before the sentence starts

#counts the number of spaces between words
for char in(sentence):
    if char == " ": #char == Character
        spaces += 1
        
print(f"Number Of Characters: {len(sentence)}")
print(f"Number Of Words: {spaces}")
