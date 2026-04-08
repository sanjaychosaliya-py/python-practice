Q13 --Using list comprehension, create a list of squares of all even numbers from 1 to 50. Do it in one line.
list = [x**2 for x in range(1, 51) if(x %2 == 0)]
print(list)
