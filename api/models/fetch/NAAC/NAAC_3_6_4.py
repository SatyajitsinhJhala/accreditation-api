from pydantic import BaseModel

class NAAC_3_6_4(BaseModel):
    activity_name: str
    organizing_unit: str
    scheme_name: str
    year: int
    date: str
    location: str
    link_to_report: str

    def todict(self):
        return {
            "activity_name": str(self.activity_name),
            "organizing_unit": str(self.organizing_unit),
            "scheme_name": str(self.scheme_name),
            "year": int(self.year),
            "date": str(self.date),
            "location": str(self.location),
            "link_to_report": str(self.link_to_report)
        }