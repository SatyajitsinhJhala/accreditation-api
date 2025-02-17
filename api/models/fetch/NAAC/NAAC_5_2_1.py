from pydantic import BaseModel

class NAAC_5_2_1(BaseModel):
    year: int
    exam_type: str
    total_students: int
    names: str

    def todict(self):
        return {
            "year": int(self.year),
            "exam_type": str(self.exam_type),
            "total_students": int(self.total_students),
            "names": str(self.names)
        }