class Client:
    def __init__(self,name,age,vulnerabilities,documents = None):
        self.name = name
        self.age = age
        self.vulnerabilities = vulnerabilities
        self.documents = documents or []
        self.status = "intake_pending"

class Shelter:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.current_clients = []

class ServiceProvider:
    def __init__(self,name,purpose):
        self.name = name
        self.purpose = purpose
    
class IntakeForm:
    def __init__(self,name,age,height,weight,race,ethnicity,gender,housing_status):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.race = race
        self.ethnicity = ethnicity
        self.gender = gender
        self.housing_status = housing_status
    
    def submit(self):
        # Simulate form submission logic
        print(f"Intake form for {self.name} submitted successfully.")

    def validate(self):
        # Simulate form validation logic
        if self.age < 0:
            print("Invalid age. Age cannot be negative.")
            return False
        if self.height <= 0:
            print("Invalid height. Height must be greater than zero.")
            return False
        if self.weight <= 0:
            print("Invalid weight. Weight must be greater than zero.")
            return False
        print("Intake form validated successfully.")
        return True
    
    def validate_documents(self, documents):
        # Simulate document validation logic
        required_documents = ["ID", "Proof of Address", "Income Statement"]
        missing_documents = [doc for doc in required_documents if doc not in documents]
        if missing_documents:
            print(f"Missing required documents: {', '.join(missing_documents)}")
            return False
        print("All required documents are valid.")
        return True

    def housingStatus(self,self.housing_status):
        if self.housing_status == "unhoused":
            return True
        else:
            return False
