# Import modules.
from GUI import init_main_window, init_selection_panel, init_main_label, init_date
from Functions import download_city_names_and_stations_id

# Mainloop of WEATHER.APP.
if __name__ == "__main__":
    # Creating root object, object of application.
    root = init_main_window()
    # Downloading lists of cities and stations id from Requests and assigning them to global variables.
    download_city_names_and_stations_id()
    # Creating panel for selection city.
    init_selection_panel(root)
    # Creating panel with date.
    init_date(root)
    # Creating label for displaying weather info.
    init_main_label(root)
    # Running root object to mainloop.
    root.mainloop()
