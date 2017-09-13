# Write a program that prints all the prime numbers and all the perfect squares for all numbers between 100 and 100000.

# For all numbers between 100 and 100000 test that number for whether it is prime or a perfect square. If it is a prime number print "Foo". If it is a perfect square print "Bar". If it is neither print "FooBar". Do not use the python math library for this exercise. For example, if the number you are evaluating is 25, you will have to figure out if it is a perfect square. It is, so print "Bar".

# This assignment is extra challenging! Try pair programming and pulling up a white board.


for number in range (100,100001):
    Square=False
    Prime=True
    for a in range(2,number):
        if number%a==0:
            Prime=False
            if a*a==number:
                Square=True
    numberstring=str(number)
    if Prime==True:
        print "Foo "+numberstring
    elif Square==True:
        print "Bar "+numberstring
    else:
        print "FooBar "+numberstring
