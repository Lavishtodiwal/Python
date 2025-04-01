class Hospital:
    # instance method in which used the init
    def __init__(self,patientName,patientGender, patientAdmitDate, patientRoom, patientBed):
        self.patientName = patientName
        self.patientGender = patientGender
        self.patientAdmitDate = patientAdmitDate
        self.patientRoom = patientRoom
        self.patientBed = patientBed
    
    def patientDisp(self):
        print("")



print("\t\t******** Welcome to the Surya Hospital ********\n")

while True:
    visitor = input("Would you like to admit the patient(yes/no) -> ").strip()
    if visitor == "yes":
        patientName = input("Enter the patient name -> ")
        patientGender = input("Enter the gender of the patient(male/female/others) -> ")
        patientAdmitDate = input("Enter the Admit Date(dd:mm:yyyy) -> ")
        patientRoom = input("Enter the room no. of the patient -> ")
        patientBed = input("Enter the patient Bed no. -> ")
        patient = Hospital(patientName,patientGender, patientAdmitDate, patientRoom, patientBed)





