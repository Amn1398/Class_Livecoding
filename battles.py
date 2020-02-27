import requests
import json

pokemon_url = "https://pokeapi.co/api/v2/pokemon/?limit=1000"
pokemon_json = requests.get(pokemon_url).text

print(pokemon_json)
pokemon = json.loads(pokemon_json)
# print(pokemon['results'])
# print(len(pokemon['results']))
for result in pokemon['results']:
    res_json = requests.get(result['url']).json()
    # print(result['name'], json.dumps(res_json, indent=2))
    print(result['name'], "Weight:", res_json['weight'])
print("test")