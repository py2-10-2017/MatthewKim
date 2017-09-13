words = "It's thanksgiving day. It's my birthday,too!"
print words.find("day")
words=words.replace("day","month",1)
print words

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
y=len(x)-1
print x[y]

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
y=(len(x)+1)/2
z=[]
for number in range(0,y):
    z.append(x[number])
    x.pop(0)
x.insert(0,z)
print x
