# Q14 -- Write a function that takes a number and returns True if it is perfect number (sum of divisors equals number, e.g. 6 = 1+2+3)
n = int(input("enter the number n:"))
i = 1
sum = 0
while i < n:
    if n % i == 0:
        sum += i
    i += 1
if(sum == n):
    print(n,"it is perfect number")
else:
    print("it is not a perfect number")
