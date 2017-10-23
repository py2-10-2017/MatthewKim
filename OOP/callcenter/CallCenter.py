from datetime import datetime
global id
id=0
class CallCenter(object):
    def __init__(self):
        self.calls=[]
        self.queue=len(self.calls)
    def add(self, call):
        self.calls.append(call)
        self.queue=len(self.calls)
        return self
    def remove(self, number=None):
        if number==None:
            self.calls.pop(0)
            self.queue=len(self.calls)
            return self
        else:
            for call in self.calls:
                if call.caller_number==number:
                    self.calls.remove(call)
            self.queue=len(self.calls)
            return self
    def info(self):
        print ("-" * 20)
        for call in self.calls:
            print "Name: "+ call.name
            print "Number: "+call.caller_number
            print ("-"*20)
        queue=str(self.queue)
        print "Queue: "+queue

class Call(object):
    def __init__(self, name, caller_number, reason):
        global id
        self.id=id
        self.name=name
        self.caller_number= caller_number
        self.time=datetime.now()
        self.reason=reason
        id+=1
    def info(self):
        id=str(self.id)
        print "ID: "+id
        print "Name: "+self.name
        print "Caller Phone Number: "+self.caller_number
        time=str(self.time)
        print "Time: "+time
        print "Reason: "+self.reason

nicole=Call("Nicole","001","someone is in the house!")
katie=Call("Katie","000","Domestic Violence")

Ambulance=CallCenter()
Ambulance.add(nicole).add(katie).remove("001")
Ambulance.info()
