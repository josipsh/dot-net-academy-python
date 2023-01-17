from Contracts.models.address import Address
from Contracts.models.rented_book import RentedBook


class Person:
    id: int
    first_name: str
    last_name: str
    
    address: Address
    books: list[RentedBook]
    
    
    def __init__(self, id: int, first_name: str, last_name: str, address: Address) -> 'Person':
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
    
    
    def __repr__(self) -> str:
        return f'{self.id} | {self.first_name} - {self.last_name} -> {repr(self.address)}'
    