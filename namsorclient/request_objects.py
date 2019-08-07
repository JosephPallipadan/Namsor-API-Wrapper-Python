class GenderBatchItem:

    ID: str = "" 
    first_name: str = ""
    last_name: str = ""

    def __init__(self, first_name: str, last_name: str, ID = "unassigned"):
        self.ID = ID
        self.first_name = first_name
        self.last_name = last_name      


class GenderBatch:
    
    items: list = []

    def addItem(self, item: GenderBatchItem):
        self.items.append(item)

