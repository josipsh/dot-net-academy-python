
from ..Services.address_service_impl import AddressServiceImpl


def main():
    service = AddressServiceImpl()
    
    print(service.get_address_by_id(1))
    
    

main()