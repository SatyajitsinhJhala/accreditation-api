from pydantic import BaseModel

class NBA_4_6(BaseModel):
    F: int
    X: int
    Y: int
    Z: int
    P1: float
    P2: float

    def todict(self):
        return {
            "F": int(self.F),
            "X": int(self.X),
            "Y": int(self.Y),
            "Z": int(self.Z),
            "P1": float(self.P1),
            "P2": float(self.P2)
        }