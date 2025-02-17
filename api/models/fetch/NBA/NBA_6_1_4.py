from pydantic import BaseModel

class NBA_6_1_4(BaseModel):
    faculty_name: str
    course_name: str

    def todict(self):
        return {
            "faculty_name": str(self.faculty_name),
            "course_name": str(self.course_name)
        }