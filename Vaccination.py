class Vaccination:

    # constructor
    def __init__(self, vaccine, patient, administered_date, administered_location):
        self.vaccine = vaccine
        self.patient = patient
        self.administered_date = administered_date
        self.administered_location = administered_location

    # getters

    # get Vaccine info
    def getVaccine(self):
        return self.vaccine

    # get Patient info
    def getPatient(self):
        return self.patient

    # get Administration date
    def getAdministered_date(self):
        return self.administered_date

    # get Administration location

    def getAdministered_location(self):
        return self.administered_location

    # setters
    # set Vaccine info
    def setVaccine(self, vaccine):
        self.vaccine = vaccine

    # set Patient info
    def setPatient(self, patient):
        self.patient = patient

    # set Administration date
    def setAdministered_date(self, administered_date):
        self.administered_date = administered_date

    # set Administration location

    def setAdministered_location(self, administered_location):
        self.administered_location = administered_location
