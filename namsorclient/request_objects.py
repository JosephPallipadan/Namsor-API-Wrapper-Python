import math
import time
import xlsxwriter
import re
from abc import ABC, abstractmethod
import requests

import faker
import random

from namsorclient.models import GenderResponse
from namsorclient.models import GenderFullResponse
from namsorclient.models import OriginResponse
from namsorclient.models import CountryResponse
from namsorclient.models import RaceEthnicityResponse
from namsorclient.models import DiasporaResponse
from namsorclient.models import ParseNameResponse
from namsorclient.models import NameParserTypeWrapper
from namsorclient.models import FirstLastNameWrapper
from namsorclient.country_codes import CountryCodes
from namsorclient.sample_batch_responses import Sample_Responses


class BatchItem(ABC):
    """ An abstract class representing a general batch item.
    """
    pass


class Batch(ABC):
    """ An abstract class representing a general batch in which items can be added.
    """

    response = []

    @abstractmethod
    def batch_item_converter(self):
        pass

    @abstractmethod
    def addItem(self, item: BatchItem):
        """ An abstract method that appends an item of type BatchItem (any subclass of BatchItem) to items, a list.
        Args:
            item (BatchItem): The item of type BatchItem (any subclass of BatchItem) which is to be 
            appended to items, a list.
        """
        self.items.append(item)

    def api_post(self, url: str, data: dict, api_key: str) -> requests.models.Response:
        """ Returns a response containing desired information of the data.
        Args:
            url (str): Ending portion of NamsorAPI url to desired section.
            data (dict): The high throughput data to process.
        Returns:
            requests.models.Response: The response received from this POST request.
        """
        BASE_URL = "https://v2.namsor.com/NamSorAPIv2/api2/json/"
        r = requests.post(url=f"{BASE_URL}{url}", headers={"X-API-KEY":
                                                           api_key}, json=data)
        if r.status_code == 401:
            # The client has not entered his/her API key or the API key is incorrect.
            raise Exception('Invalid API Key')
        elif r.status_code == 403:
            # The client's amount of requests has reached the maximum amount he/she can send in a month or his/her subscription plan has been cancelled.
            raise Exception("API Limit Reached or API Key Disabled")
        return r

    def classify(self, api_key: str) -> list:
        """ Takes in the user's API key and returns responses of this batch's request(s) and response type in the form of a list.

        Args:
            api_key (str): The user's API key.

        Returns:
            list: A list of responses of this batch's response type.
        """

        # Stores the batch's items' data in appropriate JSON format in personal_names_list
        personal_names_list = self.batch_item_converter()
        
        response_list = []
        # Data is separated into blocks to bypass the 100 item limit
        item_list = list_separator(personal_names_list)

        for item in item_list:
            # Data is to be put in the appropriate format and be passed in as an argument of the POST request
            payload = {}
            payload['personalNames'] = item
            response = self.api_post(url=self.url, data=payload, api_key=api_key).json()[
                'personalNames']

            # This response from the POST request is appended to the previous responses
            self.response += response
            print(response)
            for i in range(len(response)):
                response_list.append(self.response_type(response[i]))
            # A one second delay for latency
            time.sleep(1)

        return response_list

    def export_to_excel(self, file_name: str):
        """ Creates an excel file and represents the batch's items' data in a spreadsheet form.

        Args:
            file_name (str): The desired Excel file name.
        """
        # Creates a Excel workbook, with the desired file name, and a worksheet.
        workbook = xlsxwriter.Workbook(file_name)
        worksheet = workbook.add_worksheet()


        for column, item in enumerate(self.response[0].keys()):

            # Regex to convert the keys from camel-case to Capital Case separated by hyphens
            # Eg: firstName to First-Name
            match = re.match(
                r'([a-z]+)([A-Z]*[a-z]*)([A-Z]*[a-z]*)([A-Z]*[a-z]*)', item).groups()
            row_title = '-'.join([i[0].upper() + i[1:]
                                  for i in match if i != ''])
            worksheet.write(0, column, row_title)

        # Adds the responses' data to their appropriate cells.
        for num, item in enumerate(self.response):
            for column, value in enumerate(item.values()):
                worksheet.write(num+1, column, str(value))

        workbook.close()


class GenderBatch(Batch):
    """
        A class representing a batch of items whose data is used to infer the likely gender of multiple names, detecting automatically the cultural context.
        Attributes:
            url (str): Ending portion of NamsorAPI url to desired section.
            items (list): A list of all batch items added by the user.
            response_type: The type of response a POST request for this batch will return.
    """
    class GenderBatchItem(BatchItem):
        """ 
            A class representing an item of a GenderBatch object that contains necessary data which is inputted by the user.
            Attributes:
               ID (str): The ID of the item.
               first_name (str): The desired first name.
               last_name (str): The desired last name.
        """

        def __init__(self, first_name: str, last_name: str, ID="unassigned"):
            """ Constructor

            Args:
                first_name (str): The desired first name.
                last_name (str): The desired last name.
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
        """ Adds a GenderBatchItem, with the required input, to the batch.
        Args:
            first_name (str): The desired first name.
            last_name (str): The desired last name.
            ID (str, optional): The ID of the item. Defaults to "unassigned".
        """
        super().addItem(self.GenderBatchItem(first_name, last_name, ID))

    def batch_item_converter(self) -> list:
        """ Converts all the batch's items' data into a list of dictionaries.
        Returns:
            list: A list of dictionaries each containing each batch item's data.
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
            url (str): Ending portion of NamsorAPI url to desired section.
            items (list): A list of all batch items added by the user.
            response_type: The type of response a POST request for this batch will return.
    """
    class GenderGeoBatchItem(BatchItem):
        """ 
            A class representing an item of a GenderGeoBatch object that contains necessary data which is inputted by the user.
            Attributes:
               ID (str): The ID of the item.
               first_name (str): The desired first name.
               last_name (str): The desired last name.
               country_code (CountryCodes): The desired country code.
        """

        def __init__(self, first_name: str, last_name: str, country_code: CountryCodes, ID="unassigned"):
            """Constructor
            Args:
                first_name (str): The desired first name.
                last_name (str): The desired last name.
                country_code (CountryCodes): The desired country code.
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
        """ Adds a GenderGeoBatchItem, with the required input, to the batch.
        Args:
            first_name (str): The desired first name.
            last_name (str): The desired last name.
            country_code (CountryCodes): The desired country code.
            ID (str, optional): The ID of the item. Defaults to "unassigned".
        """
        super().addItem(self.GenderGeoBatchItem(first_name, last_name, country_code, ID))

    def batch_item_converter(self) -> list:
        """ Converts all the batch's items' data into a list of dictionaries.
        Returns:
            list: A list of dictionaries each containing each batch item's data.
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
            url (str): Ending portion of NamsorAPI url to desired section.
            items (list): A list of all batch items added by the user.
            response_type: The type of response a POST request for this batch will return.
    """
    class ParsedGenderBatchItem(BatchItem):
        """ 
            A class representing an item of a ParsedGenderBatch object that contains necessary data which is inputted by the user.
            Attributes:
               ID (str): The ID of the item.
               first_name (str): The desired first name.
               last_name (str): The desired last name.
               prefix_or_title (str): The desired prefix or title.
               suffix (str): The desired suffix.
               middle_name (str): The desired middle name.
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
        """ Adds a ParsedGenderBatchItem, with the required input, to the batch.
        Args:
            first_name (str): The desired first name.
            last_name (str): The desired last name.
            prefix_or_title (str): The desired prefix or title
            suffix (str): The desired suffix
            middle_name (str): The desired middle name
            ID (str, optional): The ID of the item. Defaults to "unassigned".
        """
        super().addItem(self.ParsedGenderBatchItem(first_name,
                                                   last_name, prefix_or_title, suffix, middle_name, ID))

    def batch_item_converter(self) -> list:
        """ Converts all the batch's items' data into a list of dictionaries.
        Returns:
            list: A list of dictionaries each containing each batch item's data.
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
            url (str): Ending portion of NamsorAPI url to desired section.
            items (list): A list of all batch items added by the user.
            response_type: The type of response a POST request for this batch will return.
    """
    class ParsedGenderGeoBatchItem(BatchItem):
        """ 
            A class representing an item of a ParsedGenderGeoBatch object that contains necessary data which is inputted by the user.
            Attributes:
               ID (str): The ID of the item.
               first_name (str): The desired first name.
               last_name (str): The desired last name.
               prefix_or_title (str): The desired prefix or title
               suffix (str): The desired suffix
               middle_name (str): The desired middle name
               country_code (CountryCodes): The desired country code.
        """

        def __init__(self, first_name: str, last_name: str, prefix_or_title: str, suffix: str, middle_name: str, country_code: CountryCodes, ID="unassigned"):
            """Constructor
            Args:
                first_name (str): The desired first name.
                last_name (str): The desired last name.
                prefix_or_title (str): The desired prefix or title
                suffix (str): The desired suffix
                middle_name (str): The desired middle name
                country_code (CountryCodes): The desired country code.
                ID (str, optional): The ID of the item. Defaults to "unassigned".
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
        """ Adds a ParsedGenderGeoBatchItem, with the required input, to the batch.
        Args:
            first_name (str): The desired first name.
            last_name (str): The desired last name.
            prefix_or_title (str): The desired prefix or title
            suffix (str): The desired suffix
            middle_name (str): The desired middle name
            country_code (CountryCodes): The desired country code.
            ID (str, optional): The ID of the item. Defaults to "unassigned".
        """
        super().addItem(self.ParsedGenderGeoBatchItem(first_name, last_name,
                                                      prefix_or_title, suffix, middle_name, country_code, ID))

    def batch_item_converter(self) -> list:
        """ Converts all the batch's items' data into a list of dictionaries.
        Returns:
            list: A list of dictionaries each containing each batch item's data.
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
            url (str): Ending portion of NamsorAPI url to desired section.
            items (list): A list of all batch items added by the user.
            response_type: The type of response a POST request for this batch will return.
    """
    class GenderFullBatchItem(BatchItem):
        """ 
            A class representing an item of a GenderFullBatch object that contains necessary data which is inputted by the user.
            Attributes:
               ID (str): The ID of the item.
               name (str): The desired name.
        """

        def __init__(self, name: str, ID="unassigned"):
            """Constructor
            Args:
                name (str): The desired name.
                ID (str, optional): The ID of the item. Defaults to "unassigned".
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
        self.response_type = GenderFullResponse

    def addItem(self, name: str, ID="unassigned"):
        """ Adds a GenderFullBatchItem, with the required input, to the batch.
        Args:
            name (str): The desired name.
            ID (str, optional): The ID of the item. Defaults to "unassigned".
        """
        super().addItem(self.GenderFullBatchItem(name, ID))

    def batch_item_converter(self) -> list:
        """ Converts all the batch's items' data into a list of dictionaries.
        Returns:
            list: A list of dictionaries each containing each batch item's data.
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
            url (str): Ending portion of NamsorAPI url to desired section.
            items (list): A list of all batch items added by the user.
            response_type: The type of response a POST request for this batch will return.
    """
    class GenderFullGeoBatchItem(BatchItem):
        """ 
            A class representing an item of a GenderFullGeoBatch object that contains necessary data which is inputted by the user.
            Attributes:
               ID (str): The ID of the item.
               name (str): The desired name.
               country_code (CountryCodes): The desired country code.
        """

        def __init__(self, name: str,  country_code: CountryCodes,  ID="unassigned"):
            """ Constructor
            Args:
                name (str): The desired name.
                country_code (CountryCodes): The desired country code.
                ID (str, optional): The ID of the item. Defaults to "unassigned".
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
        self.response_type = GenderFullResponse

    def addItem(self, name: str,  country_code: CountryCodes,  ID="unassigned"):
        """ Adds a GenderFullGeoBatchItem, with the required input, to the batch.
        Args:
            name (str): The desired name.
            country_code (CountryCodes): The desired country code.
            ID (str, optional): The ID of the item. Defaults to "unassigned".
        """
        super().addItem(self.GenderFullGeoBatchItem(name, country_code, ID))

    def batch_item_converter(self) -> list:
        """ Converts all the batch's items' data into a list of dictionaries.
        Returns:
            list: A list of dictionaries each containing each batch item's data.
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
        A class representing a batch of items whose data is used to infer the likely country of origin of multiple names, detecting automatically the cultural context.
        Attributes:
            url (str): Ending portion of NamsorAPI url to desired section.
            items (list): A list of all batch items added by the user.
            response_type: The type of response a POST request for this batch will return.
    """
    class OriginBatchItem(BatchItem):
        """ 
            A class representing an item of an OriginBatchItem object that contains necessary data which is inputted by the user.
            Attributes:
               ID (str): The ID of the item.
               first_name (str): The desired first name.
               last_name (str): The desired last name.
        """

        def __init__(self, first_name: str, last_name: str,  ID="unassigned"):
            """Constructor
            Args:
                first_name (str): The desired first name.
                last_name (str): The desired last name.
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
        """ Adds a OriginBatchItem, with the required input, to the batch.
        Args:
            first_name (str): The desired first name.
            last_name (str): The desired last name.
            ID (str, optional): The ID of the item. Defaults to "unassigned".
        """
        super().addItem(self.OriginBatchItem(first_name, last_name, ID))

    def batch_item_converter(self) -> list:
        """ Converts all the batch's items' data into a list of dictionaries.
        Returns:
            list: A list of dictionaries each containing each batch item's data.
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
            url (str): Ending portion of NamsorAPI url to desired section.
            items (list): A list of all batch items added by the user.
            response_type: The type of response a POST request for this batch will return.
    """
    class CountryBatchItem(BatchItem):
        """ 
            A class representing an item of an OriginBatchItem object that contains necessary data which is inputted by the user.
            Attributes:
               ID (str): The ID of the item.
               first_name (str): The desired first name.
               last_name (str): The desired last name.
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
        """ Adds a CountryBatchItem, with the required input, to the batch. 
        Args:
            name (str): The desired name
            ID (str, optional): The ID of the item. Defaults to "unassigned".
        """
        super().addItem(self.CountryBatchItem(name, ID))

    def batch_item_converter(self) -> list:
        """ Converts all the batch's items' data into a list of dictionaries.
        Returns:
            list: A list of dictionaries each containing each batch item's data.
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
            url (str): Ending portion of NamsorAPI url to desired section.
            items (list): A list of all batch items added by the user.
            response_type: The type of response a POST request for this batch will return.
    """
    class US_RaceEthnicityBatchItem(BatchItem):
        """ 
            A class representing an item of a US_RaceEthnicityBatch object that contains necessary data which is inputted by the user.
            Attributes:
               ID (str): The ID of the item.
               first_name (str): The desired first name.
               last_name (str): The desired last name.
               country_code (CountryCodes): The desired country code.
        """

        def __init__(self, first_name: str, last_name: str,  country_code: CountryCodes,   ID="unassigned"):
            """Constructor
            Args:
                first_name (str): The desired first name.
                last_name (str): The desired last name.
                country_code (CountryCodes): The desired country code.
                ID (str, optional): The ID of the item. Defaults to "unassigned".
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
        """ Adds a US_RaceEthnicityBatchItem, with the required input, to the batch. 
        Args:
            first_name (str): The desired first name.
            last_name (str): The desired last name.
            country_code (CountryCodes): The desired country code.
            ID (str, optional): The ID of the item. Defaults to "unassigned".
        """
        super().addItem(self.US_RaceEthnicityBatchItem(
            first_name, last_name, country_code, ID))

    def batch_item_converter(self) -> list:
        """ Converts all the batch's items' data into a list of dictionaries.
        Returns:
            list: A list of dictionaries each containing each batch item's data.
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
        A class representing a batch of items whose data is used to infer a US resident's likely race/ethnicity according to US Census taxonomy, using ZIP5 code info. Output is W_NL (white, non latino), HL (hispano latino),  A (asian, non latino), B_NL (black, non latino).
        Attributes:
            url (str): Ending portion of NamsorAPI url to desired section.
            items (list): A list of all batch items added by the user.
            response_type: The type of response a POST request for this batch will return.
    """
    class US_ZipRaceEthnicityBatchItem(BatchItem):
        """ 
            A class representing an item of a US_ZipRaceEthnicityBatch object that contains necessary data which is inputted by the user.
            Attributes:
               ID (str): The ID of the item.
               first_name (str): The desired first name.
               last_name (str): The desired last name.
               country_code (CountryCodes): The desired country code.
               zip_code (str): The desired zip code.
        """

        def __init__(self, first_name: str, last_name: str,  country_code: CountryCodes, zip_code: str,  ID="unassigned"):
            """Constructor
            Args:
                first_name (str): The desired first name.
                last_name (str): The desired last name.
                country_code (CountryCodes): The desired country code.
                zip_code (str): The desired zip code.
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
        """ Adds a CountryBatchItem, with the required input, to the batch. 
        Args:
            first_name (str): The desired first name.
            last_name (str): The desired last name.
            country_code (CountryCodes): The desired country code.
            zip_code (str): The desired zip code.
            ID (str, optional): The ID of the item. Defaults to "unassigned".
        """
        super().addItem(self.US_ZipRaceEthnicityBatchItem(
            first_name, last_name, country_code, zip_code, ID))

    def batch_item_converter(self) -> list:
        """ Converts all the batch's items' data into a list of dictionaries.
        Returns:
            list: A list of dictionaries each containing each batch item's data.
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
            url (str): Ending portion of NamsorAPI url to desired section.
            items (list): A list of all batch items added by the user.
            response_type: The type of response a POST request for this batch will return.
    """
    class DiasporaBatchItem(BatchItem):
        """ 
            A class representing an item of a DiasporaBatch object that contains necessary data which is inputted by the user.
            Attributes:
               ID (str): The ID of the item.
               first_name (str): The desired first name.
               last_name (str): The desired last name.
               country_code (CountryCodes): The desired country code.
        """

        def __init__(self, first_name: str, last_name: str,  country_code: CountryCodes,   ID="unassigned"):
            """Constructor
            Args:
                first_name (str): The desired first name.
                last_name (str): The desired last name.
                country_code (CountryCodes): The desired country code.
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
        """ Adds a DiasporaBatchItem, with the required input, to the batch. 
        Args:
            first_name (str): The desired first name.
            last_name (str): The desired last name.
            country_code (CountryCodes): The desired country code.
            ID (str, optional): The ID of the item. Defaults to "unassigned".
        """
        super().addItem(self.DiasporaBatchItem(first_name, last_name, country_code, ID))

    def batch_item_converter(self) -> list:
        """ Converts all the batch's items' data into a list of dictionaries.
        Returns:
            list: A list of dictionaries each containing each batch item's data.
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
            url (str): Ending portion of NamsorAPI url to desired section.
            items (list): A list of all batch items added by the user.
            response_type: The type of response a POST request for this batch will return.
    """
    class ParseNameBatchItem(BatchItem):
        """ 
            A class representing an item of a ParseNameBatch object that contains necessary data which is inputted by the user.
            Attributes:
               ID (str): The ID of the item.
               name (str): The desired name.
        """

        def __init__(self, name: str,  ID="unassigned"):
            """Constructor
            Args:
                name (str): The desired name.
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
        """ Adds a ParseNameBatchItem, with the required input, to the batch. 
        Args:
            name (str): The desired name.
            ID (str, optional): The ID of the item. Defaults to "unassigned".
        """
        super().addItem(self.ParseNameBatchItem(name, ID))

    def batch_item_converter(self) -> list:
        """ Converts all the batch's items' data into a list of dictionaries.
        Returns:
            list: A list of dictionaries each containing each batch item's data.
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
            url (str): Ending portion of NamsorAPI url to desired section.
            items (list): A list of all batch items added by the user.
            response_type: The type of response a POST request for this batch will return.
    """
    class ParseNameGeoBatchItem(BatchItem):
        """ 
            A class representing an item of a ParseNameGeoBatch object that contains necessary data which is inputted by the user.
            Attributes:
               ID (str): The ID of the item.
               name (str): The desired name.
               country_code (CountryCodes): The desired country code.
        """

        def __init__(self, name: str, country_code: CountryCodes, ID="unassigned"):
            """Constructor
            Args:
                name (str): The desired name.
                country_code (CountryCodes): The desired country code.
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
        """ Adds a ParseNameGeoBatchItem, with the required input, to the batch. 
        Args:
            name (str): The desired name
            country_code (CountryCodes): The desired country code.
            ID (str, optional): The ID of the item. Defaults to "unassigned".
        """
        super().addItem(self.ParseNameGeoBatchItem(name, country_code, ID))

    def batch_item_converter(self) -> list:
        """ Converts all the batch's items' data into a list of dictionaries.
        Returns:
            list: A list of dictionaries each containing each batch item's data.
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
    """ Function used to transform the batch arrays into blocks to bypass the 100 item limit.
    Args:
        data (list): The list to be separated.
    Returns:
        list: A list of lists each having a maximum of 100 items.
    """

    big_list = []
    total_num = math.ceil(len(data)/100)
    for i in range(total_num):
        big_list.append(data[i*100:(i+1)*100])
    return big_list



