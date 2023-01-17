from abc import ABC, abstractmethod
from Contracts.dtos.address_create_dto import AddressCreateDto
from Contracts.dtos.address_dto import AddressDto


class IAddressService(ABC):
    @abstractmethod
    def get_addresses() -> list[AddressDto]:
        pass
    
    @abstractmethod
    def get_address_by_id(id: int) -> AddressDto:
        pass
    
    