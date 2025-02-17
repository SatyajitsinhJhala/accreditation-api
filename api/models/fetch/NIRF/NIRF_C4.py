from pydantic import BaseModel

class NIRF_C4(BaseModel):
    financial_year: int
    title_of_project: str
    funding_agency: str
    amount_in_lakh_inr: float

    def todict(self):
        return {
            "financial_year": int(self.financial_year),
            "title_of_project": str(self.title_of_project),
            "funding_agency": str(self.funding_agency),
            "amount_in_lakh_inr": float(self.amount_in_lakh_inr)
        }