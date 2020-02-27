import requests
import json

pokemon_url = "https://pokeapi.co/api/v2/pokemon/?limit=1000"
pokemon_json = requests.get(pokemon_url).text

print(pokemon_json)
pokemon = json.loads(pokemon_json)
#print(pokemon['results'])
#print(len(pokemon['results']))
for result in pokemon['results']:
    print(result['name'], result['url'])