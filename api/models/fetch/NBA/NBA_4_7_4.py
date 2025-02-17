from pydantic import BaseModel

class NBA_4_7_4(BaseModel):
    student_name: str
    semester: int
    publisher_name: str
    journal_conference_name: str
    volume_number: int
    issue_number: int
    award_name: str

    def todict(self):
        return {
            "student_name": str(self.student_name),
            "semester": int(self.semester),
            "publisher_name": str(self.publisher_name),
            "journal_conference_name": str(self.journal_conference_name),
            "volume_number": int(self.volume_number),
            "issue_number": int(self.issue_number),
            "award_name": str(self.award_name)
        }