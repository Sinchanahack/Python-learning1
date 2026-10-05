#Level 5
#If-elif-else
#Check whether a number is positive, negative or zero 
num = int(input("Enter a number:"))
if num >=1:
    print("Number is positive")
elif num == 0:
    print("Number is zero")
else:
    print("Number is negative")


#Check whether a number is even or odd
number = int(input("Enter a number:"))
if number % 2 == 0:
    print("Even number")
else:
    print("Odd numbers")


#Print whether a person is eligible to vote
age = int(input("Enter your age:"))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")