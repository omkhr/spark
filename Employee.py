class Employee:
    
    def __init__():
	print("our class is created")
	
    def setFullName(self,id,empname):
	self.id = id
	self.empname = empname
	
    def printName(self):
	print(self.id," ",self.empname)

emp = Employee()

emp.setFullName(1,"omi")
emp.printName()
