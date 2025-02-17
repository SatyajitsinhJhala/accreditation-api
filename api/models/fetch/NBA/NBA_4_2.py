from pydantic import BaseModel

class NBA_4_2(BaseModel):
    A: int
    B: int
    SR_1: float
    SR_2: float

    def todict(self):
        return {
            "A": int(self.A),
            "B": int(self.B),
            "SR_1": float(self.SR_1),
            "SR_2": float(self.SR_2)
        }