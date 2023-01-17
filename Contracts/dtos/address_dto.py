
class AddressDto:
    id: int
    street: str
    city: str
    country: str
    
    def __init__(self, id: int, street: str, city: str, country: str) -> "AddressDto":
        self.id = id
        self.street = street
        self.city = city
        self.country = country