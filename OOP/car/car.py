class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        if price>10000:
            self.tax="15%"
        else:
            self.tax="12%"
        self.price=price
        self.speed=speed
        self.fuel=fuel
        self.mileage=mileage
        self.display_all()
    def display_all(self):
        info=[]
        info.extend((self.price, self.speed, self.fuel, self.mileage, self.tax))
        price=str(self.price)
        print "Price: "+price
        print "Speed: "+self.speed
        print "Fuel: "+self.fuel
        print "Mileage: "+self.mileage
        print "Tax: "+self.tax
        return info

car1=Car(2000, "35mph", "Full", "15mpg")
car2=Car(2000, "50mph", "Kind of full", "35mpg")
car3=Car(3000, "80mph", "Empty", "20mpg")
car4=Car(33333,"200mph", "Full", "18mpg")
car5=Car(2, "1mph", "Always Full", "Infinite mpg")
car6=Car(1000000, "300mph", "Half", "5mpg")
