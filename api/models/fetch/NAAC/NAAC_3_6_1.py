from pydantic import BaseModel
from datetime import date  # Optional: Only if you need date type handling

class NAAC_3_6_1(BaseModel):
    date: str  # Could also use datetime.date if parsing properly
    activity_name: str
    organizing_unit: str
    students_participated: int
    teachers_participated: int
    link_to_report: str

    def todict(self):
        return {
            "date": str(self.date),
            "activity_name": str(self.activity_name),
            "organizing_unit": str(self.organizing_unit),
            "students_participated": str(self.students_participated),
            "teachers_participated": str(self.teachers_participated),
            "link_to_report": str(self.link_to_report)
        }