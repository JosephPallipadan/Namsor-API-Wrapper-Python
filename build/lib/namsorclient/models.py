import requests


class GenderResponse:
    ID = ""
    first_name = ""
    last_name = ""
    likely_gender = ""
    gender_scale = 0.0
    score = 0.0
    probability_calibrated = 0.0

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
