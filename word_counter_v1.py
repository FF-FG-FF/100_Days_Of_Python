#Word Counter pt.1

sentence = input("Enter Your Sentence: ")

sentence_length = len(sentence)
spaces = 1

for i in range(sentence_length):
    if sentence[i] == " ":
        spaces += 1
        
   

print(sentence_length)
print(spaces)

print(f"The number of words in your sentence is '{spaces}' ")
