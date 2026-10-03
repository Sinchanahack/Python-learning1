#Level 2 - Strings
#Take your first name and last name combine them
first_name = "Sinchana"
last_name = "M L"
Name = first_name + last_name
print(Name)

#print the length of string 
name = "Sinchana"
print(len(name))

#Convert a string to uppercase and lowercase
name = "siNcHaNa M l"
print(name.upper())
print(name.lower())

#Remove extra space using strip()
name = " Si n  c  ha na"
print(name.strip())

#Replace one world in a sentence with another
intrested = "I am intrested in AI"
print(intrested.replace("AI", "Data Science"))


#Print first, last and middle charector of string
word = "Computer Science"
print(word[0])
print(word[7])
print(word[-1])


#Use slicing to print first 3 charectors last 3 charectors reverse the string
branch = "Computer Science and Engineering"
print(branch[0:3])
print(branch[-4:-1])
print(branch[::-1])


#Take a name and print Hello sinchana! using f-string
name = "Sinchana!"
print(f"Hello {name}")