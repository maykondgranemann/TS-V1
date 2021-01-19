class SellerNotFoundException(Exception):
    def __init__(self):
        super().__init__('Seller not found!')
