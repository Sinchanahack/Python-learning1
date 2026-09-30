#While loop

#print numbers from 1 to 10
i=1
while i<=10:
    print(i)
    i+= 1


#Print numbers from 10 t0 1
i = 10

while i<=10 and i>=1:
    print(i)
    i-= 1


#Print even nuber from 1 tp 20
i = 1

while i<=20:
    if i%2 == 0:
        print(i)
    i += 1


#print odd number form 1-20
i = 1

while i<=20:
    if i%2 != 0:
        print(i)
    i += 1

#Multiple of 3
i = 0
j = int(input("Enter a number:"))

while i <= 100:
    if i%j == 0:
        print(i)
    i+=1


#Sum of numbers from 1 t0 N
i = 1
N = int(input("Enter the N number"))

sum = 0

while i<= N:
    sum = sum + i
    print(sum)
    i+=1


#count from 1 to N and find the sum
i = 1
N = int(input("Enter the N number"))

sum = 0 
count = 0

while i <= N:
    count = count + 1
    
    sum = sum+count 
    print(sum)
    i+=1
