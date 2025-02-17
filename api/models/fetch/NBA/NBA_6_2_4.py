from pydantic import BaseModel

class NBA_6_2_4(BaseModel):
    principal_investigator_name: str
    co_principal_investigator_name: str
    department_name: str
    project_title: str
    name_of_funding_agency: str
    duration_of_project: str
    amount_in_lacs: float

    def todict(self):
        return {
            "principal_investigator_name": str(self.principal_investigator_name),
            "co_principal_investigator_name": str(self.co_principal_investigator_name),
            "department_name": str(self.department_name),
            "project_title": str(self.project_title),
            "name_of_funding_agency": str(self.name_of_funding_agency),
            "duration_of_project": str(self.duration_of_project),
            "amount_in_lacs": float(self.amount_in_lacs)
        }