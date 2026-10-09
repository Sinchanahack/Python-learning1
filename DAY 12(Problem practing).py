#if elif else
#Take a marks and print 90+ → A, 75–89 → B, 50–74 → C, below 50 → Fail

marks = int(input("Enter a student marks:"))

if marks >= 90:
    print("Grade: A")
elif marks <= 89 and marks >= 75:
    print("Grade: B")
elif marks <= 74 and marks >= 50:
    print("Grade: C")
else:
    print("Fail")

#Find the largest of two numbers
a = int(input("Enter the number:"))
b = int(input("Enter the number:"))
if a > b:
    print("A is greater")
else: 
    print("B is greater")

#Find the largest of three numbers
d = int(input("Enter the number:"))
e = int(input("Enter the number:"))
f = int(input("Enter the number:"))
if d > e and d > f:
    print("D is greater")
elif e > d and e > f:
    print("E is greater")
else:
    print("F is greater")

#Check whether a number is divisible by both 3 and 5.
number = int(input("Enter a number:"))

if number%3 == 0 and number%5 ==0:
    print("Number is divided by both 3 or 5")
elif number%3 == 0 :
    print("Number is divided by 3")
elif number%5 == 0:
    print("Number is divided by 5")
else:
    print("Number is not divided by 3 or 5")


#Create a simple login program using username and password
username = input("Enter a username:")
password = int(input("Enter a password"))

if username == "Sinchana" and password == 7585:
    print("Login succesfully")
else:
    print("Username or Password is incorrect")
