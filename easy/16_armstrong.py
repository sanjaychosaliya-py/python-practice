n = input("enter the number n:")
sum = 0
for i in n:
    m = int(i) ** 3 
    sum += m
if (sum == int(n)):
    print("it is armstrong number")
else:
    print("not armstrong number")
print(sum)
