#lists in python, 

#constructed two lists, the first one has brackets and the second one has the ist constructor
countries = ["United Kingdom", "Ghana", "Nigeria", "Australia","New Zealand"]
countries_v2 = list(("United Kingdom", "Ghana", "Nigeria", "Australia","New Zealand"))

print(countries)
print(countries_v2)

#gets the first attribute from the list called countries
print("This is the first Value In The list")
print(countries[0])

#gets the second letter from the fourth word "Australia"
print(countries[3][1])

#excluding items from list, starts at 1 and goes to the end
print(countries[1:])

#range,only displays the range provided
print(countries[1:4])

#adding a value to the list
countries.append("Norway")
print(countries)

#getting the length of a list
print(len(countries))

#changing the value of an item in the list
countries[0] = "United States"
print(countries)

#getting the last value of the list
print(countries[-1])

#starting at the front of the list is positive,counting from the end is negative

#gets the second to last value of the list
print(countries[-2])

#getting the type of the list
print(type(countries))

#difference using the type function
name = "Jimmy John"
print(type(name))
number = 619
print(type(number))

