*namsor-client* is a python package that serves as a wrapper for the Namsor classification API.


## Responses
- **GenderResponse**
  - ```ID```
  - ```first_name```
  - ```last_name```
  - ```likely_gender```
  - ```gender_scale```
  - ```score```
  - ```probability_calibrated```
- **OriginResponse**
  - ```ID```
  - ```first_name```
  - ```last_name```
  - ```likely_gender```
  - ```score```
  - ```country_origin```
  - ```country_origin_alt```
  - ```region_origin```
  - ```top_region_origin```
  - ```sub_region_origin```
- **CountryResponse**
  - ```ID```
  - ```name```
  - ```score```
  - ```country```
  - ```country_alt```
  - ```region```
  - ```top_region```
  - ```sub_region```
- **RaceEthnicityResponse**
  - ```ID```
  - ```first_name```
  - ```last_name```
  - ```race_ethnicity```
  - ```race_ethnicity_alt```
  - ```score```
- **DiasporaResponse**
  - ```ID```
  - ```first_name```
  - ```last_name```
  - ```score```
  - ```ethnicity```
  - ```ethnicity_alt```
  - ```lifted```
  - ```country```
- **ParseNameResponse**
  - ```ID```
  - ```name```
  - ```name_parser_type```
  - ```name_parser_type_alt```
  - ```first_last_name```
  - ```score```

## Batches
- ```GenderBatch``` *returns GenderResponse*
- ```GenderGeoBatch``` *returns GenderResponse*
- ```ParsedGenderBatch``` *returns GenderResponse*
- ```ParsedGenderGeoBatch``` *returns GenderResponse*
- ```GenderFullBatch``` *returns GenderResponse*
- ```GenderFullGeoBatch``` *returns GenderResponse*
- ```OriginBatch``` *returns OriginResponse*
- ```CountryBatch``` *returns CountryBatch*
- ```US_RaceEthnicityBatch``` *returns RaceEthnicityBatch*
- ```US_ZipRaceEthnicityBatch``` *returns RaceEthnicityBatch*
- ```DiasporaBatch``` *returns DiasporaResponse*
- ```ParseNameBatch``` *returns ParsedNameResponse*
- ```ParseNameGeoBatch``` *returns ParsedNameResponse*

## Installation

```pip install namsor-client```

## Usage

```python
from namsorclient import *


# Create an instance of NamsorClient and pass in your API key as an argument
client = NamsorClient("Insert API key")

# Access the gender (GET) endpoint with function that returns a response of type GenderResponse
response = client.gender("Lelouch","Lamperouge")

# Access the different parts of the response for this particular endpoint

print(response.ID)
print(response.first_name)
print(response.last_name)
print(response.likely_gender)
print(response.gender_scale)
print(response.score)
print(response.probability_calibrated)

# Refer to Responses section to view all different variables of each different Response


# Access the genderGeo (GET) endpoint with function that returns a response of type GenderResponse
response = client.genderGeo("Lelouch","Lamperouge", CountryCodes.Japan)

# Access the genderFullGeo (GET) endpoint with function that returns a response of type GenderResponse
response = client.genderFullGeo("Lelouch Lamperouge", CountryCodes.Japan)

# Access the genderFull (GET) endpoint with function that returns a response of type GenderResponse
response = client.genderFull("Lelouch Lamperouge")

# Access the usRaceEthnicity (GET) endpoint with function that returns a response of type RaceEthnicityResponse
response = client.usRaceEthnicity("Lelouch","Lamperouge")

# Access the usRaceEthnicityZIP5 (GET) endpoint with function that returns a response of type RaceEthnicityResponse
response = client.usRaceEthnicityZIP5("Lelouch","Lamperouge", "42096")

# Access the diaspora (GET) endpoint with function that returns a response of type DiasporaResponse
response = client.diaspora(CountryCodes.Japan, "Lelouch",  "Lamperouge")

# Access the parseName (GET) endpoint with function that returns a response of type ParseNameResponse
response = client.parseName("Lelouch Lamperouge")

# Access the parseNameGeo (GET) endpoint with function that returns a response of type ParseNameResponse
response = client.parseNameGeo("Lelouch Lamperouge", CountryCodes.Japan)

# Access the origin (GET) endpoint with function that returns a response of type OriginResponse
response = client.origin("Lelouch","Lamperouge")

# Access the country (GET) endpoint with function that returns a response of type CountryResponse
response = client.country("Lelouch Lamperouge")



# Access the genderBatch (POST) endpoint
gender_batch = GenderBatch()

# Add items, with required arguments, to the batch you want
gender_batch.addItem("Lelouch","Lamperouge","A2140")
gender_batch.addItem("Gon","Freecs", "M0245")
gender_batch.addItem("Jonathan","Joestar", "M0014")

response_list = client.batch(gender_batch)

print(response_list[2].likely_gender)


```

