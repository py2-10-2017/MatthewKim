def multiply(arr,num):
    for x in arr:
        arr[x] *= num
    return x


a = [2,4,10,16]
b = multiply(a,5)
print b
