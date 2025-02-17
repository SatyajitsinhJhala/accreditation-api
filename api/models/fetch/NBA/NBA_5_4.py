from pydantic import BaseModel

class NBA_5_4(BaseModel):
    person_name: str
    course_name: str
    designation_organization: str
    hours_handled: int

    def todict(self):
        return {
            "person_name": str(self.person_name),
            "course_name": str(self.course_name),
            "designation_organization": str(self.designation_organization),
            "hours_handled": int(self.hours_handled)
        }