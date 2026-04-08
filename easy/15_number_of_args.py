# Q15 --Write a function that accepts any number of arguments (*args) and returns their average
def avg(*args): print(sum(args)/len(args))
n = []
i = 0
while i < 1:
    a = input("enter a number ans. y or n:")
    if (a == "y"):
        n.append(float(input("enter the number:")))
    else:
        break
m = tuple(n)
print(m)
avg(*m)
