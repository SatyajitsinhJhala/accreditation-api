from pydantic import BaseModel

class NIRF_C8(BaseModel):
    year: int
    event_name: str
    position: str
    event_level: str
    participant_name: str

    def todict(self):
        return {
            "year": int(self.year),
            "event_name": str(self.event_name),
            "position": str(self.position),
            "event_level": str(self.event_level),
            "participant_name": str(self.participant_name)
        }