from faker import Faker
from random import Random
import xlrd
import namsorclient
from namsorclient.sample_batch_responses import Sample_Responses

random_obj = Random()
faker_obj = Faker()


def test_list_seperator():
    total_num = random_obj.randint(100, 1000)
    tester = [random_obj.randint(1, 1000) for i in range(total_num)]
    tester_copy = tester.copy()

    tester = namsorclient.list_separator(tester)

    block, pointer_1, pointer_2 = 0, 0, 0
    while pointer_2 < len(tester_copy):
        assert tester_copy[pointer_2] == tester[block][pointer_1]

        pointer_2 += 1
        if pointer_1 == 99:
            pointer_1 = 0
            block += 1
        else:
            pointer_1 += 1


def test_export_to_excel():
    for i in list(Sample_Responses()):
        print(i)


def test_GenderBatch():
    tester = namsorclient.GenderBatch()
    assert tester.response_type == namsorclient.GenderResponse
    names = []
    for id in range(10):
        name = str(faker_obj.name()).split(" ")[:2]
        name.append(id)
        names.append(name)

        tester.addItem(name[0], name[1], id)

        assert isinstance(
            tester.items[-1], namsorclient.GenderBatch.GenderBatchItem)
        assert tester.items[-1].first_name == name[0]
        assert tester.items[-1].last_name == name[1]
        assert tester.items[-1].ID == name[2]

    for name, item in zip(names, tester.batch_item_converter()):
        keys = ["id", "firstName", "lastName"]
        assert all([key in item for key in keys])
        assert item["firstName"] == name[0]
        assert item["lastName"] == name[1]
        assert item["id"] == name[2]


def test_GenderGeoBatch():
    tester = namsorclient.GenderGeoBatch()
    assert tester.response_type == namsorclient.GenderResponse
    names = []
    for id in range(10):
        name = str(faker_obj.name()).split(" ")[:2]
        country_code = random_obj.choice(list(namsorclient.CountryCodes))

        name.append(country_code)
        name.append(id)

        names.append(name)

        tester.addItem(name[0], name[1], name[2], name[3])

        assert isinstance(
            tester.items[-1], namsorclient.GenderGeoBatch.GenderGeoBatchItem)
        assert tester.items[-1].first_name == name[0]
        assert tester.items[-1].last_name == name[1]
        assert tester.items[-1].country_code == name[2].value
        assert tester.items[-1].ID == id

    for name, item in zip(names, tester.batch_item_converter()):
        keys = ["id", "firstName", "lastName", "countryIso2"]
        assert all([key in item for key in keys])
        assert item["firstName"] == name[0]
        assert item["lastName"] == name[1]
        assert item["countryIso2"] == name[2].value
        assert item["id"] == name[3]


def test_ParsedGenderBatch():
    tester = namsorclient.ParsedGenderBatch()
    assert tester.response_type == namsorclient.GenderResponse
    names = []
    for id in range(10):
        name = str(faker_obj.name()).split(" ")

        while len(name) < 3:
            name = str(faker_obj.name()).split(" ")
        name = [name[0], name[2], "Dr.", "The First", name[1], id]
        names.append(name)

        tester.addItem(name[0], name[1], name[2], name[3], name[4], name[5])

        assert isinstance(
            tester.items[-1], namsorclient.ParsedGenderBatch.ParsedGenderBatchItem)
        assert tester.items[-1].first_name == name[0]
        assert tester.items[-1].last_name == name[1]
        assert tester.items[-1].prefix_or_title == name[2]
        assert tester.items[-1].suffix == name[3]
        assert tester.items[-1].middle_name == name[4]
        assert tester.items[-1].ID == name[5]

    for name, item in zip(names, tester.batch_item_converter()):
        keys = ["id", "firstName", "lastName",
                "prefixOrTitle", "suffix", "middleName"]
        assert all([key in item for key in keys])
        assert item["firstName"] == name[0]
        assert item["lastName"] == name[1]
        assert item["prefixOrTitle"] == name[2]
        assert item["suffix"] == name[3]
        assert item["middleName"] == name[4]
        assert item["id"] == name[5]


def test_ParsedGenderGeoBatch():
    tester = namsorclient.ParsedGenderGeoBatch()
    assert tester.response_type == namsorclient.GenderResponse
    names = []
    for id in range(10):
        name = str(faker_obj.name()).split(" ")
        country_code = random_obj.choice(list(namsorclient.CountryCodes))

        while len(name) < 3:
            name = str(faker_obj.name()).split(" ")
        name = [name[0], name[2], "Dr.", "The First", name[1], country_code, id]
        names.append(name)

        tester.addItem(name[0], name[1], name[2], name[3], name[4], name[5], name[6])

        assert isinstance(
            tester.items[-1], namsorclient.ParsedGenderGeoBatch.ParsedGenderGeoBatchItem)
        assert tester.items[-1].first_name == name[0]
        assert tester.items[-1].last_name == name[1]
        assert tester.items[-1].prefix_or_title == name[2]
        assert tester.items[-1].suffix == name[3]
        assert tester.items[-1].middle_name == name[4]
        assert tester.items[-1].country_code == name[5].value
        assert tester.items[-1].ID == name[6]

    for name, item in zip(names, tester.batch_item_converter()):
        keys = ["id", "firstName", "lastName",
                "prefixOrTitle", "suffix", "middleName", "countryIso2"]
        assert all([key in item for key in keys])
        assert item["firstName"] == name[0]
        assert item["lastName"] == name[1]
        assert item["prefixOrTitle"] == name[2]
        assert item["suffix"] == name[3]
        assert item["middleName"] == name[4]
        assert item["countryIso2"] == name[5].value
        assert item["id"] == name[6]


def test_GenderFullBatch():
    tester = namsorclient.GenderFullBatch()
    assert tester.response_type == namsorclient.GenderFullResponse
    names = []
    for id in range(10):
        name = [faker_obj.name()]
        name.append(id)

        names.append(name)

        tester.addItem(name[0], name[1])

        assert isinstance(
            tester.items[-1], namsorclient.GenderFullBatch.GenderFullBatchItem)
        assert tester.items[-1].name == name[0]
        assert tester.items[-1].ID == name[1]

    for name, item in zip(names, tester.batch_item_converter()):
        keys = ["id", "name"]
        assert all([key in item for key in keys])
        assert item["name"] == name[0]
        assert item["id"] == name[1]


def test_GenderFullGeoBatch():
    tester = namsorclient.GenderFullGeoBatch()
    assert tester.response_type == namsorclient.GenderFullResponse
    names = []
    for id in range(10):
        name = [faker_obj.name()]
        country_code = random_obj.choice(list(namsorclient.CountryCodes))

        name.append(country_code)
        name.append(id)

        names.append(name)
        tester.addItem(name[0], name[1], name[2])

        assert isinstance(
            tester.items[-1], namsorclient.GenderFullGeoBatch.GenderFullGeoBatchItem)
        assert tester.items[-1].name == name[0]
        assert tester.items[-1].country_code == name[1].value
        assert tester.items[-1].ID == name[2]

    for name, item in zip(names, tester.batch_item_converter()):
        keys = ["id", "name", "countryIso2"]
        assert all([key in item for key in keys])
        assert item["name"] == name[0]
        assert item["countryIso2"] == name[1].value
        assert item["id"] == name[2]


def test_OriginBatch():
    tester = namsorclient.OriginBatch()
    assert tester.response_type == namsorclient.OriginResponse
    names = []
    for id in range(10):
        name = str(faker_obj.name()).split(" ")[:2]
        name.append(id)
        names.append(name)

        tester.addItem(name[0], name[1], id)

        assert isinstance(
            tester.items[-1], namsorclient.OriginBatch.OriginBatchItem)
        assert tester.items[-1].first_name == name[0]
        assert tester.items[-1].last_name == name[1]
        assert tester.items[-1].ID == name[2]

    for name, item in zip(names, tester.batch_item_converter()):
        keys = ["id", "firstName", "lastName"]
        assert all([key in item for key in keys])
        assert item["firstName"] == name[0]
        assert item["lastName"] == name[1]
        assert item["id"] == name[2]


def test_CountryBatch():
    tester = namsorclient.CountryBatch()
    assert tester.response_type == namsorclient.CountryResponse
    names = []
    for id in range(10):
        name = [faker_obj.name()]
        name.append(id)

        names.append(name)

        tester.addItem(name[0], name[1])

        assert isinstance(
            tester.items[-1], namsorclient.CountryBatch.CountryBatchItem)
        assert tester.items[-1].name == name[0]
        assert tester.items[-1].ID == name[1]

    for name, item in zip(names, tester.batch_item_converter()):
        keys = ["id", "name"]
        assert all([key in item for key in keys])
        assert item["name"] == name[0]
        assert item["id"] == name[1]


def test_USRaceEthnicityBatch():
    tester = namsorclient.US_RaceEthnicityBatch()
    assert tester.response_type == namsorclient.RaceEthnicityResponse
    names = []
    for id in range(10):
        name = str(faker_obj.name()).split(" ")[:2]
        country_code = random_obj.choice(list(namsorclient.CountryCodes))

        name.append(country_code)
        name.append(id)

        names.append(name)

        tester.addItem(name[0], name[1], name[2], name[3])

        assert isinstance(
            tester.items[-1], namsorclient.US_RaceEthnicityBatch.US_RaceEthnicityBatchItem)
        assert tester.items[-1].first_name == name[0]
        assert tester.items[-1].last_name == name[1]
        assert tester.items[-1].country_code == name[2].value
        assert tester.items[-1].ID == id

    for name, item in zip(names, tester.batch_item_converter()):
        keys = ["id", "firstName", "lastName", "countryIso2"]
        assert all([key in item for key in keys])
        assert item["firstName"] == name[0]
        assert item["lastName"] == name[1]
        assert item["countryIso2"] == name[2].value
        assert item["id"] == name[3]


def test_ZipRaceEthnicityBatch():
    tester = namsorclient.US_ZipRaceEthnicityBatch()
    assert tester.response_type == namsorclient.RaceEthnicityResponse
    names = []
    for id in range(10):
        name = str(faker_obj.name()).split(" ")[:2]
        country_code = random_obj.choice(list(namsorclient.CountryCodes))

        name.append(country_code)
        name.append(str(random_obj.randint(10000, 99999)))
        name.append(id)

        names.append(name)
        tester.addItem(name[0], name[1], name[2], name[3], name[4])

        assert isinstance(
            tester.items[-1], namsorclient.US_ZipRaceEthnicityBatch.US_ZipRaceEthnicityBatchItem)
        assert tester.items[-1].first_name == name[0]
        assert tester.items[-1].last_name == name[1]
        assert tester.items[-1].country_code == name[2].value
        assert tester.items[-1].zip_code == name[3]
        assert tester.items[-1].ID == name[4]

    for name, item in zip(names, tester.batch_item_converter()):
        keys = ["id", "firstName", "lastName", "countryIso2", "zipCode"]
        assert all([key in item for key in keys])
        assert item["firstName"] == name[0]
        assert item["lastName"] == name[1]
        assert item["countryIso2"] == name[2].value
        assert item["zipCode"] == name[3]
        assert item["id"] == name[4]


def test_DiasporaBatch():
    tester = namsorclient.DiasporaBatch()
    assert tester.response_type == namsorclient.DiasporaResponse
    names = []
    for id in range(10):
        name = str(faker_obj.name()).split(" ")[:2]
        country_code = random_obj.choice(list(namsorclient.CountryCodes))

        name.append(country_code)
        name.append(id)

        names.append(name)

        tester.addItem(name[0], name[1], name[2], name[3])

        assert isinstance(
            tester.items[-1], namsorclient.DiasporaBatch.DiasporaBatchItem)
        assert tester.items[-1].first_name == name[0]
        assert tester.items[-1].last_name == name[1]
        assert tester.items[-1].country_code == name[2].value
        assert tester.items[-1].ID == id

    for name, item in zip(names, tester.batch_item_converter()):
        keys = ["id", "firstName", "lastName", "countryIso2"]
        assert all([key in item for key in keys])
        assert item["firstName"] == name[0]
        assert item["lastName"] == name[1]
        assert item["countryIso2"] == name[2].value
        assert item["id"] == name[3]


def test_ParseNameBatch():
    tester = namsorclient.ParseNameBatch()
    assert tester.response_type == namsorclient.ParseNameResponse
    names = []
    for id in range(10):
        name = [faker_obj.name()]
        name.append(id)

        names.append(name)

        tester.addItem(name[0], name[1])

        assert isinstance(
            tester.items[-1], namsorclient.ParseNameBatch.ParseNameBatchItem)
        assert tester.items[-1].name == name[0]
        assert tester.items[-1].ID == name[1]

    for name, item in zip(names, tester.batch_item_converter()):
        keys = ["id", "name"]
        assert all([key in item for key in keys])
        assert item["name"] == name[0]
        assert item["id"] == name[1]


def test_ParsedNameGeoBatch():
    tester = namsorclient.ParseNameGeoBatch()
    assert tester.response_type == namsorclient.ParseNameResponse
    names = []
    for id in range(10):
        name = [faker_obj.name()]
        country_code = random_obj.choice(list(namsorclient.CountryCodes))

        name.append(country_code)
        name.append(id)

        names.append(name)
        tester.addItem(name[0], name[1], name[2])

        assert isinstance(
            tester.items[-1], namsorclient.ParseNameGeoBatch.ParseNameGeoBatchItem)
        assert tester.items[-1].name == name[0]
        assert tester.items[-1].country_code == name[1].value
        assert tester.items[-1].ID == name[2]

    for name, item in zip(names, tester.batch_item_converter()):
        keys = ["id", "name", "countryIso2"]
        assert all([key in item for key in keys])
        assert item["name"] == name[0]
        assert item["countryIso2"] == name[1].value
        assert item["id"] == name[2]
