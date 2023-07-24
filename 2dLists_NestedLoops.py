#2d lists and nested loops

storage = [    #this is a 2d list because it has rows and columns/ a list within a list
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ] 
    
print(storage)  #prints entire 2d list
print(storage[0]) #prints the first value
print(storage[0][2]) #prints the second value of the first value
print("\n") #prints a newline

#nested list , a for loop inside a for loop, looping through a loop
for values in storage:
    for row in values:
        print(row)