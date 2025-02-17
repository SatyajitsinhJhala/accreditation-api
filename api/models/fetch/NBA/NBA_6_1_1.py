from pydantic import BaseModel

class NBA_6_1_1(BaseModel):
    faculty_name: str
    professional_society: str
    grade_level_position: str

    def todict(self):
        return {
            "faculty_name": str(self.faculty_name),
            "professional_society": str(self.professional_society),
            "grade_level_position": str(self.grade_level_position)
        }