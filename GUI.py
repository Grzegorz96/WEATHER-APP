# Modules import.
# Module Config for global variables.
import Config
# Module Functions for validations and invoking and handling requests.
from Functions import update_date, show_weather_info
from tkinter import ttk
from tkinter import *


# Initialization main window of application.
def init_main_window():
    # Creating main window object.
    root = Tk()
    # Creating window geometry and position.
    window_width = 380
    window_height = 660
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
    # Creating title, resizable, background color, and icon.
    root.title("WEATHER.APP")
    root.resizable(width=False, height=False)
    root.config(bg="#B0C4DE")
    root.call("wm", "iconphoto", root._w, PhotoImage(file="Photos/ikona.png"))

    # Returning object of root.
    return root


# Initialization selection panel.
def init_selection_panel(root):
    # Creating top frame.
    top_frame = Frame(root, width=380, height=60, bg="#B0C4DE")
    top_frame.pack()
    # Creating Combobox for selecting cities.
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", fieldbackground="#D3D3D3", background="white")
    current_var = StringVar()
    city_selection = ttk.Combobox(top_frame, textvariable=current_var, width=40)
    city_selection.place(x=20, y=20)
    # Adding Global list_of_city_names to city_selection object's values.
    city_selection["values"] = Config.list_of_city_names
    # Creating button for showing weather for selected city.
    search_button = Button(top_frame, text="Sprawdź", borderwidth=0, bg="#D3D3D3", width=7,
                           command=lambda: show_weather_info(current_var, init_main_label, root))
    search_button.place(x=285, y=20)


# Initialization time label.
def init_date(root):
    # Creating label for displaying time.
    time_label = Label(root, width=380)
    time_label.pack()
    # Start updating the time via functions from Functions.py.
    update_date(root, time_label)


# Initialization main label.
def init_main_label(root, city_info=None):
    # If current_label from Config is instance of Label, will be destroyed and made new one.
    if isinstance(Config.current_label, Label):
        Config.current_label.destroy()
    # Changing background photo.
    Config.photo = PhotoImage(file="Photos/background.png")
    # Creating new main label.
    main_label = Label(root, width=380, height=580, image=Config.photo)
    main_label.pack()
    # If function is called from Main.py this will be omitted, if it is called from Functions.show_weather_info then
    # it will enter this block.
    if city_info:
        # Creating variables from downloaded dictionary keys.
        city = city_info["stacja"]
        temperature = city_info["temperatura"]
        wind_speed = city_info["predkosc_wiatru"]
        humidity = city_info["wilgotnosc_wzgledna"]
        total_precipitation = city_info["suma_opadu"]
        pressure = city_info["cisnienie"]
        # Creating labels with text data about the downloaded weather from a given city.
        Label(main_label, text=city, font=("Arial", 31)).place(x=10, y=10, width=360)
        Label(main_label, text=f"Temperatura: {temperature} \u00B0C", font=("Arial", 12)).place(x=10, y=180, width=200)
        Label(main_label, text=f"Prędkość wiatru: {wind_speed} m/s", font=("Arial", 12)).place(x=10, y=220, width=200)
        Label(main_label, text=f"Wilgotność: {humidity} %", font=("Arial", 12)).place(x=10, y=260, width=200)
        Label(main_label, text=f"Suma opadów: {total_precipitation} mm", font=("Arial", 12)).place(x=10, y=300,
                                                                                                   width=200)
        Label(main_label, text=f"Ciśnienie: {pressure} hPa", font=("Arial", 12)).place(x=10, y=340, width=200)
    # Assignment new main_label to destroyed current_label from Config.
    Config.current_label = main_label
