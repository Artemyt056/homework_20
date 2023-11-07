import json

information = {
    'name': 'Petro',
    'surname': 'Korolev',
    'age': '14'
}

convert_information_to_json = json.dumps(information)
print(convert_information_to_json)


information_from_json = json.loads(convert_information_to_json)
print(information_from_json)


with open('information.json', mode='w', encoding='utf-8') as file:
    json.dump(information, file)
    # json.dump(information, file, indent='4')
