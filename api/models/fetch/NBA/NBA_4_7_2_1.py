from pydantic import BaseModel

class NBA_4_7_2_1(BaseModel):
    student_name: str
    event_name: str
    level: str
    date: str
    award: str

    def todict(self):
        return {
            "student_name": str(self.student_name),
            "event_name": str(self.event_name),
            "level": str(self.level),
            "date": str(self.date),
            "award": str(self.award)
        }