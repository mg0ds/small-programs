def convert_to_snake(data):
    word = ""
    i = 0
    for letter in data:
        if letter == "-" and i == 0:
            letter = ""
        elif letter == "-" and i != 0:
            letter = "_"
        elif letter == letter.upper() and letter.isalpha() and i == 0:
            letter = letter.lower()
        elif letter == letter.upper() and letter.isalpha() and i != 0:
            letter = "_" + letter.lower()
        elif letter.isnumeric() and word[-1].isnumeric() is False:
            letter = "_" + letter
        word += letter
        i += 1
    return word

def snake_case_keys(obj):
    if isinstance(obj, dict):
        obj = {convert_to_snake(key): value for key, value in obj.items()}
        for key, value in obj.items():
              if isinstance(value, list):
                    for idx, item in enumerate(value):
                        obj[key] = snake_case_keys(value)
              obj[key] = snake_case_keys(value)
    elif isinstance(obj, list):
        for idx, item in enumerate(obj):
            obj[idx] = snake_case_keys(item)
    return obj


test3 = {
        "darthVader": {
            "firstName": "Anakin",
            "lastName": "Skywalker",
            "appearance": {
                "helmetColor": "black",
                "armorColor": "black",
                "capeColor": "black",
            },
        }
    }

test4 = {
        "random": [
            "Luke",
            [
                "blowing up the death star",
                {"skillName": "bulls-eye womprats",
                 "skillParameters": "with my T47"},
            ],
        ]
    }
