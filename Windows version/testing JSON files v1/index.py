import json

# json_data = '{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}'

# parsed_json = (json.loads(json_data))
# print(json.dumps(parsed_json, indent=4, sort_keys=True))

def cambiar_nombre(nombre):
    with open('pete_data.json', 'r') as pete_data:
        pete_info = json.load(pete_data)
        pete_info['nombre_curso'] = nombre


