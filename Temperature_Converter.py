#Temperature Converter

print("Hello Welcome To The Temperature Converter")
choice = input("Do you have your Temperature in celsius or farenheit ( C / F ): ")

if choice == "c" or choice == "C":
    temp = float(input("Enter The Temperature: "))
    new_temp = (temp * 1.8) + 32
    print(f"Your New Temperature is '{new_temp}' farenheit")
elif choice == "f" or choice == "F":
    temp = float(input("Enter The Temperature: "))
    new_temp = (temp - 32) * (5/9)
    print(f"Your New Temperature is '{new_temp}' Celsius ")
    