# Q9 -- Find all prime numbers between 1 and N (user gives N)
n = int(input("enter number:"))
for i in  range(2, n+1):
    prime = True

    for j in range(2, i):
        if i % j == 0:
            prime = False
            break
    
    if prime:
        print(i)
