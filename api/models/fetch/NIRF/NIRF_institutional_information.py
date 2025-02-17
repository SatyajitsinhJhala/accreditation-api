from pydantic import BaseModel

class NIRFInstitutionalInformation(BaseModel):
    year: int
    program_name: str
    participants_certified: int
    no_of_days: int

    def todict(self):
        return {
            "year": int(self.year),
            "program_name": str(self.program_name),
            "participants_certified": int(self.participants_certified),
            "no_of_days": int(self.no_of_days)
        }