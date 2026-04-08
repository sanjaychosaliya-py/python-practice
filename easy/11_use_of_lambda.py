# Q11 --Create a dictionary of 5 students with name as key and marks as value. Print only students who scored above 60
di = {
    "sanjay" : 89,
    "raj" : 67,
    "archis" : 45,
    "nevil" : 84,
    "parv" : 35
}
a = sorted(di.items(), key= lambda x : x[1] )
for val, i in a:
    if i >= 60:
        print(val, i)
