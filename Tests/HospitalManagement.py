from abc import ABC,abstractmethod

class MedicalOperations(ABC):
    def __init__(self,operation_name,patient,doctor):
        self.operation_name=operation_name
        self.patient=patient
        self.doctor=doctor

    @abstractmethod
    def perform_operation(self):
        pass    


class Surgery(MedicalOperations):
    def __init__(self,patient, doctor):
        super().__init__("Surgery", patient, doctor)    

    def perform_operation(self):
        return f"Surgery operation for {patient.name},by doctor {doctor.name}"    
    

class Checkup(MedicalOperations):
    def __init__(self, patient, doctor):
        super().__init__("Checkup", patient, doctor) 

    def perform_operation(self):
        return f"Checkup on {patient.name},by doctor {doctor.name}"       
    


class Patient:
    def __init__(self,name,age,medical_history):
        self.name=name
        self.age=age
        self.medical_history=medical_history
        self.appointments=[]


    def add_medical_history(self,info):
        self.medical_history.append(info)

    def view_medical_history(self):
        for info in self.medical_history:
            print(info)


    def schedule_appointment(self,doctor,date):
        appointment={"Doctor":doctor,"date":date}
        self.appointments.append(appointment)


    def view_appointment(self):
        return self.appointments


class Doctor:
    def __init__(self,name,contact_info):
        self.name=name
        self.contact_info=contact_info
        self.patients=[]


    def add_patient(self,patient):
        if patient not in self.patients:
            self.patients.append(patient)
        else:
            print(f"{patient.name} is already patient of Dr {self.name}")   


    def manage_patient_info(self,patient:Patient,info):
        patient.add_medical_history(info)


    def view_patients(self):
        for patient in self.patients:
            print(patient.name)    


class MedicalStaff:
    def __init__(self,name,position):
        self.name=name
        self.position=position


    def manage_hospital_operations(self,task):
        print(f"{self.name} in {self.position},is doing {task}")