import requests


class NamsorClient:
    api_key = ""

    def __init__(self, api_key):
        self.api_key = api_key
        test_response = self.api_get()
        if test_response.status_code == 401:
            print("Do This")
        elif test_response.status_code == 403:
            print("Do That")

    def api_get(self, url="/api2/json/gender/Lelouch/Lamperouge"):
        return requests.get(url='https://v2.namsor.com/NamSorAPIv2/api2/json/genderBatch',
                            headers={"X-API-KEY": self.api_key})


class GenderResponse:
    ID = ""
    firstName = ""
    lastName = ""
    likelyGender = ""
    genderScale = ""
    score = 0.0
    probabilityCalibrated = 0.0
    
    def __init__(self, api_response: requests.models.Response) -> GenderResponse:
        ID = api_response.json['id']
        firstName = api_response.json['firstName']
        lastName = api_response.json['lastName']
        likelyGender = api_response.json['likelyGender']
        genderScale = int(api_response.json['genderScale'])
        score = float(api_response.json['score'])
        probabilityCalibrated = float(api_response.json['probabilityCalibrated'])

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