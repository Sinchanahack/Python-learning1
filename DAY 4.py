#Lists
#Ascessing of list
fruit = ['apple', 'grapes', 'orange', 'papaya']
print(fruit[1])

#Adding element
#1.append
fruit.append('mango')
print(fruit)

#2.insert
fruit.insert(1,'pineapple')
print(fruit)

#removing an element
#1.remove
fruit.remove('orange')
print(fruit)

#2.pop
fruit.pop()
print(fruit)

#3.clear
fruit.clear()
print(fruit)

#Slicing
fruit = ['apple', 'grapes', 'orange', 'papaya']
print(fruit[1:4])

#Common functions
print(len(fruit))

#Sorted list
length = [15, 2, 19, 7, 92]
length.sort()
print(length)

print(sum(length))

#Common method 
length = [15, 2, 19, 7, 92]
print(length.index(92))

print(length.count(2))

length.reverse()
print(length)