from pydantic import BaseModel

class NBA_4_7_1_2(BaseModel):
    body_name: str
    event_name: str
    level: str
    date: str

    def todict(self):
        return {
            "body_name": str(self.body_name),
            "event_name": str(self.event_name),
            "level": str(self.level),
            "date": str(self.date)
        }