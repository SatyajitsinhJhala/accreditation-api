from pydantic import BaseModel

class NAAC_3_6_3(BaseModel):
    award_name: str
    awarding_body: str

    def todict(self):
        return {
            "award_name": str(self.award_name),
            "awarding_body": str(self.awarding_body)
        }