class Patient:
    def __init__(self, username,name,age,sex):
        self.username=username
        self.name=name
        self.age=age
        self.sex=sex
        print("Patient was created")

    def setUsername(username):
        self.username = username
    def setName(name):
        self.name=name
    def setAge(age):
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
        print(self.username,self.name,self.age,self.sex)

patient1=Patient("eldargaifullin","Eldar Gaifullin",33,"male")
patient1.output()