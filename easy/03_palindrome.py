# Q3 -- Check if a given string is a palindrome (ignoring spaces and case)
str2 = "S anas"
str1 = str2.lower().replace(" ", "")
list = list(str1)
list1 = list.copy()
list.reverse()
if( list1 == list):
    print("given string is palindrome", str2)
else:
    print("given string is not palindrome", str2)
