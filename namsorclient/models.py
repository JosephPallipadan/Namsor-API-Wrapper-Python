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

        self.ID = api_response['id']
        self.first_name = api_response['firstName']
        self.last_name = api_response['lastName']
        self.likely_gender = api_response['likelyGender']
        self.gender_scale = int(api_response['genderScale'])
        self.score = float(api_response['score'])
        self.probability_calibrated = float(api_response['probabilityCalibrated'])
        # Initializing the GenderResponse attributes with values of corresponding attribute names or keys of  the API response in json format


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
