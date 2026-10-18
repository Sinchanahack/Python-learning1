#Exception handling
#Safe division

a = int(input("Enter a first number:"))
b = int(input("Enter a second number:"))

try:
    print(a/b)
except Exception as e:
    print(f"Not divided by zero!!{e}")
finally:
    print("Program Ended")

#Age input validation
age = input("Enter your age:")

try:
    print(int(age))
except:
    print("Value Error: Please enter a valid input")
finally:
    print("Program ended")


#Multiple exceptions
try:
    num1 = int(input("Enter a number:"))
    num2 = int(input("Enter a number:"))
    num = num1/num2
    print(num)
except ZeroDivisionError:
    print("ZeroDivisionError:Cannot divided by zero")
except ValueError:
    print("Value Error: Please enter valid input!!")
else:
    print(num)
finally:
    print("PROGRAM ENDED")


#Student marks calculator

marks = [75, 58, -15, 148, 68]

total_marks = sum(marks)

try:
    for mark in marks:
        if mark <= 0 or mark >= 100:
            raise Exception("Invalid: Marks are from 0 to 100")
        print(mark)
    print(total_marks)

except Exception as e:
    print(f"{e}")

#Student Register system
students = {
    input("Name:"),
    int(input("Age:")),
    int(input("marks:"))
}
try:
    for student in students:
        if age <= 16 and mark <= 0 or mark >= 100:
            raise Exception("ValueError: Please Enter a valid input")
except Exception as e:
    print(f"{e}")
