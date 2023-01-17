from abc import ABC, abstractmethod
from Contracts.dtos.book_dto import BookDto


class IBookService(ABC):
    @abstractmethod
    def get_books() -> list[BookDto]:
        pass
    
    @abstractmethod
    def get_rented_books(user_id: int) -> list[BookDto]:
        pass
    
    @abstractmethod
    def get_book_by_id(id: int) -> BookDto:
        pass
    
    @abstractmethod
    def rent_book(user_id: int, book_id: int):
        pass
    
    @abstractmethod
    def return_book(user_id: int, book_id: int):
        pass
    