import requests
import json
import matplotlib.pyplot as plt

pokemon_url = "https://pokeapi.co/api/v2/pokemon/?limit=1000"
pokemon_json = requests.get(pokemon_url).text

print(pokemon_json)
pokemon = json.loads(pokemon_json)
# print(pokemon['results'])
# print(len(pokemon['results']))
pokemon_weights = []
pokemon_ids = []
for result in pokemon['results']:
    res_json = requests.get(result['url']).json()
    # print(result['name'], json.dumps(res_json, indent=2))
    pokemon_weights.append(res_json['id'])
    pokemon_ids.append(res_json['weight'])
    print(result['name'], "Weight:", res_json['weight'])