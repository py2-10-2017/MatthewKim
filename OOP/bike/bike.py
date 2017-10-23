class Bike(object):
    def __init__(self, price, max_speed):
        self.price=price
        self.max_speed=max_speed
        self.miles=0
    def displayInfo(self):
        price=str(self.price)
        miles=str(self.miles)
        print self
        print "Price: "+price
        print "Max Speed: "+self.max_speed
        print "Total Miles "+miles
    def ride(self):
        print "Riding"
        self.miles=self.miles+10
        return self
    def reverse(self):
        if self.miles>0:
            print "Reversing"
            self.miles=self.miles-5
            return self
        else:
            print "Cannot reverse more"
            return self

bike1=Bike(100,"25mph")
bike2=Bike(200,"55mph")
bike3=Bike(1000,"200mph")

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()
