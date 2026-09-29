#if-elif-else

hospital = "Multispecality"

if hospital == "Heart Patient":
    print("Hospital is only for heart patient")
else:
    print("Sorry!, only for heart patient")



#Sugar calculation
Sugar = int(input("Enter the sugar rate:"))

if Sugar < 85:
    print("Low Sugar")
elif Sugar > 135:
    print("High Sugar")
else:
    print("Normal sugar rate")



your_food = input("Enter your favourite food:")
hostel_food = input("Enter tuesdays hostel food:")

if your_food == "Dosa" and  hostel_food == "Dosa":
    print("Ohh!, my favourite food")

elif your_food != "Dosa" and hostel_food == "Dosa":
    print("No, its not my favourite food")

else:
    print("Ayoo tomato bath haa")
