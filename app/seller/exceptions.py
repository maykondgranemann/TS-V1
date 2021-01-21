class SellerNotFoundException(Exception):
    def __init__(self) -> None:
        super().__init__('Seller not found!')
