import requests

from models import GenderResponse

BASE_URL = "https://v2.namsor.com/NamSorAPIv2/api2/json/" 

class NamsorClient:
    """
    A class representing a NamsorAPI client

    Attributes:
        api_key(str): the NamsorAPI key the client receives after signing in
    """
    def __init__(self, api_key):
        self.api_key = api_key
        test_response = self.api_get()
        if test_response.status_code == 401:
            raise Exception('Invalid API Key')
            # The client has not entered his/her API key or the API key is incorrect
        elif test_response.status_code == 403:
            raise Exception("API Limit Reached or API Key Disabled")
            # The client's amount of requests has reached the maximum amount he/she can send in a month or his/her subscription plan has been cancelled

    def api_get(self, url="gender/Lelouch/Lamperouge") -> requests.models.Response:
        """ returns a response containing desired information of the data
        
        Args:
            url (str, optional): ending portion of NamsorAPI url to desired section. Defaults to "gender/Lelouch/Lamperouge".
        
        Returns:
            requests.models.Response: the response received from this GET request
        """
        return requests.get(url=f"{BASE_URL}{url}", headers={"X-API-KEY": self.api_key})

    def api_post(self, url, data) -> requests.models.Response:
        """ returns a response containing desired information of the data
        
        Args:
            url (str): ending portion of NamsorAPI url to desired section 
            data (dict): the high throughput data to process
        
        Returns:
            requests.models.Response: the response received from this POST request
        """
        return requests.post(url=f"{BASE_URL}{url}", headers={"X-API-KEY": self.api_key}, json=data)

    def gender(self, first_name: str, last_name: str) -> GenderResponse:
        """ Returns a GenderResponse object containing gender data 
        
        Args:
            first_name (str): the desired first name 
            last_name (str): the desired last name
        
        Returns:
            GenderResponse: a GenderResponse object that contains gender data
        """
        return GenderResponse(self.api_get(url=f"gender/{first_name}/{last_name}"))


# class originResponse:
#     ID = ""
#     firstName = ""
#     lastName = ""
#     countryOrigin = ""
#     countryOriginAlt = ""
#     score = ""
#     regionOrigin = ""
#     topRegionOrigin = ""
#     subRegionOrigin = ""

# class RaceEthnicityResponse:
#     ID = ""
#     firstName = ""
#     lastName = ""
#     raceEthnicityAlt =  "W_NL"
#     raceEthnicity = "W_NL"
#     score = 0

# class DiasporaResponse:
