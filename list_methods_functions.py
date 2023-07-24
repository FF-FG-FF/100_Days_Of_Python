#list Methods/functions

list1 = [1,2,3,4,5]
list2 = ["banana","apples","mangos","oranges","apples"]

#different way to print list1 and list2 together
print(list1+list2)

#prints list1 and list 2 together
list1.extend(list2)
print(list1)

#add an item to the list
list2.append("cherry")
print(list2)

#tracks length of list
print(len(list2))

#removes an item from the list
list2.remove("banana")
print(list2)

#clears all values in a list
list1.clear()
print(list1)

#gets index number of an item in the list
print(list2.index("mangos"))

#counts the number of times an item appears on the list 
print(list2.count("apples"))

#prints the list in ascending order
list3 = [3,5,1,2,4]
list3.sort()
print(list3)

#prints the list in reverse 
list2.reverse()
print(list2)

#duplicating a list 
list4 = list3.copy()
print(list4)

#removes a value from the list using an index value and the 'pop' function  
list2.pop(2)
print(list2)

#deletes a value from the list using the 'delete' function 
del list2[0]
print(list2)

#deletes an entire list (its not going to be in our code anymore)
del list4