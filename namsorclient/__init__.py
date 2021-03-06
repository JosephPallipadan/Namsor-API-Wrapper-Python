import json
import requests
import time

from namsorclient.models import GenderResponse
from namsorclient.models import GenderFullResponse
from namsorclient.models import OriginResponse
from namsorclient.models import CountryResponse
from namsorclient.models import RaceEthnicityResponse
from namsorclient.models import DiasporaResponse
from namsorclient.models import ParseNameResponse
from namsorclient.models import NameParserTypeWrapper
from namsorclient.models import FirstLastNameWrapper

from namsorclient.request_objects import GenderBatch
from namsorclient.request_objects import GenderGeoBatch
from namsorclient.request_objects import GenderFullBatch
from namsorclient.request_objects import GenderFullGeoBatch
from namsorclient.request_objects import ParsedGenderBatch
from namsorclient.request_objects import ParsedGenderGeoBatch
from namsorclient.request_objects import OriginBatch
from namsorclient.request_objects import CountryBatch
from namsorclient.request_objects import US_RaceEthnicityBatch
from namsorclient.request_objects import US_ZipRaceEthnicityBatch
from namsorclient.request_objects import DiasporaBatch
from namsorclient.request_objects import ParseNameBatch
from namsorclient.request_objects import ParseNameGeoBatch
from namsorclient.request_objects import list_separator

from namsorclient.country_codes import CountryCodes


BASE_URL = "https://v2.namsor.com/NamSorAPIv2/api2/json/"


class NamsorClient:
    """
    A class representing a NamsorAPI client.
    Attributes:
        api_key(str): The Namsor API key of the user.
    """

    def __init__(self, api_key):
        self.api_key = api_key
        test_response = self.__api_get()
        if test_response.status_code == 401:
            raise Exception('Invalid API Key')
            # The client has not entered his/her API key or the API key is incorrect.
        elif test_response.status_code == 403:
            raise Exception("API Limit Reached or API Key Disabled")
            # The client's amount of requests has reached the maximum amount he/she can send in a month or his/her subscription plan has been cancelled.

    def __api_get(self, url="gender/Lelouch/Lamperouge") -> requests.models.Response:
        """ Returns a response containing desired information of the data.
        Args:
            url (str, optional): Ending portion of NamsorAPI url to desired section. Defaults to "gender/Lelouch/Lamperouge".
        Returns:
            requests.models.Response: The response received from this GET request.
        """

        # While the choice to include the error checking in the get request wrapper does somewhat compromise the elegance of the code base, the alternative, which would mean performing a request prior, potentially wastes a classification from the user's account and thus it was decided to prioritize the user's experience, especially given the non efficiency-intensive nature of the likely utilization of the wrapper

        return requests.get(url=f"{BASE_URL}{url}", headers={"X-API-KEY": self.api_key})

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
            country_code (CountryCodes): The country code to aid with classification.

        Returns:
            GenderResponse: An Object which is a wrapper of the API's response object for this particular endpoint.
        """
        url = f"genderGeo/{first_name}/{last_name}/{country_code.value}"
        return GenderResponse(self.__api_get(url=url).json())

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

    def usRaceEthnicity(self, first_name: str, last_name: str) -> RaceEthnicityResponse:
        """Infer a US resident's likely race/ethnicity according to US Census taxonomy W_NL (white, non latino), HL (hispano latino),  A (asian, non latino), B_NL (black, non latino).

        Args:
            first_name (str): The desired first name.
            last_name (str): The desired last name.

        Returns:
            OriginResponse: An object which is a wrapper of the API's response object for this particular endpoint.
        """
        url = f"usRaceEthnicity/{first_name}/{last_name}"
        return RaceEthnicityResponse(self.__api_get(url=url).json())

    def usRaceEthnicityZIP5(self, first_name: str, last_name: str, zip5_code: str) -> RaceEthnicityResponse:
        """Infer a US resident's likely race/ethnicity according to US Census taxonomy, using ZIP5 code info. Output is W_NL (white, non latino), HL (hispano latino),  A (asian, non latino), B_NL (black, non latino).

        Args:
            first_name (str): The desired first name.
            last_name (str): The desired last name.
            zip5_code (str): The zip code to aid with classification.

        Returns:
            OriginResponse: An object which is a wrapper of the API's response object for this particular endpoint.
        """

        url = f"usRaceEthnicity/{first_name}/{last_name}/{zip5_code}"
        return RaceEthnicityResponse(self.__api_get(url=url).json())

    def diaspora(self, first_name: str, last_name: str, country_code: CountryCodes) -> DiasporaResponse:
        """Infer the likely ethnicity/diaspora of a personal name, given a country of residence ISO2 code

        Args:
            first_name (str): The desired first name.
            last_name (str): The desired last name.
            country_code (CountryCodes): The country code to aid with classification.

        Returns:
            OriginResponse: An object which is a wrapper of the API's response object for this particular endpoint.
        """

        url = f"diaspora/{country_code.value}/{first_name}/{last_name}"
        return DiasporaResponse(self.__api_get(url=url).json())

    def parseName(self, full_name: str) -> ParseNameResponse:
        """Infer the likely first/last name structure of a name, ex. John Smith or SMITH, John or SMITH; John.

        Args:
            full_name (str): The name to be parsed.

        Returns: 
        ParseNameResponse: An object which is a wrapper of the API's response object for this particular endpoint.
        """

        url = f"parseName/{full_name}"
        return ParseNameResponse(self.__api_get(url=url).json())

    def parseNameGeo(self, full_name: str, country_code: CountryCodes) -> ParseNameResponse:
        """Infer the likely first/last name structure of a name, ex. John Smith or SMITH, John or SMITH; John, given an ISO2 country of residence.

        Args:
            full_name (str): The full name to be parsed.
            country_code (CountryCodes): The country code to aid with classification.

        Returns:
            ParseNameResponse: An object which is a wrapper of the API's response object for this particular endpoint.
        """

        url = f"parseName/{full_name}/{country_code.value}"
        return ParseNameResponse(self.__api_get(url=url).json())

    def origin(self, first_name: str, last_name: str) -> OriginResponse:
        """Infer the likely country of origin of a personal name. Assumes names as they are in the country of origin. For US, CA, AU, NZ and other melting-pots : use 'diaspora' instead.

        Args:
            first_name (str): The desired first name.
            last_name (str): The desired last name.

        Returns:
            OriginResponse: An object which is a wrapper of the API's response object for this particular endpoint.
        """

        url = f"origin/{first_name}/{last_name}"
        return OriginResponse(self.__api_get(url=url).json())

    def country(self, full_name: str) -> CountryResponse:
        """Infer the likely country of residence of a personal full name, or one surname. Assumes names as they are in the country of residence OR the country of origin.

        Args:
            full_name (str): The name whose country of residence should be determined.

        Returns:
            OriginResponse: An object which is a wrapper of the API's response object for this particular endpoint.
        """

        url = f"country/{first_name}/{last_name}"
        return OriginResponse(self.__api_get(url=url).json())
