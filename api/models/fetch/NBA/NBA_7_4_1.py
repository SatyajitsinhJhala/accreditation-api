from pydantic import BaseModel

class NBA_7_4_1(BaseModel):
    laboratory_name: str
    safety_measures: str

    def todict(self):
        return {
            "laboratory_name": str(self.laboratory_name),
            "safety_measures": str(self.safety_measures)
        }