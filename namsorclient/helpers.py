import models
import math

def list_seperator(data:list) -> list:
    if(len(data)>100):
        big_list = []
        total_num = math.ceil(len(data)/100)
        for i in range(total_num):
            big_list.append(data[i*100:(i+1)*100])
        return big_list
    else:
        return data

