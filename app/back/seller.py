import json
from datetime import datetime

from .utils import write_to_logs, write_to_txt_store, read_txt
 
def create_seller(name:str, phone:str, email:str)->None:
    content={
        'name':name,
        'phone':phone,
        'email':email
    }
    write_to_txt_store(json.dumps(content), 'sellers')
    write_to_logs(f'Seller created - {name}')

def read_seller()->list:
    write_to_logs(f'seller listed - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    
    seller_list = read_txt('sellers')
    
    for i, line in enumerate(seller_list):
        seller_list[i] = json.loads(line)
    return seller_list