import math
from models import *
from abc import ABC, abstractmethod
from country_codes import CountryCodes


class BatchItem(ABC):
    """ An abstract class representing a general batch item
    """
    pass


class Batch(ABC):
    """ An abstract class representing a general batch in which items can be added
    """
    @abstractmethod
    def batch_item_converter(self):
        pass

    @abstractmethod
    def addItem(self, item: BatchItem):
        """ An abstract method that appends an item of type BatchItem (any subclass of BatchItem) to items, a list

        Args:
            item (BatchItem): the item of type BatchItem (any subclass of BatchItem) which is to be 
            appended to items, a list
        """
        self.items.append(item)


class GenderBatch(Batch):
    """
        A class representing a batch of items whose data is used to infer the likely gender of multiple names, detecting automatically the cultural context.

        Attributes:
            url (str): ending portion of NamsorAPI url to desired section.
            items (list): a list of GenderBatchItem objects
            response_type: the type of response a POST request for this batch will return

    """
    class GenderBatchItem(BatchItem):
        """ 
            A class representing an item of a GenderBatch object that contains necessary data which is inputted by the user

            Attributes:
               ID (str): The ID of the item
               first_name (str): The desired first name
               last_name (str): The desired last name
        """

        def __init__(self, first_name: str, last_name: str, ID="unassigned"):
            """ Constructor

            Args:
                first_name (str): The desired first name
                last_name (str): The desired last name
                ID (str, optional): The ID of the item. Defaults to "unassigned".
            """
            self.ID = ID
            self.first_name = first_name
            self.last_name = last_name

    url = "genderBatch"
    items = []
    response_type = None

    def __init__(self):
        """Constructor
        """
        self.items = []
        self.response_type = GenderResponse

    def addItem(self, first_name: str, last_name: str, ID="unassigned"):
        """ Adds a GenderBatchItem, with the required input, to the batch

        Args:
            first_name (str): The desired first name
            last_name (str): The desired last name
            ID (str, optional): The ID of the item. Defaults to "unassigned".
        """
        super().addItem(self.GenderBatchItem(first_name, last_name, ID))

    def batch_item_converter(self) -> list:
        """ Converts all the batch's items' data into a list of dictionaries

        Returns:
            list: a list of dictionaries each containing each batch item's data
        """
        items_list = []
        for item in self.items:
            items_list.append({
                "id": item.ID,
                "firstName": item.first_name,
                "lastName": item.last_name,
            })

        return items_list


class GenderGeoBatch(Batch):
    """
        A class representing a batch of items whose data is used to infer the likely gender of multiple names, each given a local context (ISO2 country code).

        Attributes:
            url (str): ending portion of NamsorAPI url to desired section.
            items (list): a list of all batch items added by the user
            response_type: the type of response a POST request for this batch will return

    """
    class GenderGeoBatchItem(BatchItem):
        """ 
            A class representing an item of a GenderGeoBatch object that contains necessary data which is inputted by the user

            Attributes:
               ID (str): The ID of the item
               first_name (str): The desired first name
               last_name (str): The desired last name
               country_code (CountryCodes): The desired country code

        """

        def __init__(self, first_name: str, last_name: str, country_code: CountryCodes, ID="unassigned"):
            """Constructor

            Args:
                first_name (str): The desired first name
                last_name (str): The desired last name
                country_code (CountryCodes): The desired country code

                ID (str, optional): the ID of the item. Defaults to "unassigned".
            """
            self.ID = ID
            self.first_name = first_name
            self.last_name = last_name
            self.country_code = country_code.value

    url = "genderGeoBatch"
    items = []
    response_type = None

    def __init__(self):
        """Constructor
        """
        self.items = []
        self.response_type = GenderResponse

    def addItem(self, first_name: str, last_name: str, country_code: CountryCodes, ID="unassigned"):
        """ Adds a GenderGeoBatchItem, with the required input, to the batch

        Args:
            first_name (str): The desired first name
            last_name (str): The desired last name
            country_code (CountryCodes): The desired country code

            ID (str, optional): The ID of the item. Defaults to "unassigned".
        """
        super().addItem(self.GenderGeoBatchItem(first_name, last_name, country_code, ID))

    def batch_item_converter(self) -> list:
        """ Converts all the batch's items' data into a list of dictionaries

        Returns:
            list: a list of dictionaries each containing each batch item's data
        """
        items_list = []
        for item in self.items:
            items_list.append({
                "id": item.ID,
                "firstName": item.first_name,
                "lastName": item.last_name,
                "countryIso2": item.country_code
            })

        return items_list


class ParsedGenderBatch(Batch):
    """
        A class representing a batch of items whose data is used to infer the likely gender of multiple fully parsed names, detecting automatically the cultural context.

        Attributes:
            url (str): ending portion of NamsorAPI url to desired section.
            items (list): a list of all batch items added by the user
            response_type: the type of response a POST request for this batch will return

    """
    class ParsedGenderBatchItem(BatchItem):
        """ 
            A class representing an item of a ParsedGenderBatch object that contains necessary data which is inputted by the user

            Attributes:
               ID (str): The ID of the item
               first_name (str): The desired first name
               last_name (str): The desired last name
               prefix_or_title (str): The desired prefix or title
               suffix (str): The desired suffix
               middle_name (str): The desired middle name
        """

        def __init__(self, first_name: str, last_name: str, prefix_or_title: str, suffix: str, middle_name: str, ID="unassigned"):
            self.ID = ID
            self.first_name = first_name
            self.last_name = last_name
            self.prefix_or_title = prefix_or_title
            self.suffix = suffix
            self.middle_name = middle_name

    url = "parsedGenderBatch"
    items = []
    response_type = None

    def __init__(self):
        """Constructor
        """
        self.items = []
        self.response_type = GenderResponse

    def addItem(self, first_name: str, last_name: str, prefix_or_title: str, suffix: str, middle_name: str, ID="unassigned"):
        """ Adds a ParsedGenderBatchItem, with the required input, to the batch

        Args:
            first_name (str): The desired first name
            last_name (str): The desired last name
            prefix_or_title (str): The desired prefix or title
            suffix (str): The desired suffix
            middle_name (str): The desired middle name
            ID (str, optional): The ID of the item. Defaults to "unassigned".
        """
        super().addItem(self.ParsedGenderBatchItem(first_name,
                                                   last_name, prefix_or_title, suffix, middle_name, ID))

    def batch_item_converter(self) -> list:
        """ Converts all the batch's items' data into a list of dictionaries

        Returns:
            list: a list of dictionaries each containing each batch item's data
        """
        items_list = []
        for item in self.items:
            items_list.append({
                "id": item.ID,
                "firstName": item.first_name,
                "lastName": item.last_name,
                "prefixOrTitle": item.prefix_or_title,
                "suffix": item.suffix,
                "middleName": item.middle_name,
            })

        return items_list


class ParsedGenderGeoBatch(Batch):
    """
        A class representing a batch of items whose data is used to infer the likely gender of multiple fully parsed names, detecting automatically the cultural context.

        Attributes:
            url (str): ending portion of NamsorAPI url to desired section.
            items (list): a list of all batch items added by the user
            response_type: the type of response a POST request for this batch will return

    """
    class ParsedGenderGeoBatchItem(BatchItem):
        """ 
            A class representing an item of a ParsedGenderGeoBatch object that contains necessary data which is inputted by the user

            Attributes:
               ID (str): The ID of the item
               first_name (str): The desired first name
               last_name (str): The desired last name
               prefix_or_title (str): The desired prefix or title
               suffix (str): The desired suffix
               middle_name (str): The desired middle name
               country_code (CountryCodes): The desired country code
        """

        def __init__(self, first_name: str, last_name: str, prefix_or_title: str, suffix: str, middle_name: str, country_code: CountryCodes, ID="unassigned"):
            """Constructor

            Args:
                first_name (str): The desired first name
                last_name (str): The desired last name
                prefix_or_title (str): The desired prefix or title
                suffix (str): The desired suffix
                middle_name (str): The desired middle name
                country_code (CountryCodes): The desired country code
                ID (str, optional): The ID of the time. Defaults to "unassigned".
            """
            self.ID = ID
            self.first_name = first_name
            self.last_name = last_name
            self.prefix_or_title = prefix_or_title
            self.suffix = suffix
            self.middle_name = middle_name
            self.country_code = country_code.value

    url = "parsedGenderGeoBatch"
    items = []
    response_type = None

    def __init__(self):
        """Constructor
        """
        self.items = []
        self.response_type = GenderResponse

    def addItem(self, first_name: str, last_name: str, prefix_or_title: str, suffix: str, middle_name: str, country_code: CountryCodes, ID="unassigned"):
        """ Adds a ParsedGenderGeoBatchItem, with the required input, to the batch

        Args:
            first_name (str): The desired first name
            last_name (str): The desired last name
            prefix_or_title (str): The desired prefix or title
            suffix (str): The desired suffix
            middle_name (str): The desired middle name
            country_code (CountryCodes): The desired country code
            ID (str, optional): The ID of the time. Defaults to "unassigned".
        """
        super().addItem(self.ParsedGenderGeoBatchItem(first_name, last_name,
                                                      prefix_or_title, suffix, middle_name, country_code, ID))

    def batch_item_converter(self) -> list:
        """ Converts all the batch's items' data into a list of dictionaries

        Returns:
            list: a list of dictionaries each containing each batch item's data
        """
        items_list = []
        for item in self.items:
            items_list.append({
                "id": item.ID,
                "firstName": item.first_name,
                "lastName": item.last_name,
                "prefixOrTitle": item.prefix_or_title,
                "suffix": item.suffix,
                "middleName": item.middle_name,
                "countryIso2": item.country_code
            })

        return items_list


class GenderFullBatch(Batch):
    """
        A class representing a batch of items whose data is used to infer the likely gender of multiple full names, detecting automatically the cultural context.

        Attributes:
            url (str): ending portion of NamsorAPI url to desired section.
            items (list): a list of all batch items added by the user
            response_type: the type of response a POST request for this batch will return

    """
    class GenderFullBatchItem(BatchItem):
        """ 
            A class representing an item of a GenderFullBatch object that contains necessary data which is inputted by the user

            Attributes:
               ID (str): The ID of the item
               name (str): The desired name.
        """

        def __init__(self, name: str, ID="unassigned"):
            """Constructor

            Args:
                name (str): The desired name.
                ID (str, optional): The ID of the time. Defaults to "unassigned".
            """
            self.ID = ID
            self.name = name

    url = "genderFullBatch"
    items = []
    response_type = None

    def __init__(self):
        """Constructor
        """
        self.items = []
        self.response_type = GenderResponse

    def addItem(self, name: str, ID="unassigned"):
        """ Adds a GenderFullBatchItem, with the required input, to the batch

        Args:
            name (str): The desired name.
            ID (str, optional): The ID of the time. Defaults to "unassigned".
        """
        super().addItem(self.GenderFullBatchItem(name, ID))

    def batch_item_converter(self) -> list:
        """ Converts all the batch's items' data into a list of dictionaries

        Returns:
            list: a list of dictionaries each containing each batch item's data
        """
        items_list = []
        for item in self.items:
            items_list.append({
                "id": item.ID,
                "name": item.name,
            })

        return items_list


class GenderFullGeoBatch(Batch):
    """
        A class representing a batch of items whose data is used to infer the likely gender of multiple full names, with a given cultural context (country ISO2 code).

        Attributes:
            url (str): ending portion of NamsorAPI url to desired section.
            items (list): a list of all batch items added by the user
            response_type: the type of response a POST request for this batch will return

    """
    class GenderFullGeoBatchItem(BatchItem):
        """ 
            A class representing an item of a GenderFullGeoBatch object that contains necessary data which is inputted by the user

            Attributes:
               ID (str): The ID of the item
               name (str): The desired name.
               country_code (CountryCodes): The desired country code
        """

        def __init__(self, name: str,  country_code: CountryCodes,  ID="unassigned"):
            """ Constructor

            Args:
                name (str): The desired name.
                country_code (CountryCodes): The desired country code
                ID (str, optional): The ID of the time. Defaults to "unassigned".
            """
            self.ID = ID
            self.name = name
            self.country_code = country_code.value

    url = "genderFullGeoBatch"
    items = []
    response_type = None

    def __init__(self):
        """Constructor
        """
        self.items = []
        self.response_type = GenderResponse

    def addItem(self, name: str,  country_code: CountryCodes,  ID="unassigned"):
        """ Adds a GenderFullGeoBatchItem, with the required input, to the batch

        Args:
            name (str): The desired name.
            country_code (CountryCodes): The desired country code
            ID (str, optional): The ID of the time. Defaults to "unassigned".
        """
        super().addItem(self.GenderFullGeoBatchItem(name, country_code, ID))

    def batch_item_converter(self) -> list:
        """ Converts all the batch's items' data into a list of dictionaries

        Returns:
            list: a list of dictionaries each containing each batch item's data
        """
        items_list = []
        for item in self.items:
            items_list.append({
                "id": item.ID,
                "name": item.name,
                "countryIso2": item.country_code,
            })

        return items_list


class OriginBatch(Batch):
    """
        A class representing a batch of items w hose data is used to infer the likely country of origin of multiple names, detecting automatically the cultural context.

        Attributes:
            url (str): ending portion of NamsorAPI url to desired section.
            items (list): a list of all batch items added by the user
            response_type: the type of response a POST request for this batch will return

    """
    class OriginBatchItem(BatchItem):
        """ 
            A class representing an item of an OriginBatchItem object that contains necessary data which is inputted by the user

            Attributes:
               ID (str): The ID of the item
               first_name (str): The desired first name
               last_name (str): The desired last name
        """

        def __init__(self, first_name: str, last_name: str,  ID="unassigned"):
            """Constructor

            Args:
                first_name (str): The desired first name
                last_name (str): The desired last name
                ID (str, optional): The ID of the item. Defaults to "unassigned".
            """
            self.ID = ID
            self.first_name = first_name
            self.last_name = last_name

    url = "originBatch"
    items = []
    response_type = None

    def __init__(self):
        """Constructor
        """
        self.items = []
        self.response_type = OriginResponse

    def addItem(self, first_name: str, last_name: str,  ID="unassigned"):
        """ Adds a OriginBatchItem, with the required input, to the batch

        Args:
            first_name (str): The desired first name
            last_name (str): The desired last name
            ID (str, optional): The ID of the item. Defaults to "unassigned".
        """
        super().addItem(self.OriginBatchItem(first_name, last_name, ID))

    def batch_item_converter(self) -> list:
        """ Converts all the batch's items' data into a list of dictionaries

        Returns:
            list: a list of dictionaries each containing each batch item's data
        """
        items_list = []
        for item in self.items:
            items_list.append({
                "id": item.ID,
                "firstName": item.first_name,
                "lastName": item.last_name,
            })

        return items_list


class CountryBatch(Batch):
    """
        A class representing a batch of items whose data is used to infer the likely country of residence of multiple personal full names, or surnames. Assumes names as they are in the country of residence OR the country of origin.

        Attributes:
            url (str): ending portion of NamsorAPI url to desired section.
            items (list): a list of all batch items added by the user
            response_type: the type of response a POST request for this batch will return

    """
    class CountryBatchItem(BatchItem):
        """ 
            A class representing an item of an OriginBatchItem object that contains necessary data which is inputted by the user

            Attributes:
               ID (str): The ID of the item
               first_name (str): The desired first name
               last_name (str): The desired last name
        """

        def __init__(self, name: str,  ID="unassigned"):
            """Constructor

            Args:
                name (str): The desired name
                ID (str, optional): The ID of the item. Defaults to "unassigned".
            """
            self.ID = ID
            self.name = name

    url = "countryBatch"
    items = []
    response_type = None

    def __init__(self):
        """Constructor
        """
        self.items = []
        self.response_type = CountryResponse

    def addItem(self, name: str,  ID="unassigned"):
        """ Adds a CountryBatchItem, with the required input, to the batch 

        Args:
            name (str): The desired name
            ID (str, optional): The ID of the item. Defaults to "unassigned".
        """
        super().addItem(self.CountryBatchItem(name, ID))

    def batch_item_converter(self) -> list:
        """ Converts all the batch's items' data into a list of dictionaries

        Returns:
            list: a list of dictionaries each containing each batch item's data
        """
        items_list = []
        for item in self.items:
            items_list.append({
                "id": item.ID,
                "name": item.name,
            })

        return items_list


class US_RaceEthnicityBatch(Batch):
    """
        A class representing a batch of items whose data is used to infer a US resident's likely race/ethnicity according to US Census taxonomy W_NL (white, non latino), HL (hispano latino),  A (asian, non latino), B_NL (black, non latino).

        Attributes:
            url (str): ending portion of NamsorAPI url to desired section.
            items (list): a list of all batch items added by the user
            response_type: the type of response a POST request for this batch will return

    """
    class US_RaceEthnicityBatchItem(BatchItem):
        """ 
            A class representing an item of a US_RaceEthnicityBatch object that contains necessary data which is inputted by the user

            Attributes:
               ID (str): The ID of the item
               first_name (str): The desired first name
               last_name (str): The desired last name
               country_code (CountryCodes): The desired country code
        """

        def __init__(self, first_name: str, last_name: str,  country_code: CountryCodes,   ID="unassigned"):
            """Constructor

            Args:
                first_name (str): The desired first name
                last_name (str): The desired last name
                country_code (CountryCodes): The desired country code
                ID (str, optional): [description]. Defaults to "unassigned".
            """
            self.ID = ID
            self.first_name = first_name
            self.last_name = last_name
            self.country_code = country_code.value

    url = "usRaceEthnicityBatch"
    items = []
    response_type = None

    def __init__(self):
        """Constructor
        """
        self.items = []
        self.response_type = RaceEthnicityResponse

    def addItem(self, first_name: str, last_name: str,  country_code: CountryCodes,   ID="unassigned"):
        """ Adds a US_RaceEthnicityBatchItem, with the required input, to the batch 

        Args:
            first_name (str): The desired first name
            last_name (str): The desired last name
            country_code (CountryCodes): The desired country code
            ID (str, optional): [description]. Defaults to "unassigned".
        """
        super().addItem(self.US_RaceEthnicityBatchItem(
            first_name, last_name, country_code, ID))

    def batch_item_converter(self) -> list:
        """ Converts all the batch's items' data into a list of dictionaries

        Returns:
            list: a list of dictionaries each containing each batch item's data
        """
        items_list = []
        for item in self.items:
            items_list.append({
                "id": item.ID,
                "firstName": item.first_name,
                "lastName": item.last_name,
                "countryIso2": item.country_code, })

        return items_list


class US_ZipRaceEthnicityBatch(Batch):
    """
        A class representing a batch of items whose data is used to infer a US resident's likely race/ethnicity according to US Census taxonomy, using (optional) ZIP5 code info. Output is W_NL (white, non latino), HL (hispano latino),  A (asian, non latino), B_NL (black, non latino).

        Attributes:
            url (str): ending portion of NamsorAPI url to desired section.
            items (list): a list of all batch items added by the user
            response_type: the type of response a POST request for this batch will return

    """
    class US_ZipRaceEthnicityBatchItem(BatchItem):
        """ 
            A class representing an item of a US_ZipRaceEthnicityBatch object that contains necessary data which is inputted by the user

            Attributes:
               ID (str): The ID of the item
               first_name (str): The desired first name
               last_name (str): The desired last name
               country_code (CountryCodes): The desired country code
               zip_code (str): The desired zip code
        """

        def __init__(self, first_name: str, last_name: str,  country_code: CountryCodes, zip_code: str,  ID="unassigned"):
            """Constructor

            Args:
                first_name (str): The desired first name
                last_name (str): The desired last name
                country_code (CountryCodes): The desired country code
                zip_code (str): The desired zip code
                ID (str, optional): The ID of the item. Defaults to "unassigned".
            """
            self.ID = ID
            self.first_name = first_name
            self.last_name = last_name
            self.country_code = country_code.value
            self.zip_code = zip_code

    url = "usZipRaceEthnicityBatch"
    items = []
    response_type = None

    def __init__(self):
        """Constructor
        """
        self.items = []
        self.response_type = RaceEthnicityResponse

    def addItem(self, first_name: str, last_name: str,  country_code: CountryCodes, zip_code: str, ID="unassigned"):
        """ Adds a CountryBatchItem, with the required input, to the batch 

        Args:
            first_name (str): The desired first name
            last_name (str): The desired last name
            country_code (CountryCodes): The desired country code
            zip_code (str): The desired zip code
            ID (str, optional): The ID of the item. Defaults to "unassigned".
        """
        super().addItem(self.US_ZipRaceEthnicityBatchItem(
            first_name, last_name, country_code, zip_code, ID))

    def batch_item_converter(self) -> list:
        """ Converts all the batch's items' data into a list of dictionaries

        Returns:
            list: a list of dictionaries each containing each batch item's data
        """
        items_list = []
        for item in self.items:
            items_list.append({
                "id": item.ID,
                "firstName": item.first_name,
                "lastName": item.last_name,
                "countryIso2": item.country_code,
                "zipCode": item.zip_code, })

        return items_list


class DiasporaBatch(Batch):
    """
        A class representing a batch of items whose data is used to infer the likely ethnicity/diaspora of up to 100 personal names, given a country of residence ISO2 code (ex. US, CA, AU, NZ etc.)

        Attributes:
            url (str): ending portion of NamsorAPI url to desired section.
            items (list): a list of all batch items added by the user
            response_type: the type of response a POST request for this batch will return

    """
    class DiasporaBatchItem(BatchItem):
        """ 
            A class representing an item of a DiasporaBatch object that contains necessary data which is inputted by the user

            Attributes:
               ID (str): The ID of the item
               first_name (str): The desired first name
               last_name (str): The desired last name
               country_code (CountryCodes): The desired country code
        """

        def __init__(self, first_name: str, last_name: str,  country_code: CountryCodes,   ID="unassigned"):
            """Constructor

            Args:
                first_name (str): The desired first name
                last_name (str): The desired last name
                country_code (CountryCodes): The desired country code
                ID (str, optional): The ID of the item. Defaults to "unassigned".
            """
            self.ID = ID
            self.first_name = first_name
            self.last_name = last_name
            self.country_code = country_code.value

    url = "diasporaBatch"
    items = []
    response_type = None

    def __init__(self):
        """Constructor
        """
        self.items = []
        self.response_type = DiasporaResponse

    def addItem(self, first_name: str, last_name: str,  country_code: CountryCodes,   ID="unassigned"):
        """ Adds a DiasporaBatchItem, with the required input, to the batch 

        Args:
            first_name (str): The desired first name
            last_name (str): The desired last name
            country_code (CountryCodes): The desired country code
            ID (str, optional): The ID of the item. Defaults to "unassigned".
        """
        super().addItem(self.DiasporaBatchItem(first_name, last_name, country_code, ID))

    def batch_item_converter(self) -> list:
        """ Converts all the batch's items' data into a list of dictionaries

        Returns:
            list: a list of dictionaries each containing each batch item's data
        """
        items_list = []
        for item in self.items:
            items_list.append({
                "id": item.ID,
                "firstName": item.first_name,
                "lastName": item.last_name,
                "countryIso2": item.country_code, })

        return items_list


class ParseNameBatch(Batch):
    """
        A class representing a batch of items whose data is used to infer the likely first/last name structure of a name, ex. John Smith or SMITH, John or SMITH; John.

        Attributes:
            url (str): ending portion of NamsorAPI url to desired section.
            items (list): a list of all batch items added by the user
            response_type: the type of response a POST request for this batch will return

    """
    class ParseNameBatchItem(BatchItem):
        """ 
            A class representing an item of a ParseNameBatch object that contains necessary data which is inputted by the user

            Attributes:
               ID (str): The ID of the item
               name (str): The desired name
        """

        def __init__(self, name: str,  ID="unassigned"):
            """Constructor

            Args:
                name (str): The desired name
                ID (str, optional): The ID of the item. Defaults to "unassigned".
            """
            self.ID = ID
            self.name = name

    url = "parseNameBatch"
    items = []
    response_type = None

    def __init__(self):
        """Constructor
        """
        self.items = []
        self.response_type = ParseNameResponse

    def addItem(self, name: str,  ID="unassigned"):
        """ Adds a ParseNameBatchItem, with the required input, to the batch 

        Args:
            name (str): The desired name
            ID (str, optional): The ID of the item. Defaults to "unassigned".
        """
        super().addItem(self.ParseNameBatchItem(name, ID))

    def batch_item_converter(self) -> list:
        """ Converts all the batch's items' data into a list of dictionaries

        Returns:
            list: a list of dictionaries each containing each batch item's data
        """
        items_list = []
        for item in self.items:
            items_list.append({
                "id": item.ID,
                "name": item.name,
            })

        return items_list


class ParseNameGeoBatch(Batch):
    """
        A class representing a batch of items whose data is used to infer the likely first/last name structure of a name, ex. John Smith or SMITH, John or SMITH; John. Giving a local context improves precision. 

        Attributes:
            url (str): ending portion of NamsorAPI url to desired section.
            items (list): a list of all batch items added by the user
            response_type: the type of response a POST request for this batch will return

    """
    class ParseNameGeoBatchItem(BatchItem):
        """ 
            A class representing an item of a ParseNameGeoBatch object that contains necessary data which is inputted by the user

            Attributes:
               ID (str): The ID of the item
               name (str): The desired name
               country_code (CountryCodes): The desired country code
        """

        def __init__(self, name: str, country_code: CountryCodes, ID="unassigned"):
            """Constructor

            Args:
                name (str): The desired name
                country_code (CountryCodes): The desired country code
                ID (str, optional): The ID of the item. Defaults to "unassigned".
            """
            self.ID = ID
            self.name = name
            self.country_code = country_code.value

    url = "parseNameBatch"
    items = []
    response_type = None

    def __init__(self):
        """Constructor
        """
        self.items = []
        self.response_type = ParseNameResponse

    def addItem(self, name: str, country_code: CountryCodes, ID="unassigned"):
        """ Adds a ParseNameGeoBatchItem, with the required input, to the batch 

        Args:
            name (str): The desired name
            country_code (CountryCodes): The desired country code
            ID (str, optional): The ID of the item. Defaults to "unassigned".
        """
        super().addItem(self.ParseNameGeoBatchItem(name, country_code, ID))

    def batch_item_converter(self) -> list:
        """ Converts all the batch's items' data into a list of dictionaries

        Returns:
            list: a list of dictionaries each containing each batch item's data
        """
        items_list = []
        for item in self.items:
            items_list.append({
                "id": item.ID,
                "name": item.name,
                "countryIso2": item.country_code,
            })

        return items_list


def list_separator(data: list) -> list:
    """ Separates list of dictionaries representing batch items' data into multiple lists each having a maximum of 100 dictionaries

    Args:
        data (list): a list of dictionaries each containing each batch item's data

    Returns:
        list: a list of lists each having a maximum of 100 dictionaries
    """
    big_list = []
    total_num = math.ceil(len(data)/100)
    for i in range(total_num):
        big_list.append(data[i*100:(i+1)*100])
    return big_list
