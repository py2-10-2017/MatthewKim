sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

a=spL

if type(a)==int:
    if a>=100:
        print "THAT'S A BIG NUMBER!!!"
    if a<100:
        print "that's a small numebr"

if type(a)==str:
    if len(a)>=50:
        print "looooooooong sentence"
    if len(a)<50:
        print "short sentence"

if type(a)==list:
    if len(a)>=10:
        print "BIG list"
    if len(a)<10:
        print "short list"
