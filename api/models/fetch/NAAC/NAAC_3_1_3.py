from pydantic import BaseModel
class NAAC_3_1_3(BaseModel):
    teacher_name:str
    award_fellowship:str
    year_of_award:int
    awarding_agency:str
    def todict(self):
        return{
            "teacher_name":str(self.teacher_name),
            "award_fellowship":str(self.award_fellowship),
            "year_of_award":str(self.year_of_award),
            "awarding_agency":str(self.awarding_agency),
        }