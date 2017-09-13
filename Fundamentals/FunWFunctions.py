#Odd/Even
def oddeven():
    for x in range(1,2001):
        xstring=str(x)
        if x%2==0:
            print "Number is "+xstring+". This is an even number."
        else:
            print "Number is "+xstring+". This is an odd number."

#multiply
def multiply(arr,x):
    new_list=[]
    for y in arr:
        new_list.append(y*x)
    return new_list

#HackerChallenge
def multiplyv2(arr):
    new_list=[]
    for x in range(0,len(arr)):
        temp_list=[]
        for y in range(1,arr[x]+1):
            temp_list.append(1)
        new_list.append(temp_list)
    return new_list

b=multiplyv2(multiply([2,4,5],3))
print b
