from requests import get
from json import loads


# Download city names and stations id
def download_city_names_and_stations_id():
    url = "https://danepubliczne.imgw.pl/api/data/synop"
    # Sending request for url
    response = get(url)
    city_names = []
    stations_id = []
    # .text making string of list of dictionaries, then we must convert it on list of dictionaries by loads
    for city in loads(response.text):
        # Updating two lists
        city_names.append(city["stacja"])
        stations_id.append(city["id_stacji"])

    return city_names, stations_id


# Download weather info about specific city
def download_city_weather_info(current_var, list_of_city_names, list_of_stations_id):
    # Making index of station_id that corresponds to a selected city
    index_station_id = list_of_city_names.index(current_var.get())
    # Assignment station_id to the corresponding station_id from list_of_stations_id
    station_id = list_of_stations_id[index_station_id]
    url = f"https://danepubliczne.imgw.pl/api/data/synop/id/{station_id}"
    response = get(url)
    # Conversion string to the dictionary
    converted_response = loads(response.text)

    return converted_response
