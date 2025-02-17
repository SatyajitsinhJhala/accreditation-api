from pydantic import BaseModel

class NAAC_5_2_3(BaseModel):
    year: int
    student_names: str
    program_graduated_from: str
    department_graduated_from: str
    institute_name: str
    program_admitted_to: str

    def todict(self):
        return {
            "year": int(self.year),
            "student_names": str(self.student_names),
            "program_graduated_from": str(self.program_graduated_from),
            "department_graduated_from": str(self.department_graduated_from),
            "institute_name": str(self.institute_name),
            "program_admitted_to": str(self.program_admitted_to)
        }