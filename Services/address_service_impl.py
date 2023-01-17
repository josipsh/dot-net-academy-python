from Contracts.dtos.address_dto import AddressDto
from ..Contracts.Services.address_service_interface import IAddressService

class AddressServiceImpl(IAddressService):

    def get_addresses() -> list[AddressDto]:
        return list[
            AddressDto(0, 'Strojarska 11', 'Zagreb', 'Croatia'),
            AddressDto(1, 'Some street 45', 'London', 'UK'),
            AddressDto(2, 'Another street 34', 'NewYork', 'America')
        ]
    

    def get_address_by_id(id: int) -> AddressDto:
        return AddressDto(0, 'Strojarska 11', 'Zagreb', 'Croatia')