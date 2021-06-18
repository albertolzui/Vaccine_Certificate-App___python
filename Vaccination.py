class Vaccination:

    # constructor
    def __init__(self,vaccination_id, vaccine, patient, administered_date, administered_location):
        self.vaccination_id = vaccination_id
        self.vaccine = vaccine
        self.patient = patient
        self.administered_date = administered_date
        self.administered_location = administered_location

    # getters

    # get Vaccination ID
    def getVaccination_ID(self):
        return self.vaccination_id

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

    # set Vaccination ID
    def setVaccination_ID(self, vaccination_id):
        self.vaccination_id = vaccination_id

    def __str__(self):
        return f"Vaccination ID: {self.vaccination_id}, Vaccine: {self.vaccine}, Patient : {self.patient}" \
               f", Administered on: {self.administered_date}, Administered at: {self.administered_location} "


if __name__ == "__main__":
    import Vaccine
    import datetime

    vax1 = Vaccination(Vaccine.Vaccine("Mugl", "Kugl", 3), "Helga Huso", datetime.datetime.now(), "Pfarrkirchen")
    print(vax1)