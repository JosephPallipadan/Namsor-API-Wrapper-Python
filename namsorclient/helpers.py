import models
import math
from request_objects import GenderBatch

def list_seperator(data:list) -> list:
    big_list = []
    total_num = math.ceil(len(data)/100)
    for i in range(total_num):
        big_list.append(data[i*100:(i+1)*100])
    return big_list

def gender_batch_item_converter(item_group: GenderBatch) -> list:
    item_list = []
    for item in item_group.items:
        item_list.append({
            "ID":item.ID,
            "firstName":item.first_name,
            "lastName":item.last_name,
        })
    
    return item_list