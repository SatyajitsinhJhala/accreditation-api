from pydantic import BaseModel

class NBA_5_2(BaseModel):
    X: int
    Y: int
    F: int
    FQI: float

    def todict(self):
        return {
            "X": int(self.X),
            "Y": int(self.Y),
            "F": int(self.F),
            "FQI": float(self.FQI)
        }