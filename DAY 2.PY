#LEVEL 1
#Student details
name = "Sinchana" 
age = 18
branch = "Computer science and engineering"
college = "Ghousia college of engineering"
print(name)
print(age)
print(branch)
print(college)


#Basic Data Types
name = "sinchana"
age = 18.9
year = 2026
engineering = True or False
print(type(name))
print(type(age))
print(type(year))
print(type(engineering))


#Simple calculation
a = 10
b = 5
print("Addition:", a+b)
print("Substraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)


#Rectangle
length = int(input("Enter a number:"))
breadth = int(input("Enter a number:"))
area = length * breadth
perimeter = 2*(length+breadth)
print("Area of the rectangle is", area)
print("Area of th e perimeter is", perimeter)


#Temperature conversion
C = int(input("Enter the celsius temperature"))
F = (C * (9/5))+32
print("Fahrenheit  temperature", F)


#Add two numbers 
a = int(input("Enter a first number:"))
b = int(input("Enter a second number:"))
print("The added two number is", a+b)


#Student marks
subject_1 = int(input("Enter a marks of 1st subject:"))
subject_2 = int(input("Enter a marks of 2nd subject:"))
subject_3 = int(input("Enter a marks of 3rd subject:"))
Total = subject_1 + subject_2 + subject_3
average = Total*100/300.00
print("Total of all three subjects:", Total)
print("Average:", average)


#Simpele interest
P = int(input("Enter the principle:")) #the original amount
R = int(input("Enter the rate:")) #Rate of intrest
T = int(input("Enter the time of the interest:"))
Simple_interest = (P*R*T)/100
print("The interest is", Simple_interest)