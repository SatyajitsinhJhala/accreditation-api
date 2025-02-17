from pydantic import BaseModel

class NBA_6_2_5(BaseModel):
    principal_investigator_name: str
    project_title: str
    duration_of_project: str
    amount_in_lacs: float
    outcomes: str

    def todict(self):
        return {
            "principal_investigator_name": str(self.principal_investigator_name),
            "project_title": str(self.project_title),
            "duration_of_project": str(self.duration_of_project),
            "amount_in_lacs": float(self.amount_in_lacs),
            "outcomes": str(self.outcomes)
        }