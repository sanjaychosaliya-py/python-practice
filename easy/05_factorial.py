# Q5 — Write a function that returns the factorial of a number using both loop and recursion
def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print("the factorial of the number:", n, "is :", fact)
def fact_recur(n):
    if (n == 0 or n== 1):
        return 1
    else:
        return n*fact_recur(n-1)
n = int(input("enter the number n"))
a = int(input("chhose the method 1. for normal\n2. for recusion"))
if (a == 1):
    fact(n)
elif (a == 2):
    print(fact_recur(n))
else:
    print("you are selected wrong number")
