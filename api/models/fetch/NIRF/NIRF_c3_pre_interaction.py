from pydantic import BaseModel

class NIRF_C3_PreInteraction(BaseModel):
    publication_type: str
    authors: str
    full_title: str
    year_of_publication: int

    def todict(self):
        return {
            "publication_type": str(self.publication_type),
            "authors": str(self.authors),
            "full_title": str(self.full_title),
            "year_of_publication": int(self.year_of_publication)
        }
