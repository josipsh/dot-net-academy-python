from abc import ABC, abstractmethod
from Contracts.dtos.person_create_dto import PersonCreateDto
from Contracts.dtos.person_dto import PersonDto
from Contracts.dtos.person_update_dto import PersonUpdateDto


class IPersonService(ABC):
    @abstractmethod
    def get_people() -> list[PersonDto]:
        pass

    @abstractmethod
    def get_people_for_city(city: str) -> list[PersonDto]:
        pass
    
    @abstractmethod
    def get_person_by_id(id: int) -> PersonDto:
        pass

    @abstractmethod
    def create_person(person: PersonUpdateDto) -> None:
        pass

    @abstractmethod
    def delete_person(id: int) -> None:
        pass
    
    