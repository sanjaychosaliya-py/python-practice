# Q12 --Write a function that checks if two strings are anagrams of each other (e.g. "listen" and "silent")
def find(list1, list2):
    if list1 == list2:
        print("it is anagrams")
    else:
        print("not enegrams")
str1 = input("enter string a:")
str2 = input("enter string b:")
list1 = sorted(str1)
list2 = sorted(str2)
find(list1, list2)
