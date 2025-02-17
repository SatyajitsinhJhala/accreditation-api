from pydantic import BaseModel

class NAAC_4_3_5(BaseModel):
    teacher_name: str
    module_name: str
    platform: str
    launch_date: str
    document_link: str
    institute: str

    def todict(self):
        return {
            "teacher_name": str(self.teacher_name),
            "module_name": str(self.module_name),
            "platform": str(self.platform),
            "launch_date": str(self.launch_date),
            "document_link": str(self.document_link),
            "institute": str(self.institute)
        }