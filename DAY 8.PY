#For loop

#print number from 1 to 10
for i in range(1,11):
    print(i)

#Print a even number 
for i in range(2,21,2):
    print(i)


#Print odd numbers from 1 to 20 
for i in range(1,20,2):
    print(i)


#print number from 10 to 1
for i in range(10, 0,-1):
    print(i, end=" ")


#Print number from 20 to 1 even numbers
for i in range(20, 1, -2):
    print(i)


#Multiplication table
for i in range(2,5):
    for j in range(1,11):
        print(f"{i}x{j} = {i*j}")
    