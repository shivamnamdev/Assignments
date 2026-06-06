from abc import ABC, abstractmethod

# =====================================
# Abstract Base Class
# =====================================

class HospitalSystem(ABC):

    @abstractmethod
    def execute(self):        # FIX 1
        pass


# =====================================
# Person Class
# =====================================

class Person:

    hospital_name = "City Care Hospital"

    def __init__(self, name, age, contact):      # FIX 2

        self.name = name
        self._contact = contact
        self.__age = age                         # FIX 3

    def get_age(self):
        return self.__age

    def show(self):
        print(f"Name: {self.name}, Contact: {self._contact}")


# =====================================
# Doctor Class
# =====================================

class Doctor(Person):

    def __init__(self, name, age, contact, specialization):

        super().__init__(name, age, contact)

        self.specialization = specialization
        self.patients_treated = []
        self.available_days = set()
        self.cabin = (2, 5)

    def add_patient(self, patient_name):
        self.patients_treated.append(patient_name)

    def set_availability(self, day):
        self.available_days.add(day)

    def show(self, detail=False):

        if detail:
            print(self.__dict__)     # FIX 4
        else:
            print(f"Dr. {self.name} - {self.specialization}")

    # ===============================
    # NEW TASK 4
    # ===============================

    def show_cabin(self):

        floor, room = self.cabin

        print(
            f"Dr. {self.name} - Floor: {floor}, Room: {room}"
        )

    def execute(self):
        print(f"Dr. {self.name} is on duty.")


# =====================================
# Patient Class
# =====================================

class Patient(Person):

    def __init__(self, name, age, contact, disease):

        super().__init__(name, age, contact)     # FIX 5

        self.disease = disease
        self.__bills = []

    def add_bill(self, amount):

        self.__bills.append(amount)              # FIX 6

    def get_total_bill(self):

        total = 0

        for bill in self.__bills:
            total += bill

        return total

    # ===============================
    # NEW TASK 3
    # ===============================

    def calculate_discount(self):

        total_bill = self.get_total_bill()

        if total_bill > 20000:
            return total_bill * 0.10

        return 0

    def show(self, detail=False):

        if detail:

            print(
                f"Patient: {self.name}, "
                f"Disease: {self.disease}, "
                f"Bills: {self.__bills}"
            )

        else:

            print(
                f"Patient: {self.name} - {self.disease}"
            )

    def execute(self):

        print(
            f"Patient {self.name} checked in."
        )


# =====================================
# Hospital Class
# =====================================

class Hospital(HospitalSystem):

    def __init__(self):

        self.__doctors = []
        self.__patients = []

    def add_doctor(self, doctor):

        self.__doctors.append(doctor)

    def add_patient(self, patient):

        self.__patients.append(patient)

    def show_doctors(self):

        for doc in self.__doctors:
            doc.show()

    def show_patients(self):

        for pat in self.__patients:
            pat.show()

    def find_doctor(self, name):

        for doc in self.__doctors:

            if doc.name == name:
                return doc

        return None

    # ===============================
    # NEW TASK 1
    # ===============================

    def discharge_patient(self, patient_name):

        for patient in self.__patients:

            if patient.name == patient_name:

                self.__patients.remove(patient)

                print(
                    f"{patient_name} discharged successfully"
                )

                return

        print("Patient not found")

    # ===============================
    # NEW TASK 2
    # ===============================

    def get_doctor_report(self, doctor_name):

        for doctor in self.__doctors:

            if doctor.name == doctor_name:

                return {
                    "name": f"Dr. {doctor.name}",
                    "specialization": doctor.specialization,
                    "patients_count":
                        len(doctor.patients_treated),
                    "available_days":
                        doctor.available_days
                }

        print("Doctor not found")

    def execute(self):

        print("Hospital system running...")


# =====================================
# Main Execution
# =====================================

h = Hospital()

d1 = Doctor(
    "Sharma",
    45,
    "9876543210",
    "Cardiology"
)

d1.set_availability("Monday")
d1.set_availability("Thursday")
d1.add_patient("Rahul")

d2 = Doctor(
    "Verma",
    38,
    "8765432109",
    "Neurology"
)

p1 = Patient(
    "Rahul",
    30,
    "7654321098",
    "Heart Block"
)

p1.add_bill(15000)
p1.add_bill(8000)

p2 = Patient(
    "Priya",
    25,
    "6543210987",
    "Migraine"
)

h.add_doctor(d1)
h.add_doctor(d2)

h.add_patient(p1)
h.add_patient(p2)

# ===============================
# Existing Features
# ===============================

h.show_doctors()
h.show_patients()

print(
    f"Rahul's total bill: "
    f"{p1.get_total_bill()}"
)

print(
    f"Dr. Sharma's age: "
    f"{d1.get_age()}"
)

print(d1.specialization)      # FIX 7

d1.execute()
p1.execute()
h.execute()

# ===============================
# New Features
# ===============================

print("\nDoctor Report")
print(
    h.get_doctor_report("Sharma")
)

print("\nDiscount")
print(
    p1.calculate_discount()
)

print("\nCabin Details")
d1.show_cabin()

print("\nDischarge Patient")
h.discharge_patient("Priya")

print("\nUpdated Patient List")
h.show_patients()