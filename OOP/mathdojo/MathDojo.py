#Part 1
class MathDojo(object):
    def __init__(self):
        self.result=0

    def add(self,*vars):
        for var in vars:
            if type(var)==int:
                self.result+=var
            elif type(var)==(list or tuple):
                for num in var:
                    self.result+=num
        return self
    def subtract(self, *vars):
        for var in vars:
            if type(var)==int:
                self.result-=var
            elif type(var)==(list or tuple):
                for num in var:
                    self.result-=num
        return self

md=MathDojo()
print md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result
