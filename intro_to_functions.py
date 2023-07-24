#functions in python

#declaring/defining a function in python

def greetings():
    print("Hello User") #indents, tells the function what to do
    
greetings()   #calls the functions, or else it wont activate

#upgraded version of the greetings function
name = input("Type in your name: ") #asks for user input
def greetings_2(name):
    print(f"Welcome {name}")
greetings_2(name) 

#passing two parameters/arguments through a function
age = input("Enter Your Age: ")  #asks for user input
def greetings_3(name, age):
    print(f"Welcome {name}, {age} years old")
greetings_3(name,age)

#passing multiple parameters/arguments through a function 
names = ("carl","Bruce","Alexander","Adam")
def greetings_4(names):
    print(f"Welcome, {names}")
greetings_4(names)    


