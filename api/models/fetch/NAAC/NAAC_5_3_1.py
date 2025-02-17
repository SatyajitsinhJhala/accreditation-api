from pydantic import BaseModel

class NAAC_5_3_1(BaseModel):
    year: int
    award_name: str
    team_or_individual: str
    event_type: str
    classification: str
    student_name: str
    student_id: int

    def todict(self):
        return {
            "year": int(self.year),
            "award_name": str(self.award_name),
            "team_or_individual": str(self.team_or_individual),
            "event_type": str(self.event_type),
            "classification": str(self.classification),
            "student_name": str(self.student_name),
            "student_id": int(self.student_id)
        }