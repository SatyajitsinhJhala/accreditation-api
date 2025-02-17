from pydantic import BaseModel

class NBA_7_1_1(BaseModel):
    laboratory_name: str
    batch_size: int
    equipment_name: str
    equipment_utilization: str
    staff_name: str
    staff_designation: str
    staff_qualification: str

    def todict(self):
        return {
            "laboratory_name": str(self.laboratory_name),
            "batch_size": int(self.batch_size),
            "equipment_name": str(self.equipment_name),
            "equipment_utilization": str(self.equipment_utilization),
            "staff_name": str(self.staff_name),
            "staff_designation": str(self.staff_designation),
            "staff_qualification": str(self.staff_qualification)
        }