from pydantic import BaseModel

class NBA_4A(BaseModel):
    sanctioned_intake: int
    N1: int
    N2: int

    def todict(self):
        return {
            "sanctioned_intake": int(self.sanctioned_intake),
            "N1": int(self.N1),
            "N2": int(self.N2)
        }