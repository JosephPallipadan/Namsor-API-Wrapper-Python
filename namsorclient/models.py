import requests
 
 
class GenderResponse: 
    
 
   def __init__(self, api_response: requests.models.Response):
       response_json = api_response.json()
       self.ID = response_json['id']
       self.first_name = response_json['firstName']
       self.last_name = response_json['lastName']
       self.likely_gender = response_json['likelyGender']
       self.gender_scale = int(response_json['genderScale'])
       self.score = float(response_json['score'])
       self.probability_calibrated = float(response_json['probabilityCalibrated'])
       # Initializing the GenderResponse attributes with values of corresponding attribute names or keys of the API response in json format


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
