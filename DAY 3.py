#String manipulation
#Common string operation
#concatination
First_name = "Sinchana"
Last_name = "M L"
Full_name = First_name + " " + Last_name
print(Full_name)

#Repitation
name = "sinchana!"
print(name*5)


#String methods
#upper case
name = "sinchana"
print(name.upper())

#lower case 
name = "SINCHANA"
print(name.lower())

#strip
name = "     Sinchana M      L"
print(name.strip())

#Replace 
name = "sinchu"
print(name.replace("sinchu", "sinchana"))


#Accessing a string
name = "Sinchana M L"
print(name[9])

#Slicing a string
name = "Sinchana"
print(name[:6])

#Escape sequence
print("Hello \n world")
print("Hello \t world")
print("Hello \\ world")

#Operators are symbols use to perform task 
#1.Assignment operator
x = 5
x += 5
x -= 5
x *= 5
x/= 5

#2.Comparision operator
a = 10 
b = 5
print(a>b) #Greater than
print(a<b) #Lesser than
print(a>=b) #Greater than or equal to 
print(a<=b) #Less than or equal to 
print(a==b) #Equal to 
print(a!=b) #Not equal to 

#3.Logical operator (AND, OR, NOT)
a = 10
b = 5
print(a>b and b<a) #AND means if both statement is true
print(a>b or b>a) #if one is true
print(not(a>b)) #if both the statement is true then it is false

#Membership operator
my_name = "Sinchana"
my_number = 1,2,3,4
print("i" in my_name)
print(3 in my_number)

#Bitwise operator 


#Lists   it is a collection of items which are ordered, mutable
