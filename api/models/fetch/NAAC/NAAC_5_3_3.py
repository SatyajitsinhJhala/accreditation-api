from pydantic import BaseModel

class NAAC_5_3_3(BaseModel):
    year: int
    event_date: str
    activity_name: str
    level: str

    def todict(self):
        return {
            "year": int(self.year),
            "event_date": str(self.event_date),
            "activity_name": str(self.activity_name),
            "level": str(self.level)
        }