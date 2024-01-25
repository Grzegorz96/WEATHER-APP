![logo pogoda](https://github.com/Grzegorz96/WEATHER-APP/assets/129303867/011dd406-5ba8-4f1d-9937-e086b7ceed3b)
# WEATHER.app

WEATHER_app is a weather application that connects to the danepubliczne.imgw.pl API and creates a list of cities and a list of their weather station identifiers from the available downloaded data. The user selects the city whose weather he wants to check from the list of available cities, then the program downloads the latest weather information in this city and displays it. The application performs queries in real time, moreover, it has a dynamic creation of a list of cities, so it will adapt to any change (addition of new cities, removal of existing ones) on the server. Program WEATHER.app is written and optimized for Windows.


## Description of the modules
The program consists of 5 modules, each of which plays a unique role in the functioning of the application. Below is a brief description of each module:

Weather_request.py:
- The Weather_request.py is a module that makes direct requests to the weather API, executes previously triggered queries and forwards the responses to the appropriate place.

Functions.py:
- The Functions.py calls query functions to the backend, handles response objects appropriately, validates entered data, decides what to do with it, and checks server responses, making decisions on further actions. This module is also responsible for clock updates.

GUI.py:
- The GUI.py module initializes objects on the user's screen, allowing data input into the program.

Config.py:
- The Config.py module contains global variables for the entire project. Enables the proper functioning of the program by providing global settings.

Main.py:
- The Main.py module serves as the executor for the program. It calls initialization functions, the function retrieving global lists of cities and station IDs, and finally, the mainloop method is executed on the root (application) object. 


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


## Installation

### To quickly launch the application on Windows:
- Download WEATHER-APP repository:
```bash
 git clone https://github.com/Grzegorz96/WEATHER-APP.git
```
- Enter the directory WEATHER-APP/weather_app_exe.
- If you want to move the Weather_app.exe file, do it together with the Photos folder. You can also create a copy of the .exe file on your desktop.
- Run Weather_app.exe.

### For manually launching the application on the IDE:

#### Requirements:
##### Programs and libraries:
- Python 3.11.1
- IDE, for example Pycharm
- requests 2.31.0
#### Instruction:
- Download WEATHER-APP repository:
```bash
 git clone https://github.com/Grzegorz96/WEATHER-APP.git
```
- Go to the WEATHER-APP directory.
- Open the WEATHER-APP on your IDE.
- Create virtual enviroment for the project (Windows):
```bash
 py -m venv venv
```
- Activate virtual enviroment (Windows):
```bash
 venv/Scripts/activate.bat
```
- Install required packages on your activated virtual enviroment:
```bash
  pip install -r requirements.txt
```
- or
```bash
 pip install requests==2.31.0
```
- Run Main.py on Windows:
```bash
 py .\Main.py
```
Program WEATHER.app connects to the enpoints on the IMGW server, you don't need to create a local backend server.


## Lessons Learned
During the project creation, I learned how to work with JSON files, how to modularize the project, and how crucial it is. When dealing with non-own API, we must consider that data in the database may change, so our program needs to dynamically adapt to these changes. This project allowed me to comprehend that. I also gained the ability to anticipate how the program might behave in various error scenarios and how to handle them effectively.


## Features to be implemented

- The function of showing the weather for future days and times.
- Changing the background when displaying the weather for a specific city.


## Authors

[@Grzegorz96](https://www.github.com/Grzegorz96)


## Contact

E-mail: grzesstrzeszewski@gmail.com


## License

[MIT](https://github.com/Grzegorz96/WEATHER-APP/blob/master/LICENSE.md)


## Screnshoots
##### Screenshot of the main panel
![panel_glowny](https://github.com/Grzegorz96/WEATHER-APP/assets/129303867/21cd5e3f-c630-4f00-a462-a8a1697ca3c9)
##### Screenshot of selecting city
![wybor](https://github.com/Grzegorz96/WEATHER-APP/assets/129303867/188ef1e3-5652-4371-8e17-4d89899c4a40)
##### Screenshots of the info about selected city
![miasto](https://github.com/Grzegorz96/WEATHER-APP/assets/129303867/f2fa8e55-dc02-4ea0-9698-47644199951d)
##### Screenshots of the info about selected city
![miasto2](https://github.com/Grzegorz96/WEATHER-APP/assets/129303867/c5879adc-2900-4524-99ad-d172ddccfbd8)
