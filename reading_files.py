#reading files in python    

text_file = open("sample.txt","r") #opens another file called "sample.txt" the r is for reading only

text_file = open("sample.txt","w") #opens another file called "sample.txt" the w says we want to edit this file 

text_file = open("sample.txt","a") #opens another file called "sample.txt" the a means we want to append/add to the file 

text_file = open("sample.txt","r+") #opens another file called "sample.txt" the r+ means we want to do both reading and editing 

text_file.close #make sure to close the file everytime you open it

print(text_file.readlines())#prints all the lines of our text file 

print(text_file.readlines()[0]) #prints the first line of our text_file(sample.txt)

