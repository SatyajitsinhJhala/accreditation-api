from pydantic import BaseModel

class NAAC_5_1_3(BaseModel):
    year: int
    scheme_name: str
    number_of_students_benefited: int

    def todict(self):
        return {
            "year": int(self.year),
            "scheme_name": str(self.scheme_name),
            "number_of_students_benefited": int(self.number_of_students_benefited)
        }