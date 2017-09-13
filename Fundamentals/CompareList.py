list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

y=0
if len(list_one)>len(list_two):
    print "The lists are not the same."
elif len(list_one)<len(list_two):
    print "The lists are not the same."
else:
    for x in range(0,len(list_one)):
        if list_one[x]==list_two[x]:
            y+=1
    if y==len(list_one):
        print  "The lists are the same"
    else:
        print "The lists are not the same."
