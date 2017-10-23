from datetime import datetime

class Call(object):
    NUM_CALLS = 0
    def __init__(self, caller, phone_num, reason):
        self.caller = caller
        self.phone_num = phone_num
        self.time_of_call = datetime.now()
        self.reason = reason
        self.id = Call.NUM_CALLS

        Call.NUM_CALLS += 1

    def display_info(self):
        print "\n" + ("#" * 20)
        for attr, val in self.__dict__.iteritems():
            if attr == "time_of_call":
                print "{}: {}".format(attr, val.strftime("%I:%M:%S"))
            else:
                print "{}: {}".format(attr, val)
        print "#" * 20

kate=Call("woo","9999","burgler")
kate.display_info()
