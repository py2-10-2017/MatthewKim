import random
def cointoss():
    headcount=0
    tailcount=0
    headcountstr="0"
    tailcountstr="0"
    for x in range(1,5001):
        random_num=round(random.random())
        attempt=str(x)
        if random_num==1:
            headcount+=1
            headcountstr=str(headcount)
            print "Attempt #"+attempt+": Throwing a coin... It's a head! ... Got "+headcountstr+" head(s) so far and "+tailcountstr+" so far"
        else:
            tailcount+=1
            tailcountstr=str(tailcount)
            print "Attempt #"+attempt+": Throwing a coin... It's a tail! ... Got "+tailcountstr+" tails(s) so far and "+headcountstr+" so far"


cointoss()
