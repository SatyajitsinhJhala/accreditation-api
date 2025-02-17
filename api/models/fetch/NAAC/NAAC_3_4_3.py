from pydantic import BaseModel

class NAAC_3_4_3(BaseModel):
    recipient_name: str
    awarding_agency: str
    year_of_award: int

    def todict(self):
        return {
            "recipient_name": self.recipient_name,
            "awarding_agency": self.awarding_agency,
            "year_of_award": self.year_of_award,
        }