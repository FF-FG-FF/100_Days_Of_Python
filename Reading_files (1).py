#reads a  file program

def read_file(file_name):
    try:
        with open(file_name, "r")as file: #opens the file in 'r' reading mode 
            contents = file.read() #reads the file and stores it as a string (contents)
            return contents #returns contents to the main() function
    except FileNotFoundError: #if this FileNotFoundError is found it runs the following code
        print("File Not Found, Try Again")
        return None
        
def main():
    file_name = input("Enter Your Files Name: ")
    file_contents = read_file(file_name)
    
    if file_contents:
        print("\n Contents Of The File: ")
        print(file_contents)
        
if __name__ == "__main__": #allows you to determine if the current Python script is being run
    main()              #as the main program (directly executed) or if it is being imported as a module into another script.
        
            