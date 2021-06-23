class Patient:
    def __init__(self, username,name,age,sex):
        self.username=username
        self.name=name
        self.age=age
        self.sex=sex
        print("Patient was created")

    def setUsername(self,username):
        self.username = username
    def setName(self,name):
        self.name=name
    def setAge(self,age):
        self.age = age
    def setSex(self, sex):
        self.sex = sex

    def getUsername(self):
        return self.username
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getSex(self):
        return self.sex
    def output(self):
        print("Username: ",self.username,"\n","Patient name: ",self.name,"\n","Patient age: ",self.age,"\n","Patient sex:",self.sex)

#patient1=Patient("eldargaifullin","Eldar Gaifullin",33,"male")
#patient1.output()

if __name__ == "__main__":
    patient1 = Patient("fabian23","Fabian Benc",23,"Male")
    patient1.output()