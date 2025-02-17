from pydantic import BaseModel

class NBA_7_2_1(BaseModel):
    facility_name: str
    details: str
    reasons: str
    utilization: str
    relevance_to_pos: str

    def todict(self):
        return {
            "facility_name": str(self.facility_name),
            "details": str(self.details),
            "reasons": str(self.reasons),
            "utilization": str(self.utilization),
            "relevance_to_pos": str(self.relevance_to_pos)
        }