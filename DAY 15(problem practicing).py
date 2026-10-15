#Functions
#create a function that prints hello welcome to python 

def great():
    print("Hello, Welcome to python!")
great()

#Create a function that takes your name and prints a welcome message

def welcome():
    name = "Sinchana"
    print(f"Hello {name}, Welcome to Python!")

welcome()


#Create a function that takes two numbers and prints their sum.

def sum():
    a = 10
    b = 20
    print(a+b)

sum()


#Create a function that takes a number and checks whether it is even or odd.

def num():
    n = int(input("Enter a number:"))
    if n % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
num()


#Create a function that takes two numbers and prints the larger number.

def number():
    
    x = int(input("Enter a first number:"))
    y = int(input("Enter a second number:"))

    if x > y:
        print("X is greater")
    elif y > x:
        print("Y is greater")
    else:
        print("Both are same")
number()


#Create a function that takes a list and finds the largest number

def list():

    my_list = [1, 2, 35, 75, 94, 37, 92, 23, 32, 47]
    print(max(my_list))

list()

#Create a function that takes a string and counts the vowels.
def string():
    
    Name = 'Sinchana'
    vowels = 0

    for letters in Name:
        if letters in "aeiou":
            vowels = vowels + 1
            print(vowels)

string()        

#Create a function that takes a number and calculates its square.
def square():
    numbers = int(input("Ente a number:"))
    square = numbers*numbers
    print(square)
square()

#Create a function that takes a student's name and marks and prints whether they passed.
def student(**students):
   
    for key,value in students.items():
        if value >= 35:
            print(f"{key} are passed")
        else:
            print(f"{key} are failed")
      
student_details = {"Sinchana": 89, "Pratiksha": 90, "Hitesh": 94, "Suhas": 65, "Kamala": 54, "Bhagya":73, "Ram": 32, "Rani": 29}
    
student(**student_details)