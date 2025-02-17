from pydantic import BaseModel

class NBA_4B(BaseModel):
    N4: int
    N5: int
    total_admitted: int

    def todict(self):
        return {
            "N4": int(self.N4),
            "N5": int(self.N5),
            "total_admitted": int(self.total_admitted)
        }