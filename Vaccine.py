class Vaccine:

    # constructor
    def __init__(self, name, manufacturer, doses):
        self.name = name
        self.manufacturer = manufacturer
        self.doses = doses

        # getters

    # get Vaccine name
    def get_name(self):
        return self.name

    # get Vaccine manufacturer
    def get_manufacturer(self):
        return self.manufacturer

    # get Vaccine doses
    def get_doses(self):
        return self.doses

    # setters

    # set Vaccine name
    def set_name(self, name):
        self.name = name

    # set Vaccine manufacturer
    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    # set Vaccine doses
    def set_doses(self, doses):
        if type(doses) is int:
            self.doses = doses
        else:
            raise ValueError("Please input an int as dosage")
