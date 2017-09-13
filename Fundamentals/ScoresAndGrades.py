import random
def scoresgrades():
    for x in range(1,11):
        random_num=random.random()
        random_num=random_num*40+60
        random_num=int(random_num)
        score=str(random_num)
        if 70>random_num>=60:
            print "Score: "+score+"; Your grade is a D"
        elif 80>random_num>=70:
            print "Score: "+score+"; Your grade is a C"
        elif 90>random_num>=80:
            print "Score: "+score+"; Your grade is a B"
        elif 100>=zrandom_num>=90:
            print "Score: "+score+"; Your grade is a A"

scoresgrades()
