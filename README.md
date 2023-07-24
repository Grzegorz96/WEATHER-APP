![logo pogoda](https://github.com/Grzegorz96/WEATHER-APP/assets/129303867/011dd406-5ba8-4f1d-9937-e086b7ceed3b)
# WEATHER.app

WEATHER_app is a weather application that connects to the danepubliczne.imgw.pl API and creates a list of cities and a list of their weather station identifiers from the available downloaded data. The user selects the city whose weather he wants to check from the list of available cities, then the program downloads the latest weather information in this city and displays it. The application performs queries in real time, moreover, it has a dynamic creation of a list of cities, so it will adapt to any change (addition of new cities, removal of existing ones) on the server.


## Description of the modules
The program consists of five modules. The module that makes direct requests to the weather API is Weather_request.py. It performs previously assigned queries and returns answers to individual modules. Functions.py calls query functions to the backend and handles response objects appropriately. Using functions.py, the program validates the entered data and decides what to do with it, then checks what is the response from the server and also decides what to do with it. It is also responsible for clock updates. The GUI.py module initializes objects on the user's screen, and with its help you can enter data into the program. The Config.py file contains global variables for the program. Main.py serves as the executor for the program. It calls the initialization functions, the function that get the global lists of city and station id, finally, the mainloop method is executed on the root (application) object.


## Features
- Getting real-time weather information.
- Dynamically creating a global list of cities from information downloaded from the API, adapting the application to changes on the server.
- Clock updating every second
- The ability to check the temperature, wind speed, humidity, rainfall and pressure in 62 Polish cities.
- Handling response errors from the server.
- Validation of entered data.


## Technology used

**Client:** 
- Languages: Python
- Third Party Libraries: Tkinter, requests

**Server:** 
- [Datapubliczne.imgw.pl API interface](https://danepubliczne.imgw.pl/apiinfo)
