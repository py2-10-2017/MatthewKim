a=['magical unicorns',19,'hello',98.98,'world']
total=0
liststring=''
integer=False
String=False

for i in a:
    if type(i)==int or type(i)==float:
        total+=i
        integer=True
    if type(i)== str:
        liststring+=" "+i
        String=True

string2="String:"+liststring
total=str(total)
string3="Sum: "+total

if integer==True and String==True:
    string1="The list you have entered is of a mixed type"
    print string1
    print string2
    print string3
elif integer==False and String==True:
    string1="The list you have entered is of a string type"
    print string1
    print string2
elif integer==True and String==False:
    string1="The list you have entered is of an integer type"
    print string1
    print string3
