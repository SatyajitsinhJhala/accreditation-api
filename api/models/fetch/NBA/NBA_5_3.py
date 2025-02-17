from pydantic import BaseModel

class NBA_5_3(BaseModel):
    total_faculty_required: int
    F1: int
    F2: int
    F3: int
    proportion: str

    def todict(self):
        return {
            "total_faculty_required": int(self.total_faculty_required),
            "F1": int(self.F1),
            "F2": int(self.F2),
            "F3": int(self.F3),
            "proportion": str(self.proportion)
        }