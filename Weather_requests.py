# Import module requests.
from requests import get, RequestException, Response


# Download city names and stations id.
def download_cities_info_request():
    try:
        # Creating url for sending request.
        url = "https://danepubliczne.imgw.pl/api/data/synop"
        # Sending request for url
        response = get(url)

    # When we can't send request, program creating response object with 404 error and returning object.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response

    # When request was send successfully, return response from backend.
    else:
        return response


# Download weather info about specific city.
def download_city_info_request(station_id):
    try:
        # Creating url with station id as a sub-resource.
        url = f"https://danepubliczne.imgw.pl/api/data/synop/id/{station_id}"
        # Sending request and getting response.
        response = get(url)

    # When we can't send request, program creating response object with 404 error and returning object.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response

    # When request was send successfully, return response from backend.
    return response
