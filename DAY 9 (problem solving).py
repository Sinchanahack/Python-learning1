#Basics (Level 1)

#Store your name, age, and branch in variables and print
name = "Sinchana M L"
age = 18
branch = "Computer science and Engineering"

print(name,",", age,",", branch)

#Take two number print sum, difference, multiplication and division
a = 10
b = 2

print("Addition:", a+b)
print("Substraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)


#Find the area of rectangle
l = 10
b = 8
area = l*b

print("Area of rectangle:", area)


#convert a number form string to integer and print its type 
a = "10"
b = int("28")

print(type(a))
print(type(b))


#Take a student marks card and calculate the 3 average subjects
kannada = int(input("Enter kannada marks:"))
english = int(input("Enter english marks:"))
hindi = int(input("Enter hindi marks:"))

Total = kannada + english + hindi
print(Total)

Average = (Total*100)/300
print(Average)


#Check the data type of 5 different variable
a = "Sinchana"
b = 10
c = 5.2
d = True or False
e = ["sinchu", "Prathi", "Hithu", "Suhas"]

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


#Take a number and calculate the square and cube
a = int(input("Enter a number"))

square = a*a
cube = a*a*a

print("Square:",square, "Cube:", cube)


#Swap a two variable
i = int(input("Enter a first number:"))
j = int(input("Enter a second number:"))

temp = i
i = j 
j = temp

print("After swapping",i , j)