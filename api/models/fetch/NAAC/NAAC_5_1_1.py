from pydantic import BaseModel

class NAAC_5_1_1(BaseModel):
    year: int
    scheme_type: str
    number_of_students_benefited: int

    def todict(self):
        return {
            "year": int(self.year),
            "scheme_type": str(self.scheme_type),
            "number_of_students_benefited": int(self.number_of_students_benefited)
        }