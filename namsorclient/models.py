import requests
 
 
class GenderResponse: 
  
   """A class representing the response to the request of the gender section"""
 
   def __init__(self, api_response: requests.models.Response):
       response_json = api_response.json()
       self.ID = response_json['id']
       self.first_name = response_json['firstName']
       self.last_name = response_json['lastName']
       self.likely_gender = response_json['likelyGender']
       self.gender_scale = int(response_json['genderScale'])
       self.score = float(response_json['score'])
       self.probability_calibrated = float(
           response_json['probabilityCalibrated'])
       # initializing the GenderResponse attributes with values of corresponding attribute names or keys of the API response in json format
