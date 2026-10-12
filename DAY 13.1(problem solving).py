#While loop
#Print numbers from 1 to 10.
n = 1
while n <= 10:
    print(n, end = " ")
    n+=1

#Print numbers from 10 to 1.
i = 10
while i >= 1:
    print("\n", i, end = "  " )
    i-=1

#Print all even numbers from 1 to 20.
j = 1
while j <= 20:
    if j%2 == 0:
        print(j)
    j+=1

#Print all odd numbers form 1 to 20
k = 1
while k <= 20:
    if k%2 != 0:
        print(k, end= " ")
    k+=1

#Find the sum of numbers from 1 to 10.
a = 1

Sum = 0 

while a <= 10:
    Sum = Sum + a
    print(Sum)
    a+=1

#Print the multiplication table of a number
num = 1
number = int(input("Enter a number:"))

while num <= 10:
    print(f"{number} X {num} = ", number*num)
    num+=1

#Count the digits in a number
m = 123454

count = 0

while m>0:
    m = m//10
    count = count+1
    print(count)

#Reverse a number
z = 12112007
reverse = 0

while z>0:
    reverse = str(z)[::-1]
    print(reverse)
    break

#Keep asking the user for a number until they enter 0
digit = int(input("Enter a number:"))

while digit == 0:
    print(f"{digit} is taken succesfully")
    break