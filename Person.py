class Person:
	def setFullName(self,fname,lname):
		self.fname = fname
		self.lname = lname
	def printFullName(self):
		print(self.fname," ",self.lname)


personName = Person()
personName.setFullName("omkar","haldankar")
personName.printFullName()
