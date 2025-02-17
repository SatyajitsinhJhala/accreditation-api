from pydantic import BaseModel

class NIRF_IQAC_Development(BaseModel):
    department_name: str
    event_name: str
    organizer_name: str
    co_organizer_name: str
    start_time: str
    end_time: str
    number_of_attendees: int
    venue: str
    description: str
    speaker_details: str
    attendance_doc: str
    feedback_doc: str
    brochure_doc: str
    sdg_goal: str
    photos_docs: str
    event_report_doc: str

    def todict(self):
        return {
            "department_name": str(self.department_name),
            "event_name": str(self.event_name),
            "organizer_name": str(self.organizer_name),
            "co_organizer_name": str(self.co_organizer_name),
            "start_time": str(self.start_time),
            "end_time": str(self.end_time),
            "number_of_attendees": int(self.number_of_attendees),
            "venue": str(self.venue),
            "description": str(self.description),
            "speaker_details": str(self.speaker_details),
            "attendance_doc": str(self.attendance_doc),
            "feedback_doc": str(self.feedback_doc),
            "brochure_doc": str(self.brochure_doc),
            "sdg_goal": str(self.sdg_goal),
            "photos_docs": str(self.photos_docs),
            "event_report_doc": str(self.event_report_doc)
        }