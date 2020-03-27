import json

# json_data = '{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}'

# parsed_json = (json.loads(json_data))
# print(json.dumps(parsed_json, indent=4, sort_keys=True))

def ver_nombre():
    with open('pete_data.json', 'r') as pete_data:
        pete_info = json.load(pete_data)
        print(pete_info['nombre_curso'])

def cambiar_nombre(nombre):
    with open('pete_data.json', 'r') as pete_data:
        pete_info = json.load(pete_data)
        pete_info['nombre_curso'] = nombre

        with open("pete_data.json", "w", encoding="utf-8") as new_data:
            json.dump(pete_info, new_data, indent=4) 

#cambiar_nombre('curso')
ver_nombre()
