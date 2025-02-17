from pydantic import BaseModel

class NBA_5_5(BaseModel):
    A: int
    B: int
    C: int
    D: int
    E: int
    AF: int
    RF: int
    FR: float

    def todict(self):
        return {
            "A": int(self.A),
            "B": int(self.B),
            "C": int(self.C),
            "D": int(self.D),
            "E": int(self.E),
            "AF": int(self.AF),
            "RF": int(self.RF),
            "FR": float(self.FR)
        }