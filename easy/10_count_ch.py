# Q10 --Count vowels, consonants, spaces and special characters in a given sentence
str = input("enter sentance:").lower()
vowels = 0
space = 0
con = 0
num = 0
spch = 0
for i in str:
    if i in "aeiou":
        vowels += 1
    elif i in "0123456789":
        num += 1
    elif  i in "bcdfghijklmnpqrstvwxyz":
        con += 1
    elif i in " ":
        space += 1
    else:
        spch += 1
    
print("vowels", vowels)
print("sapce", space)
print("consonants", con )
print("special characters", spch)
print("numbers", num)
