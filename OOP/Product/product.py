class Product(object):
    def __init__(self, price, item_name, weight, brand, cost):
        self.status="for sale"
        self.price= price
        self.item_name=item_name
        self.weight=weight
        self.brand=brand
        self.cost=cost
    def sell(self):
        self.status="sold"
        return self
    def tax(self, tax):
        price=self.price+self.price*tax
        return price
    def returned(self, return_reason):
        self.return_reason=return_reason
        if return_reason=="defective":
            self.price=0
            self.status="defective"
        elif return_reason=="opened":
            self.status="used"
            self.price*=0.8
        else:
            self.status="for sale"
        return self
    def displayInfo(self):
        price=str(self.price)
        cost=str(self.cost)
        print "Price: "+price
        print "Name: "+self.item_name
        print "Weight: "+self.weight
        print "Brand: "+self.brand
        print "Cost: "+cost
        print "Status: "+self.status
        return self

ring=Product(10, "The One Ring", "10lbs", "Gucci", 10)
ring.returned("opened").displayInfo()
