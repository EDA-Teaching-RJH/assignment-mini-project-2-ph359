# ==============================================================================================================
# Petrichor is a menu-based weather logging programme that allows users to; log, view, and search weather data
# Username: ph359 
# ==============================================================================================================

#Imports 
import re       # Used to validate users input      
import csv      # Used for saving and loading data to .csv files
import datetime # Automatically gets today's date

# CLASS 1 - Weather Entry (Superclass)
class WeatherLog:
    VALID_CONDITIONS = ["Clear", "Cloudy", "Fog", "Drizzle", "Rain", 
                        "Heavy Rain", "Snow", "Thunderstorm"]       

    def __init__(self, city, date, condition):
        # data points
        self.city = city
        self.date = date
        self.conditon = condition

    def __str__(self): 
        # prints out entry 
        return f"[{self.date}] {self.city} - {self.condtion}"                
                        
# CLASS 2 - Addtional Entry (subclass)
# Adds temperature, humidity, and Wind Speed 
class WeatherObservation(WeatherLog):
    
    def __init__(self, city, date, condition, temperature, 
                 humidity, wind_speed):
        
        super().__init__(city, date, condition)
        # Super() calls __init__ from 'Weather Log' so we dont have to write existing data, e.g. city, date, condition
        self.temperature = temperature
        self.humidity = humidity
        self.wind_speed = wind_speed
    
    def __str__(self):
        # Overrides the print in 'Weather Log'to include additional details
        return (f"[{self.date}] {self.city} - {self.condition} |" 
                f"[Temp: {self.temperature}C] |"    
                f"Humidity: {self.humidity}% |"
                f"Wind Speed: {self.wind_speed}kn/kt |")
    
# CLASS 3 - Atmospheric Reading (Subclass)
# Adds visibiltiy, pressure, and the Air quality Index(AQI)
class AtmosphericReading(WeatherLog):

    def __init__(self, city, date, condition, visibility, 
                 pressure, aqi):
        # Super() Calls __init__ from 'Weather Log'
        super().__init__(city, date, condition)
        self.visibility = visibility
        self.pressure = pressure
        self.aqi = aqi 

    def __str__(self):
        # Overrides the print in 'Weather Log' to include extra measurements
        return (f"[{self.date}] {self.city} - {self.condition} |"
                f"Visibility: {self.visibility} km |"
                f"Pressure: {self.pressure} hPa |"
                f"AQI: {self.aqi}")

