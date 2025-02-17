from pydantic import BaseModel

class NBA_4_7_1_1(BaseModel):
    name: str

    def todict(self):
        return {
            "name": str(self.name)
        }