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
        # Initializing the GenderResponse attributes with values of corresponding attribute names or keys of the API response in json format


class OriginResponse:



    def __init__(self, api_response: dict):
        """ Constructor
        
        Args:
            api_response (dict): the json format (dict) of the NamsorAPI response received from a GET/POST request
        """

        self.ID = api_response['id']
        self.first_name = api_response['firstName']
        self.last_name = api_response['lastName']
        self.country_origin = api_response['countryOrigin']
        self.country_origin_alt = api_response['countryOriginAlt']
        self.score = float(api_response['score'])
        self.region_origin = api_response['regionOrigin']
        self.top_region_origin = api_response['topRegionOrigin']
        self.sub_region_origin = api_response['subRegionOrigin'] 


class CountryResponse:

    def __init__(self, api_response: dict):
        """ Constructor
        
        Args:
            api_response (dict): the json format (dict) of the NamsorAPI response received from a GET/POST request
        """

        self.ID = api_response['id']
        self.name = api_response['name']
        self.score = float(api_response['score'])
        self.country = api_response['country']
        self.country_alt = api_response['countryAlt']
        self.region = api_response['region']
        self.top_region = api_response['topRegion']
        self.sub_region = api_response['subRegion']

class US_RaceEthnicityResponse:

    def __init__(self, api_response: dict):
        """ Constructor
        
        Args:
            api_response (dict): the json format (dict) of the NamsorAPI response received from a GET/POST request
        """

        self.ID = api_response['id']
        self.first_name = api_response['firstName']
        self.last_name = api_response['lastName']
        self.race_ethnicity_alt = api_response['raceEthnicityAlt']
        self.race_ethnicity = api_response['raceEthnicity']
        self.score = float(api_response['score'])

class DiasporaResponse:

    def __init__(self, api_response: dict):
        """ Constructor
        
        Args:
            api_response (dict): the json format (dict) of the NamsorAPI response received from a GET/POST request
        """

        self.ID = api_response['id']
        self.first_name = api_response['firstName']
        self.last_name = api_response['lastName']
        self.score = float(api_response['score'])
        self.ethnicity_alt = api_response['ethnicityAlt']
        self.ethnicity = api_response['ethnicity']
        self.lifted = bool(api_response['lifted'])
        self.country_code = api_response['countryIso2']

class ParseNameResponse:

    def __init__(self, api_response:dict):
        """ Constructor
        
        Args:
            api_response (dict): the json format (dict) of the NamsorAPI response received from a GET/POST request
        """
        
        self.ID = api_response['id']
        self.name = api_response['name']
        self.name_parser_type = api_response['nameParserType']
        self.name_parser_type_alt = api_response['nameParserTypeAlt']
        self.first_last_name_id = api_response['firstLastName']['id']
        self.first_last_name_first_name = api_response['firstLastName']['firstName']
        self.first_last_name_last_name = api_response['firstLastName']['lastName']
        self.score = float(api_response['score'])
# {
#       "id": "string",
#       "name": "string",
#       "nameParserType": "string",
#       "nameParserTypeAlt": "string",
#       "firstLastName": {
#         "id": "string",
#         "firstName": "string",
#         "lastName": "string"
#       },
#       "score": 0
#     }