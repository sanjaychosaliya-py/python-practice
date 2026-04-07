# Q7 — Create a simple calculator that reads two numbers and an operator from user and performs the operation
a = float(input("enter the first number: "))
b = float(input("enter the second number: "))
op = input("enter the operator among this(+ - / * %): ")
if op == '+':
    print(a+b)
elif op == '-':
    print(a-b)
elif op == '/':
    print(a/b)
elif op == '*':
    print(a*b)
elif op == '%':
    print(a%b)
else:
    print("error in oparator")
