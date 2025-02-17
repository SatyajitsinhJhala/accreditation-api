from pydantic import BaseModel

class NBA_6_2_1(BaseModel):
    peer_reviewed_journal_papers: int
    peer_reviewed_conference_papers: int
    books_book_chapters_published: int
    citations: int
    phd_students_registered: int
    phd_students_produced: int

    def todict(self):
        return {
            "peer_reviewed_journal_papers": int(self.peer_reviewed_journal_papers),
            "peer_reviewed_conference_papers": int(self.peer_reviewed_conference_papers),
            "books_book_chapters_published": int(self.books_book_chapters_published),
            "citations": int(self.citations),
            "phd_students_registered": int(self.phd_students_registered),
            "phd_students_produced": int(self.phd_students_produced)
        }