from pydantic import BaseModel

class NBA_4_1(BaseModel):
    sanctioned_intake: int
    N1: int
    ER: float

    def todict(self):
        return {
            "sanctioned_intake": int(self.sanctioned_intake),
            "N1": int(self.N1),
            "ER": float(self.ER)
        }