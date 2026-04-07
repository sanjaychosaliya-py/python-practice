# Q2 -- Take a list of numbers from user input and find the largest and smallest without using built-in min/max
list = []
i = 0
while i > -1:
    x = input("want to add:(give ans in y or n)")
    if (x == "y"):
        list.append(int(input("enter the number")))
    elif( x == "n"):
        break
    else:
        break
greatest = list[0]
smallest = list[0]
for i in list:
    if greatest < i:
        greatest = i
    if smallest > i:
        smallest = i
print("this is greatest", greatest)
print("this is smallest", smallest)
