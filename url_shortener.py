import string
import random

url_storage = {}  # creates an empty dictionary called 'url_storage'

def generate_short_url():
    characters = string.ascii_letters + string.digits #stores all letters and numbers in 'characters'
    short_url = ''.join(random.choices(characters, k=6)) #selects 6(k = 6) random(random.choices() ) letters/numbers from 'characters'
    return short_url

def shorten_url(long_url):
    short_url = generate_short_url() #calls for the 'generate_short_url' function
    url_storage[short_url] = long_url #stores the urls in the dictionary and makes 'short_url' the key and 'long_url' the value
    return short_url

def access_short_url(short_url):
    long_url = url_storage.get(short_url) # uses .get() function, and short_url as the key to find the long_url
    return long_url

def main():
    while True:
        print("1. Shorten URL")
        print("2. Access shortened URL")
        print("3. Exit")
        choice = int(input("Navigate The Menu Using (1/2/3): "))

        if choice == 1:
            long_url = input("Enter the long URL to shorten: ")
            short_url = shorten_url(long_url) #calls for the shorten_url(long_url) function
            print(f"Shortened URL: http://short.url/{short_url}")

        elif choice == 2:
            short_url = input("Enter the shortened URL: ")
            long_url = access_short_url(short_url) #calls for the access_short_url(short_url) function
            if long_url:
                print(f"You are being redirected to: {long_url}")
            else:
                print("Invalid short URL. Please check the URL and try again.")

        elif choice == 3:
            print("You Have Exited The URL Shortener.")
            break

        else:
            print("Invalid choice. Please enter a valid option (1/2/3).")

if __name__ == "__main__": #allows you to determine if the current Python script is being run             
    main() #as the main program (directly executed) or if it is being imported as a module into another script.
