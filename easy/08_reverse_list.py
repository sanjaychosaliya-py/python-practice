# Q8 — Reverse a list without using the reverse() method or slicing [::-1]
a = [24, 45, 64, 73, 21, 37, 56]
n = int(len(a)/2)
m = int(len(a))
for idx in range (0, n):
    a[idx], a[-idx-1] = a[-idx-1], a[idx]
print(a)
