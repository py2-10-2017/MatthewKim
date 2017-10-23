class Animal(object):
    def __init__(self, name):
        self.name=name
        self.health=100
    def walk(self):
        self.health-=1
        return self
    def run(self):
        self.health-=5
        return self
    def display_health(self):
        health=str(self.health)
        print "Health: "+health
        return self

Cheese=Animal("Cheese")
Cheese.walk().walk().walk().run().run().display_health()

class Dog(Animal):
    def __init__(self, name):
        super(Dog,self).__init__(name)
        self.health=150
    def pet(self):
        self.health+=5
        return self

lilo=Dog("lilo")
lilo.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon,self).__init__(name)
        self.health=170
    def fly(self):
        self.health+=10
        return self
    def display_health(self):
        super(Dragon,self).display_health()
        print "I am a Dragon"

Hunter=Dragon("hunter")
Hunter.display_health()
