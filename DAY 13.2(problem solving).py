#for loop
#Print numbers from 1 to 20

for i in range(1,11):
    print(i, end = " ")
    i+=1


#Print all odd numbers from 1 to 20

for j in range(1,21):
    if j%2 != 0:
        print(j)
    j+=1


#Print the multiplication table of any number
n = int(input("Enter a number:"))
for a in range(1,11):
    print(f"{n}X{a}=",n*a)
    a+=1


#Find the sum of numbers from 1 to 100
sum = 0
for b in range(1,101):
    sum = sum + b
print(sum)


#Print each character of a string
charector = "Sinchana"

for index, char in enumerate(charector):
    print(char*(index+1))


#Print vowels are in a string.

name = input("Enter a name:")

for vowels in name:
    if vowels in 'aeiou':
        print(vowels)  

#Find the largest number in a list
my_list = [12, 3, 46 , 67, 98, 45, 200 , 350]

for num in my_list:
    print(max(my_list))
    break

#Count how many times a particular number occurs in a list
my_list1 = [1,2,4,5,6,7,8,9,0,9,8,6,5,4,3,3,4,6,7,8,89,9,876,54,3,45678,765,43,]

count = 0
 
for num in my_list1:
    if num == 9:
        count = count + 1
        print(count)