from pydantic import BaseModel

class NBA_6_2_3(BaseModel):
    principal_investigator_name: str
    co_principal_investigator_name: str
    department_name: str
    project_title: str
    funding_agency_name: str
    project_duration: str
    amount_in_lacs: float

    def todict(self):
        return {
            "principal_investigator_name": str(self.principal_investigator_name),
            "co_principal_investigator_name": str(self.co_principal_investigator_name),
            "department_name": str(self.department_name),
            "project_title": str(self.project_title),
            "funding_agency_name": str(self.funding_agency_name),
            "project_duration": str(self.project_duration),
            "amount_in_lacs": float(self.amount_in_lacs)
        }