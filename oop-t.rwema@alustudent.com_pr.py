class Patient:
    def __init__(self, patient_id, name, age, gender, admission_date, condition):
        self.id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.admission_date = admission_date
        self.condition = condition

    def get_details(self):
        """Returns a summary of the patient's information as a string."""
        return (f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}, "
                f"Admission Date: {self.admission_date}, Condition: {self.condition}")


# Function to count the number of patients
def count_patients(patient_list):
    """Takes the list of patients as an argument and returns the total number of patients."""
    return len(patient_list)


# Function to list all patient names
def list_patient_names(patient_list):
    """Takes the list of patients and returns a list of their names."""
    return [patient.name for patient in patient_list]


# Optional function to print patient details by ID
def print_patient_by_id(patient_list, patient_id):
    """Prompts the user for a patient ID, searches the patient list for that ID,
    and prints the patient's details if found."""
    for patient in patient_list:
        if patient.id == patient_id:
            print(patient.get_details())
            return
    print("Patient not found.")


# Creating instances of the Patient class
patient1 = Patient(1, "Alice", 30, "Female", "2024-01-15", "Flu")
patient2 = Patient(2, "Bob", 40, "Male", "2024-02-20", "Asthma")
patient3 = Patient(3, "Carol", 25, "Female", "2024-03-05", "Diabetes")

# Storing the patients in a list
patients = [patient1, patient2, patient3]

# Testing the functions
print("Total number of patients:", count_patients(patients))
print("List of patient names:", list_patient_names(patients))

# Testing the search function (Optional task)
search_id = int(input("Enter patient ID to search for details: "))
print_patient_by_id(patients, search_id)
