import sys

class Menu:
    def __init__(self):
        #self.user = user
        self.choices = {
            "1": "patient",
            "2": "vaccination",
            "3": "qr scan",
            "4": "todo",
            "5": self.exit
        }

    def printMenu(self):
          print(("""================================
           MENU
               ================================
               1 - TODO
               2 - TODO
               3 - TODO
               4 - TODO
               5 - Exit program
               ================================"""),end = " ")

    def runCode(self):
        while True:
            self.printMenu()
            choice = input("Enter a number to choose an option: " )
            make = self.choices.get(choice)
            if make:
                    make()
            else:
                print("{0} is not a valid choice".format(choice))

    def exit(self):
        print("Exiting")
        sys.exit()

if __name__ == "__main__":
    menu = Menu()
    menu.printMenu()
    menu.runCode()
    menu.exit()