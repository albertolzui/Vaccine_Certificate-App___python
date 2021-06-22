class login:
    def __init__(self, username, password):
        self.username = username
        self.password = str(password)

    # setter
    def setUsername(username):
        self.username = username

    def setPassword(password):
        self.password = password

    # getter

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password


    def check_login(self):
        f = open("users.txt", "r")
        for line in f.readlines():
            us, pw = line.strip().split("|")
            if (self.username in us) and (self.password in pw):
                print("Login successful!")
                return True
        print("Wrong username/password")
        return False

login_key=login("fabian23", 1234)
login_key.check_login()