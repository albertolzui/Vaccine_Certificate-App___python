import Menu as mn
import MenuF as mf
import MenuM as mm
import MenuA as ma
import MenuE as me
import MenuG as mg
import getpass
from login import login


def main():
    log = login(input("Username: "), getpass.getpass(prompt="Password: "))

    if log.username == "fabian23" and log.password == "1234":
        mainMenuf = mf.MenuF()
        mainMenuf.runCode()

    elif log.username == "albert15" and log.password == "2211":
        mainMenuA = ma.MenuA()
        mainMenuA.runCode()

    elif log.username == "eldar24" and log.password == "1551":
        mainMenue = me.MenuE()
        mainMenue.runCode()

    elif log.username == "michael8" and log.password == "1334":
        mainMenum = mm.MenuM()
        mainMenum.runCode()

    elif log.username == "george7" and log.password == "1442":
        mainMenug = mg.MenuG()
        mainMenug.runCode()

    elif log.check_login() == True:
        mainMenu = mn.Menu()
        mainMenu.runCode()


main()
