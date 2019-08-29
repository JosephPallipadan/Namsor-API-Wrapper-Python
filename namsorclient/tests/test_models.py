import namsorclient
import random


def test_NameParserType():
    tests = [(1, 1), (10, 11), (0, 500), (1190, 0)]
    for i in tests:
        raw_string = f'LN{i[0]}FN{i[1]}'
        tester = namsorclient.NameParserTypeWrapper(raw_string)
        assert str(tester) == raw_string
        assert tester.first_name_count == i[0]
        assert tester.last_name_count == i[1]


def test_FirstLastName():
    test = {
        "id": "4w3vb328f9[h",
        "firstName": "Lelouch",
        "lastName": "Lamperouge"
    }

    tester = namsorclient.FirstLastNameWrapper(test)
    assert tester.ID == test["id"]
    assert tester.first_name == test["firstName"]
    assert tester.last_name == test["lastName"]
    assert str(
        tester) == f'First Name: {test["firstName"]} | Last Name: {test["lastName"]}'


def test_ParseNameResponse():
    test = {
        "id": "null",
        "name": "Lelouch Lamperouge",
        "nameParserType": "LN1FN1",
        "nameParserTypeAlt": "null",
        "firstLastName": {
            "id": "null",
            "firstName": "Lamperouge",
            "lastName": "Lelouch"
        },
        "score": 13.941371643351383
    }
    tester = namsorclient.ParseNameResponse(test)
    assert tester.ID == test["id"]
    assert tester.name == test["name"]
    assert tester.name_parser_type == namsorclient.NameParserTypeWrapper(
        test["nameParserType"])
    assert tester.first_last_name == namsorclient.FirstLastNameWrapper(
        test["firstLastName"])
    assert tester.score == test["score"]


def test_DiasporaResponse():
    test = {
        "id": "null",
        "firstName": "Lelouch",
        "lastName": "Lamperouge",
        "score": 4.723012344810805,
        "ethnicityAlt": "Jewish",
        "ethnicity": "French",
        "lifted": False,
        "countryIso2": "US"
    }
    tester = namsorclient.DiasporaResponse(test)
    assert tester.ID == test["id"]
    assert tester.first_name == test["firstName"]
    assert tester.last_name == test["lastName"]
    assert tester.score == test["score"]
    assert tester.ethnicity == test["ethnicity"]
    assert tester.ethnicity_alt == test["ethnicityAlt"]
    assert tester.lifted == test["lifted"]
    assert tester.country == test["countryIso2"]


def test_RaceEthnicityResponse():
    test = {
        "id": "null",
        "firstName": "Lelouch",
        "lastName": "Lamperouge",
        "raceEthnicityAlt": "B_NL",
        "raceEthnicity": "A",
        "score": 1.1935005311130282
    }

    tester = namsorclient.RaceEthnicityResponse(test)
    assert tester.ID == test["id"]
    assert tester.first_name == test["firstName"]
    assert tester.last_name == test["lastName"]
    assert tester.race_ethnicity_alt == test["raceEthnicityAlt"]
    assert tester.race_ethnicity == test["raceEthnicity"]
    assert tester.score == test["score"]


def test_CountryResponse():
    test = {
        "id": "null",
        "name": "Lelouch Lamperouge",
        "score": 4.588447222213136,
        "country": "FR",
        "countryAlt": "CD",
        "region": "Europe",
        "topRegion": "Europe",
        "subRegion": "Western Europe"
    }

    tester = namsorclient.CountryResponse(test)
    assert tester.ID == test["id"]
    assert tester.name == test["name"]
    assert tester.score == test["score"]
    assert tester.country == test["country"]
    assert tester.country_alt == test["countryAlt"]
    assert tester.region == test["region"]
    assert tester.top_region == test["topRegion"]
    assert tester.sub_region == test["subRegion"]


def test_OriginResponse():
    test = {
        "id": "null",
        "firstName": "Lelouch",
        "lastName": "Lamperouge",
        "countryOrigin": "FR",
        "countryOriginAlt": "GB",
        "score": 1.3850776127906477,
        "regionOrigin": "Europe",
        "topRegionOrigin": "Europe",
        "subRegionOrigin": "Western Europe"
    }

    tester = namsorclient.OriginResponse(test)
    assert tester.ID == test["id"]
    assert tester.first_name == test["firstName"]
    assert tester.last_name == test["lastName"]
    assert tester.country_origin == test["countryOrigin"]
    assert tester.country_origin_alt == test["countryOriginAlt"]
    assert tester.score == test["score"]
    assert tester.region_origin == test["regionOrigin"]
    assert tester.top_region_origin == test["topRegionOrigin"]
    assert tester.sub_region_origin == test["subRegionOrigin"]


def test_GenderFullResponse():
    test = {
        "id": "null",
        "name": "Lelouch Lamperouge",
        "likelyGender": "male",
        "genderScale": -1,
        "score": 99,
    }

    tester = namsorclient.GenderFullResponse(test)
    assert tester.ID == test["id"]
    assert tester.name == test["name"]
    assert tester.likely_gender == test["likelyGender"]
    assert tester.gender_scale == test["genderScale"]
    assert tester.score == test["score"]


def test_GenderResponse():
    test = {
        "id": "null",
        "firstName": "Lelouch",
        "lastName": "Lamperouge",
        "likelyGender": "male",
        "genderScale": -1,
        "score": 9.000730451243589,
        "probabilityCalibrated": 0.6253864122577326
    }

    tester = namsorclient.GenderResponse(test)
    assert tester.ID == test["id"]
    assert tester.first_name == test["firstName"]
    assert tester.last_name == test["lastName"]
    assert tester.likely_gender == test["likelyGender"]
    assert tester.gender_scale == test["genderScale"]
    assert tester.score == test["score"]
    assert tester.probability_calibrated == test["probabilityCalibrated"]
