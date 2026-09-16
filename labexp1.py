import math

print("1. Find the Area of a Circle")
print("2. Check for a Leap Year")
print("3. Find the Largest of Three Numbers")

choice = input("\nEnter your choice (1, 2, or 3): ")

if choice == '1':
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * (radius ** 2)
    print(f"Result: The area of the circle is {area:.2f}")

elif choice == '2':
    year = int(input("Enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"Result: {year} is a leap year.")
    else:
        print(f"Result: {year} is not a leap year.")

elif choice == '3':
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    if num1 >= num2 and num1 >= num3:
        largest = num1
    elif num2 >= num1 and num2 >= num3:
        largest = num2
    else:
        largest = num3
        
    print(f"Result: The largest number is {largest}")

else:
    print("Invalid choice. Please run the program again and enter 1, 2, or 3.")