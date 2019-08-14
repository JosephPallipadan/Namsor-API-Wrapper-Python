import requests
import re


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

    ID = ""
    first_name = ""
    last_name = ""
    likely_gender = ""
    gender_scale = ""
    score = 0.0

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

    ID = ""
    first_name = ""
    last_name = ""
    likely_gender = ""
    score = 0.0
    country_origin = ""
    country_origin_alt = ""
    region_origin = ""
    top_region_origin = ""
    sub_region_origin = ""

    def __init__(self, api_response: dict):
        self.ID = api_response['id']
        self.first_name = api_response['firstName']
        self.last_name = api_response['lastName']
        self.country_origin = api_response['countryOrigin']
        self.country_origin_alt = int(api_response['countryOriginAlt'])
        self.score = float(api_response['score'])
        self.region_origin = float(api_response['regionOrigin'])
        self.top_region_origin = api_response['top_region_origin']
        self.sub_region_origin = api_response['sub_region_origin']


class RaceEthnicityResponse:
    ID = ""
    first_name = ""
    last_name = ""
    race_ethnicity_alt = "W_NL"
    race_ethnicity = "W_NL"
    score = 0

    def __init__(self, api_response: dict):
        self.ID = api_response['id']
        self.first_name = api_response['firstName']
        self.last_name = api_response['lastName']
        self.race_ethnicity = api_response['raceEthnicity']
        self.race_ethnicity_alt = api_response['raceEthnicityAlt']
        self.score = api_response['score']


class DiasporaResponse:

    ID = ""
    fist_name = ""
    last_name = ""
    score = 0.0
    ethnicityAlt = ""
    ethnicity = ""
    lifted = ""
    countryIso2 = ""

    def __init__(self, api_response: dict):
        self.ID = api_response['id']
        self.first_name = api_response['firstName']
        self.last_name = api_response['lastName']
        self.score = float(api_response['score'])
        self.ethnicityAlt = api_response['ethnicityAlt']
        self.ethnicity = api_response['ethnicity']
        self.lifted = api_response['lifted']
        self.countryIso2 = api_response['countryIso2']


class ParseNameResponse:

    ID = ""
    name = ""

    name_parser_type = ""
    name_parser_type_alt = ""
    first_last_name = ""

    score = ""

    def __init__(self, api_response: dict):
        self.ID = api_response['id']
        self.name = api_response['name']
        self.name_parser_type = NameParserTypeWrapper(
            api_response['nameParserType'])
        self.name_parser_type_alt = NameParserTypeWrapper(
            api_response['nameParserTypeAlt'])
        self.first_last_name = api_response['firstLastName']
        self.score = api_response['score']


class NameParserTypeWrapper:

    _raw_string = ""
    first_name_count = 0
    last_name_count = 0

    def __init__(self, raw_string: str):
        self.raw_string = raw_string
        regex = re.fullmatch(r"FN([0-9]+)LN([0-9]+)", raw_string)
        self.first_name_count = regex.groups()[0]
        self.last_name_count = regex.groups()[1]

    def __repr__(self):
        return self._raw_string


class firstLastNameWrapper:

    ID = ""
    first_name = ""
    last_name = ""

    def __init__(self, raw_dict: dict):
        self.ID = raw_dict['id']
        self.first_name = raw_dict['firstName']
        self.last_name = raw_dict['lastName']

    def __repr__(self):
        return f'First Name: {self.first_name} | Last Name: {self.last_name}'
