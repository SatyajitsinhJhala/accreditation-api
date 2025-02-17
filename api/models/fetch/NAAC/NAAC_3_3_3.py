from pydantic import BaseModel
class NAAC_3_3_3(BaseModel):
    recipient_name:str
    awarding_agency:str
    year_of_award:int

    def todict(self):
        return{
            "recipient_name":str(self.recipient_name),
            "awarding_agency":str(self.awarding_agency),
            "year_of_award":str(self.year_of_award),
        }