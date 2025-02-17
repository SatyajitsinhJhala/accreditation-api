from pydantic import BaseModel

class NBA_4_3(BaseModel):
    X: float
    Y: int
    Z: int
    AP1: float
    AP2: float

    def todict(self):
        return {
            "X": float(self.X),
            "Y": int(self.Y),
            "Z": int(self.Z),
            "AP1": float(self.AP1),
            "AP2": float(self.AP2)
        }