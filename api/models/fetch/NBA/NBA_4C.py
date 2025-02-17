from pydantic import BaseModel

class NBA_4C(BaseModel):
    year_of_entry: int
    total_students: int
    graduated_within_stipulated_period: int
    graduated_without_backlogs: int
    graduated_with_backlogs: int

    def todict(self):
        return {
            "year_of_entry": int(self.year_of_entry),
            "total_students": int(self.total_students),
            "graduated_within_stipulated_period": int(self.graduated_within_stipulated_period),
            "graduated_without_backlogs": int(self.graduated_without_backlogs),
            "graduated_with_backlogs": int(self.graduated_with_backlogs)
        }