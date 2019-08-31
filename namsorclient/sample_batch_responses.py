from collections import namedtuple

Sample_Responses_Class = namedtuple
(
    'Sample_Responses', 
    'GenderResponses GenderFullResponses OriginResponses CountryResponses \
    RaceEthnicityResponses DiasporaResponses ParsedNameResponse'
)

Sample_Responses = Sample_Responses_Class
(
    #        ------------------------------------------------------------------------------------
    #                                   GenderResponse Samples
    #        ------------------------------------------------------------------------------------
    [{
        'id': '790',
        'firstName': 'Cynthia',
        'lastName': 'Martin',
        'likelyGender': 'female',
        'genderScale': 1.0,
        'score': 38.93331818668968,
        'probabilityCalibrated': 0.992457769300861
    }, {
        'id': '483',
        'firstName': 'Kelly',
        'lastName': 'Herrera',
        'likelyGender': 'female',
        'genderScale': 1.0,
        'score': 13.206913643992483,
        'probabilityCalibrated': 0.7568709219543044
    }, {
        'id': '738',
        'firstName': 'Margaret',
        'lastName': 'Phillips',
        'likelyGender': 'female',
        'genderScale': 1.0,
        'score': 28.28155981127263,
        'probabilityCalibrated': 0.9833262796012671
    }, {
        'id': '804',
        'firstName': 'Kevin',
        'lastName': 'Armstrong',
        'likelyGender': 'male',
        'genderScale': -1.0,
        'score': 36.82855624853989,
        'probabilityCalibrated': 0.9911835223666028
    }, {
        'id': '696',
        'firstName': 'Alicia',
        'lastName': 'Elliott',
        'likelyGender': 'female',
        'genderScale': 1.0,
        'score': 40.84375144891046,
        'probabilityCalibrated': 0.993543334003477
    }, {
        'id': '573',
        'firstName': 'David',
        'lastName': 'Perez',
        'likelyGender': 'male',
        'genderScale': -1.0,
        'score': 42.35570879385797,
        'probabilityCalibrated': 0.9936257852306357
    }, {
        'id': '31',
        'firstName': 'Breanna',
        'lastName': 'Lang',
        'likelyGender': 'female',
        'genderScale': 1.0,
        'score': 27.28303588458596,
        'probabilityCalibrated': 0.9813295829845597
    }, {
        'id': '388',
        'firstName': 'Mary',
        'lastName': 'Stein',
        'likelyGender': 'female',
        'genderScale': 1.0,
        'score': 20.892064581104407,
        'probabilityCalibrated': 0.9418945605393836
    }, {
        'id': '307',
        'firstName': 'Tonya',
        'lastName': 'Bright',
        'likelyGender': 'female',
        'genderScale': 1.0,
        'score': 21.72395268910261,
        'probabilityCalibrated': 0.9545684450756573
    }, {
        'id': '59',
        'firstName': 'Shelly',
        'lastName': 'Novak',
        'likelyGender': 'female',
        'genderScale': 1.0,
        'score': 18.845089011447104,
        'probabilityCalibrated': 0.9107087174326258
    }],
    #        ------------------------------------------------------------------------------------
    #                                   GenderFullResponse Samples
    #        ------------------------------------------------------------------------------------
    [{
        'id': '113',
        'name': 'Brett Petersen',
        'likelyGender': 'male',
        'genderScale': -1.0,
        'score': 33.691152352881794
    }, {
        'id': '195',
        'name': 'April Jackson DVM',
        'likelyGender': 'female',
        'genderScale': 1.0,
        'score': 9.315183448265584
    }, {
        'id': '498',
        'name': 'Tyrone Sanders',
        'likelyGender': 'male',
        'genderScale': -1.0,
        'score': 35.73948515061509
    }, {
        'id': '506',
        'name': 'Michael Green',
        'likelyGender': 'male',
        'genderScale': -1.0,
        'score': 30.963259191770305
    }, {
        'id': '914',
        'name': 'Mark Smith',
        'likelyGender': 'male',
        'genderScale': -1.0,
        'score': 44.99008221179214
    }, {
        'id': '522',
        'name': 'Angela Flores',
        'likelyGender': 'female',
        'genderScale': 1.0,
        'score': 24.634573447725124
    }, {
        'id': '563',
        'name': 'Richard Gonzalez',
        'likelyGender': 'male',
        'genderScale': -1.0,
        'score': 52.82109285593519
    }, {
        'id': '634',
        'name': 'Brandon Rogers',
        'likelyGender': 'male',
        'genderScale': -1.0,
        'score': 39.072922098778506
    }, {
        'id': '625',
        'name': 'John Clark',
        'likelyGender': 'male',
        'genderScale': -1.0,
        'score': 55.9746072512175
    }, {
        'id': '609',
        'name': 'Zachary Jacobs',
        'likelyGender': 'male',
        'genderScale': -1.0,
        'score': 46.82023753356409
    }],
    #        ------------------------------------------------------------------------------------
    #                                   OriginResponse Samples
    #        ------------------------------------------------------------------------------------
    [{
        'id': '31',
        'firstName': 'Stephen',
        'lastName': 'Coleman',
        'countryOrigin': 'GB',
        'countryOriginAlt': 'IE',
        'score': 1.8947393406337736,
        'regionOrigin': 'Europe',
        'topRegionOrigin': 'Europe',
        'subRegionOrigin': 'Northern Europe'
    }, {
        'id': '146',
        'firstName': 'Michael',
        'lastName': 'Burke',
        'countryOrigin': 'IE',
        'countryOriginAlt': 'GB',
        'score': 10.494827631725524,
        'regionOrigin': 'Europe',
        'topRegionOrigin': 'Europe',
        'subRegionOrigin': 'Northern Europe'
    }, {
        'id': '412',
        'firstName': 'Adrian',
        'lastName': 'Church',
        'countryOrigin': 'GB',
        'countryOriginAlt': 'CH',
        'score': 12.40215333766311,
        'regionOrigin': 'Europe',
        'topRegionOrigin': 'Europe',
        'subRegionOrigin': 'Northern Europe'
    }, {
        'id': '454',
        'firstName': 'Austin',
        'lastName': 'Boyd',
        'countryOrigin': 'GB',
        'countryOriginAlt': 'IE',
        'score': 6.311295115561374,
        'regionOrigin': 'Europe',
        'topRegionOrigin': 'Europe',
        'subRegionOrigin': 'Northern Europe'
    }, {
        'id': '428',
        'firstName': 'Michelle',
        'lastName': 'Trevino',
        'countryOrigin': 'FR',
        'countryOriginAlt': 'IT',
        'score': 0.34130148343600725,
        'regionOrigin': 'Europe',
        'topRegionOrigin': 'Europe',
        'subRegionOrigin': 'Western Europe'
    }, {
        'id': '537',
        'firstName': 'Jordan',
        'lastName': 'Gonzalez',
        'countryOrigin': 'ES',
        'countryOriginAlt': 'FR',
        'score': 21.71707930344048,
        'regionOrigin': 'Europe',
        'topRegionOrigin': 'Europe',
        'subRegionOrigin': 'Southern Europe'
    }, {
        'id': '543',
        'firstName': 'Matthew',
        'lastName': 'Garcia',
        'countryOrigin': 'ES',
        'countryOriginAlt': 'GB',
        'score': 10.620154841037358,
        'regionOrigin': 'Europe',
        'topRegionOrigin': 'Europe',
        'subRegionOrigin': 'Southern Europe'
    }, {
        'id': '876',
        'firstName': 'Beth',
        'lastName': 'Evans',
        'countryOrigin': 'GB',
        'countryOriginAlt': 'IE',
        'score': 14.819170193754193,
        'regionOrigin': 'Europe',
        'topRegionOrigin': 'Europe',
        'subRegionOrigin': 'Northern Europe'
    }, {
        'id': '978',
        'firstName': 'Elizabeth',
        'lastName': 'Miller',
        'countryOrigin': 'GB',
        'countryOriginAlt': 'IE',
        'score': 6.241282311663333,
        'regionOrigin': 'Europe',
        'topRegionOrigin': 'Europe',
        'subRegionOrigin': 'Northern Europe'
    }, {
        'id': '680',
        'firstName': 'Alexis',
        'lastName': 'Moreno',
        'countryOrigin': 'ES',
        'countryOriginAlt': 'FR',
        'score': 5.7003339923628245,
        'regionOrigin': 'Europe',
        'topRegionOrigin': 'Europe',
        'subRegionOrigin': 'Southern Europe'
    }],
    #        ------------------------------------------------------------------------------------
    #                                   CountryResponse Samples
    #        ------------------------------------------------------------------------------------
    [{
        'id': '576',
        'name': 'Jamie Fleming',
        'score': 7.06264456142918,
        'country': 'GB',
        'countryAlt': 'IE',
        'region': 'Europe',
        'topRegion': 'Europe',
        'subRegion': 'Northern Europe'
    }, {
        'id': '212',
        'name': 'John Roberts',
        'score': 3.0803229164056143,
        'country': 'GB',
        'countryAlt': 'IE',
        'region': 'Europe',
        'topRegion': 'Europe',
        'subRegion': 'Northern Europe'
    }, {
        'id': '573',
        'name': 'Jack Rhodes',
        'score': 13.510695042355879,
        'country': 'GB',
        'countryAlt': 'IE',
        'region': 'Europe',
        'topRegion': 'Europe',
        'subRegion': 'Northern Europe'
    }, {
        'id': '198',
        'name': 'Amanda Mcclure',
        'score': 4.293304555301407,
        'country': 'GB',
        'countryAlt': 'IE',
        'region': 'Europe',
        'topRegion': 'Europe',
        'subRegion': 'Northern Europe'
    }, {
        'id': '407',
        'name': 'James Wood',
        'score': 10.623796000676329,
        'country': 'GB',
        'countryAlt': 'IE',
        'region': 'Europe',
        'topRegion': 'Europe',
        'subRegion': 'Northern Europe'
    }, {
        'id': '267',
        'name': 'Bryan Griffith',
        'score': 1.7971469008117864,
        'country': 'GB',
        'countryAlt': 'IE',
        'region': 'Europe',
        'topRegion': 'Europe',
        'subRegion': 'Northern Europe'
    }, {
        'id': '200',
        'name': 'Karen Herrera',
        'score': 12.10225278411596,
        'country': 'ES',
        'countryAlt': 'GB',
        'region': 'Europe',
        'topRegion': 'Europe',
        'subRegion': 'Southern Europe'
    }, {
        'id': '188',
        'name': 'Darlene Proctor',
        'score': 9.608991621223403,
        'country': 'GB',
        'countryAlt': 'IE',
        'region': 'Europe',
        'topRegion': 'Europe',
        'subRegion': 'Northern Europe'
    }, {
        'id': '105',
        'name': 'Donald Miller',
        'score': 9.776572059793308,
        'country': 'GB',
        'countryAlt': 'AT',
        'region': 'Europe',
        'topRegion': 'Europe',
        'subRegion': 'Northern Europe'
    }, {
        'id': '109',
        'name': 'Sabrina Lara',
        'score': 8.45910530844296,
        'country': 'ES',
        'countryAlt': 'IT',
        'region': 'Europe',
        'topRegion': 'Europe',
        'subRegion': 'Southern Europe'
    }],
    #        ------------------------------------------------------------------------------------
    #                                   RaceEthnicityResponse Samples
    #        ------------------------------------------------------------------------------------
    [{
        'id': '607',
        'firstName': 'Patrick',
        'lastName': 'Rasmussen',
        'raceEthnicityAlt': 'A',
        'raceEthnicity': 'W_NL',
        'score': 22.948248540996016
    }, {
        'id': '282',
        'firstName': 'Christopher',
        'lastName': 'Kelly',
        'raceEthnicityAlt': 'B_NL',
        'raceEthnicity': 'W_NL',
        'score': 7.955888738554523
    }, {
        'id': '914',
        'firstName': 'Thomas',
        'lastName': 'Mcdonald',
        'raceEthnicityAlt': 'B_NL',
        'raceEthnicity': 'W_NL',
        'score': 10.201947264489698
    }, {
        'id': '241',
        'firstName': 'Cameron',
        'lastName': 'Graham',
        'raceEthnicityAlt': 'W_NL',
        'raceEthnicity': 'B_NL',
        'score': 3.5776916899124154
    }, {
        'id': '200',
        'firstName': 'Tracy',
        'lastName': 'Smith',
        'raceEthnicityAlt': 'W_NL',
        'raceEthnicity': 'B_NL',
        'score': 0.4432138744951581
    }, {
        'id': '908',
        'firstName': 'Kimberly',
        'lastName': 'Sellers',
        'raceEthnicityAlt': 'B_NL',
        'raceEthnicity': 'W_NL',
        'score': 4.316583054898527
    }, {
        'id': '37',
        'firstName': 'Eric',
        'lastName': 'Wyatt',
        'raceEthnicityAlt': 'B_NL',
        'raceEthnicity': 'W_NL',
        'score': 4.876180530048689
    }, {
        'id': '606',
        'firstName': 'Joann',
        'lastName': 'Hunter',
        'raceEthnicityAlt': 'B_NL',
        'raceEthnicity': 'W_NL',
        'score': 5.033235484800428
    }, {
        'id': '941',
        'firstName': 'Rebecca',
        'lastName': 'Alexander',
        'raceEthnicityAlt': 'B_NL',
        'raceEthnicity': 'W_NL',
        'score': 6.45911528690918
    }, {
        'id': '58',
        'firstName': 'Jennifer',
        'lastName': 'Martinez',
        'raceEthnicityAlt': 'W_NL',
        'raceEthnicity': 'HL',
        'score': 28.71009666363218
    }],
    #        ------------------------------------------------------------------------------------
    #                                   DiasporaResponse Samples
    #        ------------------------------------------------------------------------------------
    [{
        'id': '538',
        'firstName': 'Charles',
        'lastName': 'Juarez',
        'score': 5.018694044348786,
        'ethnicityAlt': 'Portuguese',
        'ethnicity': 'Hispanic',
        'lifted': True,
        'countryIso2': 'LY'
    }, {
        'id': '50',
        'firstName': 'Craig',
        'lastName': 'Rubio',
        'score': 1.6060483558594125,
        'ethnicityAlt': 'Portuguese',
        'ethnicity': 'Hispanic',
        'lifted': True,
        'countryIso2': 'GF'
    }, {
        'id': '518',
        'firstName': 'Ashley',
        'lastName': 'Johnson',
        'score': 11.337119830452618,
        'ethnicityAlt': 'British',
        'ethnicity': 'Liberia',
        'lifted': True,
        'countryIso2': 'MK'
    }, {
        'id': '139',
        'firstName': 'Jeffrey',
        'lastName': 'Murphy',
        'score': 16.499316179724513,
        'ethnicityAlt': 'British',
        'ethnicity': 'Irish',
        'lifted': False,
        'countryIso2': 'TL'
    }, {
        'id': '564',
        'firstName': 'Darrell',
        'lastName': 'Perez',
        'score': 11.129313165321383,
        'ethnicityAlt': 'Portuguese',
        'ethnicity': 'Hispanic',
        'lifted': True,
        'countryIso2': 'TO'
    }, {
        'id': '458',
        'firstName': 'Jeremiah',
        'lastName': 'Allison',
        'score': 16.470926891304973,
        'ethnicityAlt': 'Irish',
        'ethnicity': 'British',
        'lifted': False,
        'countryIso2': 'NP'
    }, {
        'id': '750',
        'firstName': 'Jennifer',
        'lastName': 'Moore',
        'score': 10.110044737078029,
        'ethnicityAlt': 'Irish',
        'ethnicity': 'British',
        'lifted': False,
        'countryIso2': 'PG'
    }, {
        'id': '985',
        'firstName': 'Adam',
        'lastName': 'Phillips',
        'score': 5.448428097566382,
        'ethnicityAlt': 'Jewish',
        'ethnicity': 'British',
        'lifted': False,
        'countryIso2': 'LB'
    }, {
        'id': '705',
        'firstName': 'Robert',
        'lastName': 'Davies',
        'score': 13.48239707162697,
        'ethnicityAlt': 'Jewish',
        'ethnicity': 'British',
        'lifted': False,
        'countryIso2': 'SN'
    }, {
        'id': '340',
        'firstName': 'Kevin',
        'lastName': 'Kline',
        'score': 5.9249709299274675,
        'ethnicityAlt': 'French',
        'ethnicity': 'Jewish',
        'lifted': False,
        'countryIso2': 'TF'
    }],
    #        ------------------------------------------------------------------------------------
    #                                   ParsedNameResponse Samples
    #        ------------------------------------------------------------------------------------
    [{
        'id': '650',
        'name': 'Oscar Lawrence',
        'nameParserType': 'FN1LN1',
        'nameParserTypeAlt': None,
        'firstLastName': {
            'id': None,
            'firstName': 'Oscar',
            'lastName': 'Lawrence'
        },
        'score': 1.1028782830206576
    }, {
        'id': '304',
        'name': 'Jesse Johnston',
        'nameParserType': 'FN1LN1',
        'nameParserTypeAlt': None,
        'firstLastName': {
            'id': None,
            'firstName': 'Jesse',
            'lastName': 'Johnston'
        },
        'score': 23.63613617145121
    }, {
        'id': '802',
        'name': 'Kenneth Mcgee',
        'nameParserType': 'FN1LN1',
        'nameParserTypeAlt': None,
        'firstLastName': {
            'id': None,
            'firstName': 'Kenneth',
            'lastName': 'Mcgee'
        },
        'score': 55.37036489790589
    }, {
        'id': '618',
        'name': 'Lucas Torres',
        'nameParserType': 'FN1LN1',
        'nameParserTypeAlt': None,
        'firstLastName': {
            'id': None,
            'firstName': 'Lucas',
            'lastName': 'Torres'
        },
        'score': 27.728602874596294
    }, {
        'id': '889',
        'name': 'Rhonda Herrera',
        'nameParserType': 'FN1LN1',
        'nameParserTypeAlt': None,
        'firstLastName': {
            'id': None,
            'firstName': 'Rhonda',
            'lastName': 'Herrera'
        },
        'score': 37.22560301808376
    }, {
        'id': '959',
        'name': 'Molly Dixon',
        'nameParserType': 'FN1LN1',
        'nameParserTypeAlt': None,
        'firstLastName': {
            'id': None,
            'firstName': 'Molly',
            'lastName': 'Dixon'
        },
        'score': 15.556550881794742
    }, {
        'id': '974',
        'name': 'Devin Fernandez',
        'nameParserType': 'FN1LN1',
        'nameParserTypeAlt': None,
        'firstLastName': {
            'id': None,
            'firstName': 'Devin',
            'lastName': 'Fernandez'
        },
        'score': 37.21015080658581
    }, {
        'id': '254',
        'name': 'Stacey George',
        'nameParserType': 'LN1FN1',
        'nameParserTypeAlt': None,
        'firstLastName': {
            'id': None,
            'firstName': 'George',
            'lastName': 'Stacey'
        },
        'score': 9.445291910747269
    }, {
        'id': '205',
        'name': 'David Davis',
        'nameParserType': 'FN1LN1',
        'nameParserTypeAlt': None,
        'firstLastName': {
            'id': None,
            'firstName': 'David',
            'lastName': 'Davis'
        },
        'score': 15.079782026578242
    }, {
        'id': '434',
        'name': 'Kevin Garza',
        'nameParserType': 'FN1LN1',
        'nameParserTypeAlt': None,
        'firstLastName': {
            'id': None,
            'firstName': 'Kevin',
            'lastName': 'Garza'
        },
        'score': 46.719939723728054
    }]
)
