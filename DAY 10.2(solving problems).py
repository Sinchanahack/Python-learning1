#Level 3 (Lists)
#Creat a frrit of 5 list and print it
fruit = ['Apple', 'Orange', 'Grapes', 'Banana', 'Mango']
print(fruit)

#print the first and last elements
fruit = ['Apple', 'Orange', 'Grapes', 'Banana', 'Mango']
print(fruit[0])
print(fruit[4])

#Add a few fruit to a list 
fruit = ['Apple', 'Orange', 'Grapes', 'Banana', 'Mango']
fruit.append('Pineapple')
print(fruit)

#Remove one fruit
fruit.remove('Grapes')
print(fruit)

#Change the 3rd element
fruit[2] = 'Watermaleon'
print(fruit)


#Find the length of the list
print(len(fruit))


#create a list of numbers and find sum
a = [1, 2, 3, 4, 5, 6, 7, 8]
print(sum(a))


#Create a list containing duplicate numbers and remove duplicates using a set.
a = [1, 2, 3, 4, 5, 6, 7, 8]
a.remove(5)
print(a)