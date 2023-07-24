#palindrome checker

user_string = input("Enter Your Text: ")

# Uses string slicing to reverse the string
reversed_string = user_string[::-1]

if user_string == reversed_string:
    print(f"'{user_string}' is  a palindrome")
else:
    print(f"'{user_string}' is not a palindrome")
    