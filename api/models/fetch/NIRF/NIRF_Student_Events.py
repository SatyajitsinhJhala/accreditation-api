from pydantic import BaseModel

class NIRF_Student_Events(BaseModel):
    year: int
    event_name: str
    position: str
    event_type: str

    def todict(self):
        return {
            "year": int(self.year),
            "event_name": str(self.event_name),
            "position": str(self.position),
            "event_type": str(self.event_type)
        }