from pydantic import BaseModel

class NIRF_C3_PostInteraction(BaseModel):
    year: int
    patents_filed: int
    patents_granted: int
    patents_licensed: int
    collaborative_patents: int
    designs_filed: int
    designs_granted: int
    amount_in_lakh_inr: float

    def todict(self):
        return {
            "year": int(self.year),
            "patents_filed": int(self.patents_filed),
            "patents_granted": int(self.patents_granted),
            "patents_licensed": int(self.patents_licensed),
            "collaborative_patents": int(self.collaborative_patents),
            "designs_filed": int(self.designs_filed),
            "designs_granted": int(self.designs_granted),
            "amount_in_lakh_inr": float(self.amount_in_lakh_inr)
        }
