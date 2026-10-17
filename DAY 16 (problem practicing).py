#Student result 
student_details = {'Sinchana': 88, 'Rani': 34, 'Raju': 83, 'Ramu': 23, 'Sannu': 50, 'Manga': 75}

for keys, values in student_details.items():
    if values > 35:
        print(f"{keys} is passed")
    else:
        print(f"{keys} is failed")


#Number Analyzer

number = int(input("Enter a number:"))

if number % 2 == 0:
    if number > 1:
        print(f"{number} is even and positive")
    elif number < -1:
        print(f"{number} is even and negative")
    else:
        print(f"{number} is zero")
else:
    if number > 1:
        print(f"{number} is odd and positve")
    elif number < -1:
        print(f"{number} is odd and negative")
    else:
        print(f"{number} is zero")

count = len(str(abs(number)))

print(count)
