from pydantic import BaseModel

class NAAC_5_2_2(BaseModel):
    year: int
    student_names: str
    total_students: int
    employer_name: str
    employer_contact_no: str
    employer_contact_email: str
    program_graduated_from: str

    def todict(self):
        return {
            "year": int(self.year),
            "student_names": str(self.student_names),
            "total_students": int(self.total_students),
            "employer_name": str(self.employer_name),
            "employer_contact_no": str(self.employer_contact_no),
            "employer_contact_email": str(self.employer_contact_email),
            "program_graduated_from": str(self.program_graduated_from)
        }