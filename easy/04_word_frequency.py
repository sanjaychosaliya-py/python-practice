# Q4 — Read a text file and count how many times each word appears, then print top 5
f = open("hello.txt", "r")
r = f.read()
words = r.split()
di = {}
for word in words:
    di[word] = di.get(word, 0) + 1
sorted_words = sorted(di.items(), key=lambda x: x[1], reverse=True)
top5 = sorted_words[:5]
for word, count in top5:
    print(word, ":", count)
