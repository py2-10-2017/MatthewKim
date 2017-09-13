print "x  1 2 3 4 5 6 7 8 9 10 11 12"
for a in range (1,13):
    astring=str(a)
    multistring=""
    for i in range(1,13):
        istring=str(i*a)
        multistring+=" "+istring
    print astring+" "+multistring
