class Batch:
    ID: str = ""

class GenderBatchItem:

    ID: str = "" 
    first_name: str = ""
    last_name: str = ""

    def __init__(self, first_name: str, last_name: str, ID = "unassigned"):
        self.ID = ID
        self.first_name = first_name
        self.last_name = last_name      


class GenderBatch(Batch):
    
    items: list = []

    def addItem(self, item: GenderBatchItem):
        self.items.append(item)


class ParsedGenderBatchItem:
    ID: str = "" 
    first_name: str = ""
    last_name: str = ""
    prefix_or_title: str = ""
    suffix: str = ""
    middleName: str = ""

    def __init__(self, first_name: str, last_name: str, prefix_or_title: str, suffix: str, middleName: str, ID = "unassigned"):
        self.ID = ID
        self.first_name = first_name
        self.last_name = last_name 
        self.prefix_or_title = prefix_or_title
        self.suffix = suffix
        self.middleName = middleName 


class ParsedGenderBatch(Batch):
    items: list = []

    def addItem(self, item: GenderBatchItem):
        self.items.append(item)

