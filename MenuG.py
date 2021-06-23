import sys
import datetime
from Vaccine import Vaccine
from Vaccination import Vaccination
from Patient import Patient
from QrScan import QrScan

class MenuG:
    def __init__(self):
        #self.user = user
        self.choices = {
            "1": self.printPatient,
            "2": self.printVaccine,
            "3": self.printVaccination,
            "4": self.scanQr,
            "5": self.exit
        }

    def printMenu(self):
          print(("""================================
           MENU
               ================================
               1 - Patient info
               2 - Vaccine info
               3 - Vaccination info
               4 - Scan a QR Code
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

    def printVaccine(self):
        vac1 = Vaccine("Moderna", "ModernaTX", 2)
        print(vac1)

    def printVaccination(self):
        vax1 = Vaccination(3,Vaccine("Moderna", "ModernaTX", 2), "George", datetime.datetime.now(), "Munich")
        print(vax1)
    
    def printPatient(self):
        patient1 = Patient("george7","George",25,"Male")
        patient1.output()

    def scanQr(self):
        QrScan.execute_qr_scan()

if __name__ == "__main__":
    menu = MenuG()
    menu.printMenu()
    menu.runCode()
    menu.exit()