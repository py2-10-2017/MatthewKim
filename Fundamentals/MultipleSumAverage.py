#Multiples pt1
for number in range(1,1001):
    if number%2==1:
    #    print number

#pt2
for number in range (5,1000000):
    if number%5==0:
    #    print number

#Sum List
a = [1, 2, 5, 10, 255, 3]
total=0
for i in a:
    total+=i
print total

#Average List
total=0
average=0
for i in a:
    total+=i
average=total/len(a)
print average
