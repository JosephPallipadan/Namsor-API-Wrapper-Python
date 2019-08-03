import requests

class NamsorClient:
    api_key = ""

    def __init__(self, api_key):
        self.api_key = api_key
        test_response = self.api_get()
        if test_response.status_code == 401:
            raise Exception('Invalid API Key')
        elif test_response.status_code == 403:
            raise Exception("API Key Limit Reached")

    def api_get(self, url="https://v2.namsor.com/NamSorAPIv2/api2/json/gender/Lelouch/Lamperouge"):
        return requests.get(url=url, headers={"X-API-KEY": self.api_key})


class GenderResponse:
    ID = ""
    first_name = ""
    last_name = ""
    likely_gender = ""
    gender_scale = ""
    score = 0.0
    probability_calibrated = 0.0
    
    def __init__(self, api_response: requests.models.Response):
        self.ID = api_response.json['id']
        self.first_name = api_response.json['firstName']
        self.last_name = api_response.json['lastName']
        self.likely_gender = api_response.json['likelyGender']
        self.gender_scale = int(api_response.json['genderScale'])
        self.score = float(api_response.json['score'])
        self.probability_calibrated = float(
            api_response.json['probabilityCalibrated'])

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
