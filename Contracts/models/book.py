from Contracts.models.book_genre import BookGenre
from Contracts.models.rented_book import RentedBook


class Book:
    id: int
    title: str
    author: str
    genre: BookGenre
    quantity: int
    
    renters: list[RentedBook]
    
    
    def __init__(self, id: int, title: str, author: str, genre: BookGenre, quantity: int) -> "Book":
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.quantity = quantity
    
    
    def __repr__(self) -> str:
        return f'{self.id} | {self.title} - {self.author} - {self.genre.name} - {self.quantity} -> {self.renters.count()}'
    