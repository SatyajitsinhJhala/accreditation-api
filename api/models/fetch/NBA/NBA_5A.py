from pydantic import BaseModel
from typing import Optional

class NBA_5A(BaseModel):
    faculty_name: str
    pan_no: str
    apaar_id: str
    highest_degree: str
    university: str
    area_of_specialization: str
    date_of_join: str
    designation_at_join: str
    present_designation: str
    designated_as_professor: Optional[str]
    designated_as_associate_professor: Optional[str]
    designated_as_assistant_professor: Optional[str]
    nature_of_association: str
    contractual_obligation: str
    currently_associated: bool
    date_of_leave: Optional[str]

    def todict(self):
        return {
            "faculty_name": str(self.faculty_name),
            "pan_no": str(self.pan_no),
            "apaar_id": str(self.apaar_id),
            "highest_degree": str(self.highest_degree),
            "university": str(self.university),
            "area_of_specialization": str(self.area_of_specialization),
            "date_of_join": str(self.date_of_join),
            "designation_at_join": str(self.designation_at_join),
            "present_designation": str(self.present_designation),
            "designated_as_professor": str(self.designated_as_professor) if self.designated_as_professor else None,
            "designated_as_associate_professor": str(self.designated_as_associate_professor) if self.designated_as_associate_professor else None,
            "designated_as_assistant_professor": str(self.designated_as_assistant_professor) if self.designated_as_assistant_professor else None,
            "nature_of_association": str(self.nature_of_association),
            "contractual_obligation": str(self.contractual_obligation),
            "currently_associated": bool(self.currently_associated),
            "date_of_leave": str(self.date_of_leave) if self.date_of_leave else None
        }