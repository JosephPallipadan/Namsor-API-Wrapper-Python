import requests
import re


class GenderResponse:
    """
        A class that acts as a wrapper for all responses which classify a name into a gender.

        Attributes:
            ID (str): The ID of the request
            first_name (str): The first name that was classified
            last_name (str): The last name that was classified
            likely_gender (str): The likely gender inferred from input (male or female)
            gender_scale (int): The gender scale inferred from input (-1 or 1)
            score (float): The score of the precision of the gender information provided ranging from 0 to 50
            probability_calibrated (float): The probability that the gender information provided is correct
    """

    ID = ""
    first_name = ""
    last_name = ""
    likely_gender = ""
    gender_scale = ""
    score = 0.0
    probability_calibrated = 0.0

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
        self.probability_calibrated = float(
            api_response['probabilityCalibrated'])
        # Initializing the GenderResponse attributes with values of corresponding attribute names or keys of the API responsein json format


class OriginResponse:
    """
        A class that acts as a wrapper for all responses which infer the origin of an individual with a particular name.

        Attributes:
            ID (str): The ID of the request
            first_name (str): The first name that was classified
            last_name (str): The last name that was classified
            likely_gender (str): The likely gender inferred from input (male or female)
            gender_scale (int): The gender scale inferred from input (-1 or 1)
            score (float): The score of the precision of the gender information provided ranging from 0 to 50
            country_origin (str): The most likely country that the individual with this name belongs to.
            country_origin_alt (str): A potential alternative country that the individual with this name belongs to.
            probability_calibrated (float): The probability that the classification is correct
            region_origin (str):
            top_region_origin (str):
            sub_region_origin (str): 
    """
    ID = ""
    first_name = ""
    last_name = ""
    likely_gender = ""
    score = 0.0
    # Maybe use the country codes class here?
    country_origin = ""
    country_origin_alt = ""
    region_origin = ""
    top_region_origin = ""
    sub_region_origin = ""

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


class RaceEthnicityResponse:
    """
        A class that acts as a wrapper for all responses which infer the ethnicity of an individual with a particular name.

        Attributes:
            ID (str): The ID of the request
            first_name (str): The first name that was classified
            last_name (str): The last name that was classified
            score (float): The score of the precision of the gender information provided ranging from 0 to 50
            race_ethnicity (str): The most likely ethnicity of an individual with said name.
            race_ethnicity_alt (str): A potential alternative ethnicity that the individual can have.
    """
    ID = ""
    first_name = ""
    last_name = ""
    race_ethnicity_alt = "W_NL"
    race_ethnicity = "W_NL"
    score = 0

    def __init__(self, api_response: dict):
        """ Constructor
        Args:
            api_response (dict): the json format (dict) of the NamsorAPI response received from a GET/POST request
        """
        self.ID = api_response['id']
        self.first_name = api_response['firstName']
        self.last_name = api_response['lastName']
        self.race_ethnicity = api_response['raceEthnicity']
        self.race_ethnicity_alt = api_response['raceEthnicityAlt']
        self.score = api_response['score']


class DiasporaResponse:
    """
        A class that acts as a wrapper for the diaspora response object.

        Attributes:
            ID (str): The ID of the request
            first_name (str): The first name that was classified
            last_name (str): The last name that was classified
            score (float): The score of the precision of the gender information provided ranging from 0 to 50
            race_ethnicity (str): The most likely ethnicity of an individual with said name.
            race_ethnicity_alt (str): A potential alternative ethnicity that the individual can have.
            lifted (str):
            country (str): The ISO2 code of the country to which an indiviudal with this name liekly belongs to.
    """

    ID = ""
    fist_name = ""
    last_name = ""
    score = 0.0
    ethnicity_alt = ""
    ethnicity = ""
    lifted = ""
    country = ""

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
        self.lifted = api_response['lifted']
        self.country = api_response['countryIso2']


class ParseNameResponse:
    """
        A class that acts as a wrapper for the response object of all the parseName routes.

        Attributes:
            ID (str): The ID of the request
            name (str): The full name to be parsed
            name_parser_type (NameParserTypeWrapper): An object which contains data about how many words from the full name were classified into first names and last names.

            name_parser_type_alt (NameParserTypeWrapper): An object which contains another potential form of data about how many words from the full name were classified into first names and last names.

            first_last_name (FirstLastNameWrapper): An object which contains the most likely first name/ last name format that the full name would be arranged in.

            score (float): The score of the precision of the gender information provided ranging from 0 to 50
    """
    ID = ""
    name = ""
    name_parser_type = ""
    name_parser_type_alt = ""
    first_last_name = ""
    score = ""

    def __init__(self, api_response: dict):
        """ Constructor
        Args:
            api_response (dict): the json format (dict) of the NamsorAPI response received from a GET/POST request
        """
        self.ID = api_response['id']
        self.name = api_response['name']
        self.name_parser_type = NameParserTypeWrapper(
            api_response['nameParserType'])
        self.name_parser_type_alt = NameParserTypeWrapper(
            api_response['nameParserTypeAlt'])
        self.first_last_name = FirstLastNameWrapper(
            api_response['firstLastName'])
        self.score = api_response['score']


class NameParserTypeWrapper:
    """A class which acts as a wrapper for the nameParserType key in the parseName response objects.

    Attributes:
        first_name_count (int): The number of words classified as first names.
        last_name_count (int): The number of words classified as last names.

    """
    _raw_string = ""
    first_name_count = 0
    last_name_count = 0

    def __init__(self, raw_string: str):
        """ Constructor
        Args:
            raw_string (str): The raw string in the response object representing the value of the 'nameParserType' key.
        """
        self.raw_string = raw_string
        regex = re.fullmatch(r"FN([0-9]+)LN([0-9]+)", raw_string)
        self.first_name_count = int(regex.groups()[0])
        self.last_name_count = int(regex.groups()[1])

    def __repr__(self):
        return self._raw_string


class FirstLastNameWrapper:
    """A class which acts as a wrapper for the value of the 'firstLastName' key in the parseName response objects.

    Attributes:
        first_name (str): The portion of the full name classified as the first name.
        last_name_count (int): The portion of the full name classified as the last name.

    """

    ID = ""
    first_name = ""
    last_name = ""

    def __init__(self, raw_dict: dict):
        """ Constructor
        Args:
            raw_dict (dict): The raw json object in the response object representing the value of the 'firstLastName' key. 
        """
        self.ID = raw_dict['id']
        self.first_name = raw_dict['firstName']
        self.last_name = raw_dict['lastName']

    def __repr__(self):
        return f'First Name: {self.first_name} | Last Name: {self.last_name}'
