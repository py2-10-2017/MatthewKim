users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

for key,data in users.items():
    count=0
    countI=0
    for value in data:
        if key=="Students":
            if count==0:
                print "Students"
            count+=1
            first_name=value["first_name"].upper()
            last_name=value["last_name"].upper()
            countstring=str(count)
            length=len(value["first_name"])+len(value["last_name"])
            length=str(length)
            print countstring+" - "+first_name+" "+last_name+" - "+length
        else:
            if countI==0:
                print "Instructors"
            countI+=1
            countstring=str(countI)
            first_name=value["first_name"].upper()
            last_name=value["last_name"].upper()
            length=len(value["first_name"])+len(value["last_name"])
            length=str(length)
            print countstring+" - "+first_name+" "+last_name+" - "+length
        #+" " + value["last_name"]
