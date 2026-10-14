#Dictionaries
# Create a student dictttionary containing name, age, branch, marks 

student_details =  {'name': 'Sinchana', 'age': 18, 'branch': 'Computer science and engineering', 'marks': 88}
print(student_details)

#Access and pritnt individaual values
student_details =  {'name': 'Sinchana', 'age': 18, 'branch': 'Computer science and engineering', 'marks': 88}
print(student_details['name'])
print(student_details['age'])
print(student_details['branch'])
print(student_details['marks'])

#Add a new key value pair
student_details =  {'name': 'Sinchana', 'age': 18, 'branch': 'Computer science and engineering', 'marks': 88}
student_details['CGPA']=8.8
print(student_details)

#Change an existing value
student_details['name']= 'Sinchana M L'
print(student_details)

#Delete a key value pair
student_details.pop('CGPA')
print(student_details)

#Create dictionary that has 5 suject and marks
student_marks = {"Maths": 73, "Pysics": 79, "c programing": 91, "c programming lab": 94, "Building science and mechanics": 87}
print(student_marks)

#Find the marks of a particular subject

print(student_marks["c programming lab"])

#Check whether a student marks is above 40
student_marks = {"Maths": 73, "Pysics": 79, "c programing": 91, "c programming lab": 94, "Building science and mechanics": 87}

if student_marks["Building science and mechanics"] >= 40:
    print("Student is passed")
else:
    print("Student is failed")


#Create a food meanu dictionary and print the prince of a selcted items 
meanu = {
    "Dosa": 50,
    "Idle": 30,
    "Vada": 10,
    "Pizza": 200,
    "Burger": 150,
    "Curd Rice": 60 
}
print(meanu["Dosa"])
print(meanu["Pizza"])
print(meanu["Curd Rice"])

sum = 0 
sum = sum + meanu["Dosa"] + meanu["Pizza"] + meanu["Curd Rice"]#calculated the sum of prince
print("\n",sum)

#Create a dictionary containing 5 peoples name and their age and print the dictionary
peoples_details = {"Jayanna": 80, "Puttamma": 75, "Lokeshappa": 60, "Kamalamma": 50, "Shashi": 48, "Bhagya": 42, "Sinchu": 18, "Prathi": 16}
print(peoples_details)