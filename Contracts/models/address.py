

class Address:
    id: int
    street: str
    city: str
    country: str
    
    def __init__(self, id: int, street: str, city: str, country: str) -> "Address":
        self.id = id
        self.street = street
        self.city = city
        self.country = country
    
        
    def __repr__(self) -> str:
        return f'{self.id} | {self.street} - {self.city} - {self.country}'
    