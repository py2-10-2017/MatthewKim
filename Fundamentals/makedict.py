name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1, arr2):
    new_dict = {}
    count=0
    for x in arr1:
        new_dict[x]=arr2[count]
        count+=1
    return new_dict

a=make_dict(name, favorite_animal)
print a
