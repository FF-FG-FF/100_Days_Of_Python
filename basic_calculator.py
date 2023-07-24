#building a basic CALCULATOR

num1 = float(input("Enter Your first Number: "))
operator = input("Enter Your operator sign ( +, - , *, / ): ")
num2 = float(input("Enter Your Second Number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    if num1 == 0 or num2 == 0:
        print("cannot divide by a zero")
    else:    
        print(num1 / num2)
else:
    print("Invaliid Operator Entered")