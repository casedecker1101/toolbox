class Client:
    def __init__(self,name,age,risk_factors,needs,documents = None):
        self.name = name
        self.age = age
        self.risk_factors = risk_factors
        self.needs = needs
        self.documents = documents or []
        self.status = "intake_pending"

# ------------------------
# Priority and Eligibility
# ------------------------

    def priority_score(self):
        """Compute urgency based on risk factors"""
        base = len(self.risk_factors)
        if "unsheltered" in self.risk_factors:
            base += 2
        return base

    def is_eligible(self, provider):
        """Check if the client meets a provider's requirements."""
        required = provider.requirements()
        missing = self.missing_documents(required)
        return len(missing) == 0

# ----------------------
# Document Handling
# ----------------------
    def add_document(self,documtne):
        """Attach a document to the client."""
        self.documents.append(document)

    def missing_documents(self, required_docs):
        """Return a list of required documents hte client does not have."""
        return [
            doc_type for doc_type in required_docs
            if not any(d.type == doc_type for d in self.documents)
        ]

# ---------------------
# Status & Lifecycle
# ---------------------
def update_status(self, new_status):
    """Update the client's lifecycle state."""
    self.status = new_status

# ---------------------
# Service Plan
# ---------------------
def assign_service_plan(self, plan):
    """Attach a service plan to the client."""
    self.service_plan = plan

def progress(self):
    """Advance the client's service plan."""
    if self.service_plan:
        self.service_plan.advance()

# ------------------
# Summary
# ------------------

def summary(self):
    """Return a readable snapshot of the client's state."""
    return {
        "name": self.name,
        "age": self.age,
        "status": self.status,
        "vulnerabilities": self.vulnerabilities,
        "documents": [d.type for d in self.documents],
        "priority_score": self.priority_score(),
        "service_plan":(
            self.service_plan.summary() if self.service_plan else None
        )
    }
    
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

    def housingStatus(self):
        if self.housing_status == "unhoused":
            return True
        else:
            return False
