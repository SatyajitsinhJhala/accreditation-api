from pydantic import BaseModel
from typing import Optional

class NBAInstitutionalInformation(BaseModel):
    institution_name: str
    affiliating_university_name: str
    affiliating_university_address: str
    institution_type: str
    year_of_establishment: int
    ownership_status: str
    vision: str
    mission: str
    other_institution_name: Optional[str]
    other_institution_year_of_establishment: Optional[int]
    other_institution_programs_of_study: Optional[str]
    other_institution_location: Optional[str]
    program_name: str
    year_of_start: int
    sanctioned_intake: int
    aicte_approval_details: str
    accreditation_status: str
    number_of_times_accredited: int
    department_name: str
    faculty_id: int
    designation: str
    date_of_join: str
    currently_associated: bool
    student_id: int
    batch_year: int
    year_of_join: int
    year_of_exit: Optional[int]
    type_of_exit: Optional[str]
    branch_id: int
    head_of_institution_name: str
    head_of_institution_designation: str
    head_of_institution_email: str
    head_of_institution_mobile: str
    nba_coordinator_name: str
    nba_coordinator_designation: str

    def todict(self):
        return {
            "institution_name": str(self.institution_name),
            "affiliating_university_name": str(self.affiliating_university_name),
            "affiliating_university_address": str(self.affiliating_university_address),
            "institution_type": str(self.institution_type),
            "year_of_establishment": int(self.year_of_establishment),
            "ownership_status": str(self.ownership_status),
            "vision": str(self.vision),
            "mission": str(self.mission),
            "other_institution_name": str(self.other_institution_name) if self.other_institution_name else None,
            "other_institution_year_of_establishment": int(self.other_institution_year_of_establishment) if self.other_institution_year_of_establishment else None,
            "other_institution_programs_of_study": str(self.other_institution_programs_of_study) if self.other_institution_programs_of_study else None,
            "other_institution_location": str(self.other_institution_location) if self.other_institution_location else None,
            "program_name": str(self.program_name),
            "year_of_start": int(self.year_of_start),
            "sanctioned_intake": int(self.sanctioned_intake),
            "aicte_approval_details": str(self.aicte_approval_details),
            "accreditation_status": str(self.accreditation_status),
            "number_of_times_accredited": int(self.number_of_times_accredited),
            "department_name": str(self.department_name),
            "faculty_id": int(self.faculty_id),
            "designation": str(self.designation),
            "date_of_join": str(self.date_of_join),
            "currently_associated": bool(self.currently_associated),
            "student_id": int(self.student_id),
            "batch_year": int(self.batch_year),
            "year_of_join": int(self.year_of_join),
            "year_of_exit": int(self.year_of_exit) if self.year_of_exit else None,
            "type_of_exit": str(self.type_of_exit) if self.type_of_exit else None,
            "branch_id": int(self.branch_id),
            "head_of_institution_name": str(self.head_of_institution_name),
            "head_of_institution_designation": str(self.head_of_institution_designation),
            "head_of_institution_email": str(self.head_of_institution_email),
            "head_of_institution_mobile": str(self.head_of_institution_mobile),
            "nba_coordinator_name": str(self.nba_coordinator_name),
            "nba_coordinator_designation": str(self.nba_coordinator_designation)
        }