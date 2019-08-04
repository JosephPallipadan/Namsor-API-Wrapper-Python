import requests

from models import GenderResponse

BASE_URL = "https://v2.namsor.com/NamSorAPIv2/api2/json/"


class NamsorClient:
    def __init__(self, api_key):
        self.api_key = api_key
        test_response = self.api_get()
        if test_response.status_code == 401:
            raise Exception('Invalid API Key')
        elif test_response.status_code == 403:
            raise Exception("API Key Limit Reached")

    def api_get(self, url="gender/Lelouch/Lamperouge") -> requests.models.Response:
        return requests.get(url=f"{BASE_URL}{url}", headers={"X-API-KEY": self.api_key})

    def api_post(self, url, data) -> requests.models.Response:
        return requests.post(url=f"{BASE_URL}{url}", headers={"X-API-KEY": self.api_key}, json=data)

    def gender(self, first_name: str, last_name: str) -> GenderResponse:
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
