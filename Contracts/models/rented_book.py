from Contracts.models.book import Book
from Contracts.models.person import Person


class RentedBook:
    id: int
    person_id: int
    book_id: int
    
    person: Person
    book: Book