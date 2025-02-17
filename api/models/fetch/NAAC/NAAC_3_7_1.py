from pydantic import BaseModel

class NAAC_3_7_1(BaseModel):
    activity_title: str
    collaborating_agency: str
    agency_contact_no: str
    agency_contact_email: str
    participant_name: str
    source_of_financial_support: str
    year_of_collaboration: int
    duration: str
    nature_of_activity: str
    link_to_relevant_documents: str

    def todict(self):
        return {
            "activity_title": str(self.activity_title),
            "collaborating_agency": str(self.collaborating_agency),
            "agency_contact_no": str(self.agency_contact_no),
            "agency_contact_email": str(self.agency_contact_email),
            "participant_name": str(self.participant_name),
            "source_of_financial_support": str(self.source_of_financial_support),
            "year_of_collaboration": int(self.year_of_collaboration),
            "duration": str(self.duration),
            "nature_of_activity": str(self.nature_of_activity),
            "link_to_relevant_documents": str(self.link_to_relevant_documents)
        }