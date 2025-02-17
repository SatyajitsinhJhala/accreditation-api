from pydantic import BaseModel

class NBA_4_7_3(BaseModel):
    publication_name: str
    editor_name: str
    student_name: str
    semester: int
    number_of_issues: int
    publication_type: str

    def todict(self):
        return {
            "publication_name": str(self.publication_name),
            "editor_name": str(self.editor_name),
            "student_name": str(self.student_name),
            "semester": int(self.semester),
            "number_of_issues": int(self.number_of_issues),
            "publication_type": str(self.publication_type)
        }