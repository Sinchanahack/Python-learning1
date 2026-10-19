#Reading a file
file = open("student.txt", "r")
contents = file.read()
print(contents)
file.close()


#Wrinting a file
file = open("Class.txt", "w")
file.write("Sinchana, \nprathi, \nsuhas")


#Exception handling

Name = input("name:")

try:
    Age = int(input("age:"))
    marks = []
    
    for i in range(1,6):
        mark = int(input(f"subject{i}:"))
        if mark <= 0 or mark >= 100:
            raise Exception("ValueError: Please Enter a valid input")
        marks.append(mark)
        if Age <= 16:
            raise Exception("ValueError: Please enter age above 16")

except Exception as e:
    print(f"{e}")

else:
    print(Name,"\n", Age,"\n", marks)
finally:
    print("Registration completed")
file.close()


