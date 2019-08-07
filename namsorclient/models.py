import requests
 
 
class GenderResponse: 
    """
        A class that represents a response that contains gender information

        Attributes:
            ID (str): the ID of the data set
            first_name (str): the desired first name
            last_name (str): the desired last name
            likely_gender (str): the likely gender inferred from input (male or female)
            gender_scale (int): the gender scale inferred from input (-1 or 1)
            score (float): the score of the precision of the gender information provided ranging from 0 to 50
            probability_calibrated (float): the probability that the gender information provided is correct
    """
    def __init__(self, api_response: dict):
        """ Constructor
        
        Args:
            api_response (dict): the json format (dict) of the NamsorAPI response received from a GET/POST request
        """
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

#     def _init_(self, )
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
