#word replacement program, replaces words in a sentence provided by the user

sentence = input("Type In Your sentence: ")

choice = input("Do you want to modify Your sentence: (Y / N)")

if choice == "y" or choice == "y":
    word1_change = input("What word do you  want to change from the sentence: ")
    word2_replace = input("What do you want to replace it with: ")
    print(sentence.replace(word1_change, word2_replace))
elif choice == "n" or choice == "N":
    print(f"This is your sentence '{sentence}'")
else:
    print("Invalid input Try Again")



