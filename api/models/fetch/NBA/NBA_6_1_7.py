from pydantic import BaseModel

class NBA_6_1_7(BaseModel):
    faculty_name: str
    internship_training_collaboration: str
    company_place: str
    outcomes: str

    def todict(self):
        return {
            "faculty_name": str(self.faculty_name),
            "internship_training_collaboration": str(self.internship_training_collaboration),
            "company_place": str(self.company_place),
            "outcomes": str(self.outcomes)
        }