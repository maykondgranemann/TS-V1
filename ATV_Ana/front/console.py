from ATV_Ana.back.controller.seller_controller import SellerController
from ATV_Ana.back.models.seller import Seller

option = 10

while option > 0:
    sellers = SellerController().read_all()
    for seller in sellers:
        print(f"Id: {str(seller.id)} | Name: {seller.name} | Phone: {seller.phone} | Email: {seller.email}")

    print("\n\n0 - Exit\n1 - Create Seller\n2 - Update Seller\n3 - Delete Seller")
    option = int(input("Please, choose one option: "))
    if option == 1:
        print("Please enter the information required:\n")
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        SellerController().create_update(Seller(name, phone, email))
    elif option == 2:
        id_ = int(input("please, type the id you would like to update: "))
        seller = SellerController().read_by_id(id_)
        print("Please enter the new information required:\n")
        seller.name = input("Name: ")
        seller.phone = input("Phone: ")
        seller.email = input("Email: ")
        SellerController().create_update(seller)
    elif option == 3:
        id_ = int(input("please, type the id you would like to delete: "))
        seller = SellerController().read_by_id(id_)
        SellerController().delete(seller)
    else:
        exit()



