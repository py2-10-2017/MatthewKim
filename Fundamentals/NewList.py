x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
y=(len(x)+1)/2
z=[]
for number in range(0,y):
    z.append(x[number])
    x.pop(0)
x.insert(0,z)
print x
