from models import *
from abc import ABC, abstractmethod
from country_codes import CountryCodes

class BatchItem(ABC):
    pass

class Batch(ABC):
 
    def __init__(self):
        self.batch_item = BatchItem

    @abstractmethod
    def batch_item_converter(self):
        pass
    @abstractmethod
    def addItem(self, item:BatchItem ):
        self.items.append(item)   
 

class GenderBatch(Batch):
    
    class GenderBatchItem(BatchItem):

        def __init__(self, first_name: str, last_name: str, ID = "unassigned"):
            self.ID = ID
            self.first_name = first_name
            self.last_name = last_name     

    url = "genderBatch"

    def __init__(self):
        self.items = []
        self.response_type = GenderResponse

    def addItem(self, first_name: str, last_name: str, ID = "unassigned"):
        super().addItem(self.GenderBatchItem(first_name, last_name, ID))

    def batch_item_converter(self) -> list:
        items_list = []
        for item in self.items:
            items_list.append({
                "id":item.ID,
                "firstName":item.first_name,
                "lastName":item.last_name,
            })
        
        return items_list

class GenderGeoBatch(Batch):

    class GenderGeoBatchItem(BatchItem):
        def __init__(self, first_name: str, last_name: str, country_code: CountryCodes, ID ="unassigned"):
            self.ID = ID
            self.first_name = first_name
            self.last_name = last_name 
            self.country_code = country_code.value

    url = "genderGeoBatch"

    def __init__(self):
        self.items = []
        self.response_type = GenderResponse

    def addItem(self, first_name: str, last_name: str, country_code: CountryCodes, ID ="unassigned"):
        super().addItem(self.GenderGeoBatchItem(first_name, last_name, country_code, ID))


    def batch_item_converter(self) -> list:
        items_list = []
        for item in self.items:
            items_list.append({
                "id":item.ID,
                "firstName":item.first_name,
                "lastName":item.last_name,
                "countryIso2": item.country_code
            })
        
        return items_list
 


class ParsedGenderBatch(Batch):
    url = "parsedGenderBatch"

    class ParsedGenderBatchItem(BatchItem):

        def __init__(self, first_name: str, last_name: str, prefix_or_title: str, suffix: str, middle_name: str, ID = "unassigned"):
            self.ID = ID
            self.first_name = first_name
            self.last_name = last_name 
            self.prefix_or_title = prefix_or_title
            self.suffix = suffix
            self.middle_name = middle_name 

    def __init__(self):
        self.items = []
        self.response_type = GenderResponse
    
    def addItem(self, first_name: str, last_name: str, prefix_or_title: str, suffix: str, middle_name: str, ID = "unassigned"):
        super().addItem(self.ParsedGenderBatchItem(first_name, last_name, prefix_or_title, suffix, middle_name, ID))

    def batch_item_converter(self)->list:
        items_list = []
        for item in self.items:
            items_list.append({
                "id":item.ID,
                "firstName":item.first_name,
                "lastName":item.last_name,
                "prefixOrTitle":item.prefix_or_title,
                "suffix":item.suffix,
                "middleName":item.middle_name,
            })
        
        return items_list
        


class ParsedGenderGeoBatch(Batch):

    class ParsedGenderGeoBatchItem(BatchItem):
        def __init__(self, first_name: str, last_name: str, prefix_or_title: str, suffix: str, middle_name: str, country_code: CountryCodes, ID = "unassigned"):
            self.ID = ID
            self.first_name = first_name
            self.last_name = last_name 
            self.prefix_or_title = prefix_or_title
            self.suffix = suffix
            self.middle_name = middle_name 
            self.country_code = country_code.value

    url = "parsedGenderGeoBatch"

    def __init__(self):
        self.items = []
        self.response_type = GenderResponse

    def addItem(self, first_name: str, last_name: str, prefix_or_title: str, suffix: str, middle_name: str, country_code: CountryCodes, ID = "unassigned"):
        super().addItem(self.ParsedGenderGeoBatchItem(first_name, last_name, prefix_or_title, suffix, middle_name, country_code, ID))

    def batch_item_converter(self)->list:
        items_list = []
        for item in self.items:
            items_list.append({
                "id":item.ID,
                "firstName":item.first_name,
                "lastName":item.last_name,
                "prefixOrTitle":item.prefix_or_title,
                "suffix":item.suffix,
                "middleName":item.middle_name,
                "countryIso2": item.country_code
            })
        
        return items_list



class GenderFullBatch(Batch):

    class GenderFullBatchItem(BatchItem):

        def __init__(self, name: str, ID = "unassigned"):
            self.ID = ID
            self.name = name

    url = "genderFullBatch"

    def __init__(self):
        self.items = []
        self.response_type = GenderResponse

    def addItem(self, name: str, ID = "unassigned"):
        super().addItem(self.GenderFullBatchItem(name,ID))

    def batch_item_converter(self)->list:
        items_list = []
        for item in self.items:
            items_list.append({
                "id":item.ID,
                "name":item.name,
            })
        
        return items_list

    
class GenderFullGeoBatch(Batch):

    class GenderFullGeoBatchItem(BatchItem):

        def __init__(self, name: str,  country_code: CountryCodes,  ID = "unassigned"):
            self.ID = ID
            self.name = name
            self.country_code = country_code.value
    
    url = "genderFullGeoBatch"

    def __init__(self):
        self.items = []
        self.response_type = GenderResponse

    def addItem(self, name: str,  country_code: CountryCodes,  ID = "unassigned"):
        super().addItem(self.GenderFullGeoBatchItem(name,country_code,ID))

    def batch_item_converter(self)->list:
        items_list = []
        for item in self.items:
            items_list.append({
                "id":item.ID,
                "name":item.name,
                "countryIso2":item.country_code,
            })
        
        return items_list




class OriginBatch(Batch):

    class OriginBatchItem(BatchItem):

        def __init__(self, first_name: str, last_name: str,  ID = "unassigned"):
            self.ID = ID
            self.first_name = first_name
            self.last_name = last_name


    url = "originBatch"

    def __init__(self):
        self.items = []
        self.response_type = OriginResponse
    
    def addItem(self, first_name: str, last_name: str,  ID = "unassigned"):
        super().addItem(self.OriginBatchItem(first_name,last_name,ID))

    
    def batch_item_converter(self)->list:
        items_list = []
        for item in self.items:
            items_list.append({
                "id":item.ID,
                "firstName":item.first_name,
                "lastName":item.last_name,
            })
        
        return items_list

class CountryBatch(Batch):

    class CountryBatchItem(BatchItem):

        def __init__(self, name: str,  ID = "unassigned"):
            self.ID = ID
            self.name = name


    url = "countryBatch"

    def __init__(self):
        self.items = []
        self.response_type = CountryResponse
    
    def addItem(self, name: str,  ID = "unassigned"):
        super().addItem(self.CountryBatchItem(name, ID))

    
    def batch_item_converter(self)->list:
        items_list = []
        for item in self.items:
            items_list.append({
                "id":item.ID,
                "name":item.name,
            })
        
        return items_list

class US_RaceEthnicityBatch(Batch):
    class US_RaceEthnicityBatchItem(BatchItem):

        def __init__(self, first_name: str, last_name: str,  country_code: CountryCodes,   ID = "unassigned"):
            self.ID = ID
            self.first_name = first_name
            self.last_name = last_name
            self.country_code = country_code.value


    url = "usRaceEthnicityBatch"

    def __init__(self):
        self.items = []
        self.response_type = RaceEthnicityResponse
    

    
    def addItem(self, first_name: str, last_name: str,  country_code: CountryCodes,   ID = "unassigned"):
        super().addItem(self.US_RaceEthnicityBatchItem(first_name,last_name,country_code,ID))

    
    def batch_item_converter(self)->list:
        items_list = []
        for item in self.items:
            items_list.append({
            "id":item.ID,
            "firstName":item.first_name,
            "lastName":item.last_name,
            "countryIso2":item.country_code,})
        
        return items_list

class US_ZipRaceEthnicityBatch(Batch):
    class US_ZipRaceEthnicityBatchItem(BatchItem):

        def __init__(self, first_name: str, last_name: str,  country_code: CountryCodes, zip_code:str,  ID = "unassigned"):
            self.ID = ID
            self.first_name = first_name
            self.last_name = last_name
            self.country_code = country_code.value
            self.zip_code = zip_code


    url = "usZipRaceEthnicityBatch"

    def __init__(self):
        self.items = []
        self.response_type = RaceEthnicityResponse
    

    
    def addItem(self, first_name: str, last_name: str,  country_code: CountryCodes, zip_code: str, ID = "unassigned"):
        super().addItem(self.US_ZipRaceEthnicityBatchItem(first_name,last_name,country_code,zip_code,ID))

    
    def batch_item_converter(self)->list:
        items_list = []
        for item in self.items:
            items_list.append({
            "id":item.ID,
            "firstName":item.first_name,
            "lastName":item.last_name,
            "countryIso2":item.country_code,
            "zipCode":item.zip_code,})
        
        return items_list


class DiasporaBatch(Batch):
    class DiasporaBatchItem(BatchItem):
         def __init__(self, first_name: str, last_name: str,  country_code: CountryCodes,   ID = "unassigned"):
            self.ID = ID
            self.first_name = first_name
            self.last_name = last_name
            self.country_code = country_code.value

    url = "diasporaBatch"

    def __init__(self):
        self.items = []
        self.response_type = DiasporaResponse
    
    def addItem(self, first_name: str, last_name: str,  country_code: CountryCodes,   ID = "unassigned"):
        super().addItem(self.DiasporaBatchItem(first_name,last_name,country_code,ID))

    
    def batch_item_converter(self)->list:
        items_list = []
        for item in self.items:
            items_list.append({
            "id":item.ID,
            "firstName":item.first_name,
            "lastName":item.last_name,
            "countryIso2":item.country_code,})
        
        return items_list
    
class ParseNameBatch(Batch):

    class ParseNameBatchItem(BatchItem):

        def __init__(self, name: str,  ID = "unassigned"):
            self.ID = ID
            self.name = name


    url = "parseNameBatch"

    def __init__(self):
        self.items = []
        self.response_type = ParseNameResponse
    
    def addItem(self, name: str,  ID = "unassigned"):
        super().addItem(self.ParseNameBatchItem(name, ID))

    
    def batch_item_converter(self)->list:
        items_list = []
        for item in self.items:
            items_list.append({
                "id":item.ID,
                "name":item.name,
            })
        
        return items_list

class ParseNameGeoBatch(Batch):

    class ParseNameGeoBatchItem(BatchItem):

        def __init__(self, name: str, country_code: CountryCodes, ID = "unassigned"):
            self.ID = ID
            self.name = name
            self.country_code = country_code.value


    url = "parseNameBatch"

    def __init__(self):
        self.items = []
        self.response_type = ParseNameResponse
    
    def addItem(self, name: str, country_code: CountryCodes, ID = "unassigned"):
        super().addItem(self.ParseNameGeoBatchItem(name, country_code, ID))

    
    def batch_item_converter(self)->list:
        items_list = []
        for item in self.items:
            items_list.append({
                "id":item.ID,
                "name":item.name,
                "countryIso2":item.country_code,
            })
        
        return items_list