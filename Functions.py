# Modules import.
from sys import exit
from tkinter import messagebox
from tkinter import PhotoImage, TclError
from requests import codes
# Import Weather_requests to query the backend API.
from Weather_requests import download_cities_info_request, download_city_info_request
from datetime import datetime
import Config


def download_city_names_and_stations_id():
    """The function responsible for calling the function sending a request to download weather information about all
    available cities and then assigning the city name and station ID values to the global lists."""
    # Calling request for download cities info and assigning response to variable.
    city_info_response = download_cities_info_request()
    # If response has status code 200 then enter this block.
    if city_info_response.status_code == codes.ok:

        # Creating temporary lists.
        city_names = []
        stations_id = []
        # Iterating through the list of dictionaries and assigning the values from their keys to the lists.
        for city in city_info_response.json():
            # Updating two lists
            city_names.append(city["stacja"])
            stations_id.append(city["id_stacji"])

        # When every station id and city name is in temporary lists then assigning it to global lists.
        Config.list_of_city_names = city_names
        Config.list_of_stations_id = stations_id

    # If the response does not have the status 200, it means that there was an error somewhere, and we did not receive
    # the correct JSON, the program will display an error message and shut down.
    else:
        messagebox.showerror("Błąd podczas pobierania informacji pogodowych.",
                             "W chwili obecnej wystąpił błąd i nie udało się pobrać informacji o pogodzie, "
                             "wróć do nas ponownie później.")
        exit(1)


def load_images():
    """The function responsible for loading background image to the global variable."""
    try:
        # Loading background to the global variable.
        Config.images["background"] = PhotoImage(file="Photos/background.png")
    except TclError:
        Config.images["background"] = None


def update_date(root, time_label):
    """The function responsible for updating the time on time_label every one second."""
    # assignment new date and time from now to variables.
    date = f"{datetime.now().date()}"
    time = f"{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}"
    # Config time_label for new data.
    time_label.config(text=f"{date} {time}")
    # Recursion of function after 1s.
    root.after(1000, update_date, root, time_label)


def show_weather_info(current_var, init_main_label, root):
    """The function is responsible for determining the station index for the selected city and then calling the function
    sending a request to download weather information about this city."""
    # Validation of selected city by user.
    if current_var.get() in Config.list_of_city_names:
        # Making index of station_id that corresponds to a selected city. The index of the selected city in
        # list_of_city_names matches the index of the item in list_of_stations_id.
        index_station_id = Config.list_of_city_names.index(current_var.get())
        # Assignment station_id to the corresponding station_id from list_of_stations_id
        station_id = Config.list_of_stations_id[index_station_id]
        # Calling request for download info about selected city by user.
        city_info_response = download_city_info_request(station_id)

        # If response has 200 status code then enter this block.
        if city_info_response.status_code == codes.ok:
            # Creating city info from request body.
            city_info = city_info_response.json()

            # Making sure we got a dictionary and not a list of dictionaries.
            if isinstance(city_info, dict):
                # Call initialization of main label with new city_info.
                init_main_label(root, city_info)

            # If we didn't get dictionary, that means there was an error and we cant display the information about
            # weather. Program displays error message and exit.
            else:
                messagebox.showerror("Błąd podczas pobierania informacji pogodowych.",
                                     "W chwili obecnej wystąpił błąd i nie udało się pobrać informacji o pogodzie, "
                                     "wróć do nas ponownie później.")
                exit(1)

        # We didn't get status 200, there was an error. Program displays error message and exit.
        else:
            messagebox.showerror("Błąd podczas pobierania informacji pogodowych.",
                                 "W chwili obecnej wystąpił błąd i nie udało się pobrać informacji o pogodzie, "
                                 "wróć do nas ponownie później.")
            exit(1)

    # If validation fails, a warning will be shown.
    else:
        messagebox.showwarning("Błędne miasto.", "Wybierz poprawne miasto.")
