import Config
from Requests import download_city_names_and_stations_id, download_city_weather_info
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import datetime


# Initialization main window of application
def init_main_window():
    root = Tk()
    window_width = 380
    window_height = 660
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
    root.title("WEATHER.APP")
    root.resizable(width=False, height=False)
    root.config(bg="#B0C4DE")
    root.call("wm", "iconphoto", root._w, PhotoImage(file="ikona.png"))
    return root


# Initialization selection panel
def init_selection_panel(root):
    # Downloading lists of cities and stations id from Requests
    list_of_city_names, list_of_stations_id = download_city_names_and_stations_id()
    # Creating top frame
    top_frame = Frame(root, width=380, height=60, bg="#B0C4DE")
    top_frame.pack()
    # Creating Combobox for selecting cities
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", fieldbackground="#D3D3D3", background="white")
    current_var = StringVar()
    city_selection = ttk.Combobox(top_frame, textvariable=current_var, width=40)
    city_selection.place(x=20, y=20)
    city_selection["values"] = list_of_city_names
    # Creating button for showing weather for selected city
    search_button = Button(top_frame, text="Sprawdź", borderwidth=0, bg="#D3D3D3", width=7,
                           command=lambda: show_weather_info(current_var, list_of_city_names, list_of_stations_id,
                                                             root))
    search_button.place(x=285, y=20)


# Initialization time label
def init_date(root):
    time_label = Label(root, width=380)
    time_label.pack()
    # Starting update date
    update_date(root, time_label)


# Updating date
def update_date(root, time_label):
    # assignment new date and time from now to variables
    date = f"{datetime.datetime.now().date()}"
    time = f"{datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}"
    # Config time_label for new data
    time_label.config(text=f"{date} {time}")
    # Recursion of function after 1s
    root.after(1000, update_date, root, time_label)


# Initialization main label
def init_main_label(root, city_info=None):
    # if current_label from Config is instance of Label, will be destroyed and made new one
    if isinstance(Config.current_label, Label):
        Config.current_label.destroy()

    Config.photo = PhotoImage(file="background.png")
    main_label = Label(root, width=380, height=580, image=Config.photo)
    main_label.pack()
    # if function is called form main this will be omitted, if it is called form search_button city_info={}
    if city_info:
        # Creating variables
        city = city_info["stacja"]
        temperature = city_info["temperatura"]
        wind_speed = city_info["predkosc_wiatru"]
        humidity = city_info["wilgotnosc_wzgledna"]
        total_precipitation = city_info["suma_opadu"]
        pressure = city_info["cisnienie"]
        # Creating Labels with  text data
        Label(main_label, text=city, font=("Arial", 31)).place(x=10, y=10, width=360)
        Label(main_label, text=f"Temperatura: {temperature} \u00B0C", font=("Arial", 12)).place(x=10, y=180, width=200)
        Label(main_label, text=f"Prędkość wiatru: {wind_speed} m/s", font=("Arial", 12)).place(x=10, y=220, width=200)
        Label(main_label, text=f"Wilgotność: {humidity} %", font=("Arial", 12)).place(x=10, y=260, width=200)
        Label(main_label, text=f"Suma opadów: {total_precipitation} mm", font=("Arial", 12)).place(x=10, y=300,
                                                                                                   width=200)
        Label(main_label, text=f"Ciśnienie: {pressure} hPa", font=("Arial", 12)).place(x=10, y=340, width=200)
    # Assignment new main_label to destroyed current_label from Config
    Config.current_label = main_label


# Showing weather info
def show_weather_info(current_var, list_of_city_names, list_of_stations_id, root):
    # Validation of selected city by user
    if current_var.get() in list_of_city_names:
        # if validation passes will be downloaded info about selected city by user
        city_info = download_city_weather_info(current_var, list_of_city_names, list_of_stations_id)
        # call initialization of main label with new city data
        init_main_label(root, city_info)

    # if validation fails, a warning will be shown
    else:
        messagebox.showwarning("Błędne miasto", "Wybierz poprawne miasto")
