#Tuple
#Create a tuple containing 5 subjects and print the third subject
subject = ('Kannada', 'English', 'Hindi', 'Maths', 'Science')
print(subject[2])

#Find the length of tuple
subject = ('Kannada', 'English', 'Hindi', 'Maths', 'Science')
print(len(subject))

#Convert a list into tuple
subject = ['Kannada', 'English', 'Hindi', 'Maths', 'Science']
print(tuple(subject))

#Convert tuple into a list
subject = ('Kannada', 'English', 'Hindi', 'Maths', 'Science')
print(list(subject))

#Sets
#Create a sets containing 5 element
my_sets = {'Kannada', 'English', 'Hindi', 'Maths', 'Science'}
print(my_sets)

#Add an element to a sets
my_sets = {'Kannada', 'English', 'Hindi', 'Maths', 'Science'}
my_sets.add('Social')
print(my_sets)

#Remove an element form a set
my_sets.remove('Hindi')
print(my_sets)

#Create two sets and find their union, intersection, and difference
a = {1, 6, 3, 9, 2, 5, 8}
b = {6, 9, 3, 13, 5, 1, 18}
print(a | b) #union
print(a & b) #intersection
print(a-b) #Difference

#swap two variables
c = 10
d = 5
print(c,d)
temp = c
c = d
d = temp
print(c,d)