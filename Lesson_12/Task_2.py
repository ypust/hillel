import json

import requests


def get_pilot_data(url):
    pilot_response = requests.get(url)
    if pilot_response.status_code == 200:
        pilot_data = pilot_response.json()
        homeworld_url = pilot_data["homeworld"]
        homeworld_response = requests.get(homeworld_url)
        if homeworld_response.status_code == 200:
            hw_data = homeworld_response.json()
            pilot_data["homeworld_planet"] = hw_data["name"]
            return {
                "name": pilot_data["name"],
                "height": pilot_data["height"],
                "mass": pilot_data["mass"],
                "planet": hw_data["name"],
                "planet_link": homeworld_url
            }
    else:
        raise Exception(f'Cannot download pilot data from {url}')


starship_url = 'https://swapi.dev/api/starships/10'
response = requests.get(starship_url)

if response.status_code == 200:
    ship_data = response.json()
    pilot_urls = ship_data["pilots"]
    pilots = list(map(get_pilot_data, pilot_urls))

    starship = {
        "name": ship_data["name"],
        "max_speed": ship_data["max_atmosphering_speed"],
        "class": ship_data["starship_class"],
        "pilots": pilots
    }

    with open("starship_request_result.json", "w") as ship_file:
        ship_file.write(json.dumps(starship, indent=4))

    print(json.dumps(starship, indent=4))
