import requests

from country_codes import CountryCodes
from models import GenderResponse
from request_objects import *
import helpers
import json

BASE_URL = "https://v2.namsor.com/NamSorAPIv2/api2/json/"


class NamsorClient:
    """
    A class representing a NamsorAPI client

    Attributes:
        api_key(str): The Namsor API key of the user.
    """

    def __init__(self, api_key):
        self.api_key = api_key
        test_response = self.__api_get()
        if test_response.status_code == 401:
            raise Exception('Invalid API Key')
            # The client has not entered his/her API key or the API key is incorrect
        elif test_response.status_code == 403:
            raise Exception("API Limit Reached or API Key Disabled")
            # The client's amount of requests has reached the maximum amount he/she can send in a month or his/her subscription plan has been cancelled

    def __api_get(self, url="gender/Lelouch/Lamperouge") -> requests.models.Response:
        """ returns a response containing desired information of the data

        Args:
            url (str, optional): ending portion of NamsorAPI url to desired section. Defaults to "gender/Lelouch/Lamperouge".

        Returns:
            requests.models.Response: the response received from this GET request
        """
        return requests.get(url=f"{BASE_URL}{url}", headers={"X-API-KEY": self.api_key})

    def __api_post(self, url, data) -> requests.models.Response:
        """ returns a response containing desired information of the data

        Args:

            url (str): ending portion of NamsorAPI url to desired section 

            data (dict): the high throughput data to process

        Returns:
            requests.models.Response: the response received from this POST request
        """
        return requests.post(url=f"{BASE_URL}{url}", headers={"X-API-KEY": self.api_key}, json=data)

    def gender(self, first_name: str, last_name: str) -> GenderResponse:
        """ Infer the likely gender of a name.

        Args:
            first_name (str): The desired first name. 
            last_name (str): The desired last name.

        Returns:
            GenderResponse: An Object which is a wrapper of the API's response object for this particular endpoint.
        """

        url = f"gender/{first_name}/{last_name}"
        return GenderResponse(self.__api_get(url=url).json())

    def genderGeo(self, first_name: str, last_name: str, country_code: CountryCodes) -> GenderResponse:
        """Infer the likely gender of a name, given a local context (ISO2 country code).

        Args:
            first_name (str): The desired first name.
            last_name (str): The desired last name.
            country_code (CountryCodes): The country code, to be passed using the CountryCodes object.

        Returns:
            GenderResponse: An Object which is a wrapper of the API's response object for this particular endpoint.
        """
        url = f"genderGeo/{first_name}/{last_name}/{country_code.value}"
        return GenderResponse(self.__api_get(url=url))

    def genderBatch(self, item_group: GenderBatch) -> list:
        """Infer the likely gender of multiple names, detecting automatically the cultural context

        Args:
            data (list): a list of any number of dictionaries containing information on the id, first name, and last name


        Returns:
            list: a list of GenderResponse objects which are wrappers of the API's response object for this particular endpoint.
        """

        url = "genderBatch"
        personal_names_list = helpers.gender_batch_item_converter(item_group)

        gender_response_list = []
        item_list = helpers.list_seperator(personal_names_list)

        for item in item_list:
            payload = {}
            payload['personalNames'] = item
            a = self.__api_post(url=url, data=payload).json()['personalNames']
            for i in range(len(a)):
                gender_response_list.append(GenderResponse(a[i]))

        return gender_response_list

    def parsedGenderBatch(self, item_group: ParsedGenderBatch) -> list:
        url = "parsedGenderBatch"
        personal_names_list = helpers.gender_batch_item_converter(item_group)

        gender_response_list = []
        item_list = helpers.list_seperator(personal_names_list)

        for item in item_list:
            payload = {}
            payload['personalNames'] = item
            a = self.__api_post(url=url, data=payload).json()['personalNames']
            for i in range(len(a)):
                gender_response_list.append(GenderResponse(a[i]))

        return gender_response_list

    # def batch(self, item_group: Batch) -> list:
    #     personal_names_list = helpers.gender_batch_item_converter(item_group)

    #     response_list = []
    #     item_list = helpers.list_seperator(personal_names_list)

    #     for item in item_list:
    #         payload = {}
    #         payload['personalNames'] = item
    #         a = self.__api_post(url=url, data=payload).json()['personalNames']
    #         for i in range(len(a)):
    #             response_list.append(GenderResponse(a[i]))

    #     return response_list

    def genderFullGeo(self, full_name: str, country_code: CountryCodes) -> GenderResponse:
        """Infer the likely gender of a full name, given a local context (ISO2 country code).

        Args:
            full_name (str): The name to be classified.
            country_code (CountryCodes): The country code to aid with classification.

        Returns:
            GenderResponse: An Object which is a wrapper of the API's response object for this particular endpoint.
        """

        url = f"genderFullGeo/{full_name}/{country_code.value}"
        return GenderResponse(self.__api_get(url=url).json())

        def genderFull(self, full_name: str) -> GenderResponse:
            """Infer the likely gender of a full name, ex. John H. Smith

            Args:
                full_name (str): The name to be classified.

            Returns:
                GenderResponse: An Object which is a wrapper of the API's response object for this particular endpoint.
            """

        url = f"genderFull/{full_name}"
        return GenderResponse(self.__api_get(url=url).json())
