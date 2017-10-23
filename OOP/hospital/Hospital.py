global id
id=0

class Patient(object):
    def __init__(self, name, allergies):
        global id
        self.name=name
        self.allergies=allergies
        self.id=id
        self.bed_number=None
        id+=1

class Hospital(object):
    def __init__(self, name, capacity):
        self.name=name
        self.capacity=capacity
        self.patients=[]
        self.beds=[]
    def admit(self, new_patient):
        if self.capacity>len(self.patients):
            self.patients.append(new_patient)
            for bed_number in range(1,self.capacity+1):
                if bed_number in self.beds:
                    continue
                else:
                    new_patient.bed_number=bed_number
                    self.beds.append(bed_number)
                    break
        else:
            print "The hospital is full"
        return self
    def discharge(self, patient_name):
        for patient in self.patients:
            if patient.name==patient_name:
                self.beds.remove(patient.bed_number)
                self.patients.remove(patient)
        return self

Katie=Patient("Katie","None")
redcross=Hospital("redcross",2)
redcross.admit(Katie)
print Katie.bed_number
Kelley=Patient("Kelley","stretching")
redcross.admit(Kelley)
print Kelley.bed_number
Bob=Patient("Bob","Bananas")
redcross.admit(Bob)
redcross.discharge("Katie")
redcross.admit(Bob)
print Bob.bed_number
