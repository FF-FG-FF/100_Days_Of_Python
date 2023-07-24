#Dictionaries In Python, Mutable/Able To Change, but no duplicates allowed,We can add different data types

first_dict = {"name" : "John", "nationality" : "Canadian", "Job" : "Mechanic ","age" : 47, 
    "Healthy": True,
    "friends" : ["Carol","Adam","Josh","Matthew"]
}

Health_status = first_dict["Healthy"]

print(first_dict) #Prints Entire Dictionary
print(first_dict["name"]) #"Name" is the KEY
print(len(first_dict)) #Prints Lenght Of Dictionary
print(type(first_dict)) #prints the data type of first_dict
print(Health_status)

