from pydantic import BaseModel

class NBA_6_1_6(BaseModel):
    faculty_name: str
    event_name: str
    website_link: str

    def todict(self):
        return {
            "faculty_name": str(self.faculty_name),
            "event_name": str(self.event_name),
            "website_link": str(self.website_link)
        }