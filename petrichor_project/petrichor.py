# ==============================================================================================================
# Petrichor is a menu-based weather logging programme that allows users to; log, view, and search weather data
# Username: ph359 
# ==============================================================================================================

#Imports 
import re       # Used to validate users input      
import csv      # Used for saving and loading data to .csv files
import datetime # Automatically gets today's date

# CLASS 1 - Weather Entry
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
                        
# CLASS 2 - Addtional Entry 
class WeatherObservation(WeatherLog):
    
    def __init__(self, city, date, condition, temperature, humidity,
                 wind_speed):
        super().__init__(city, date, condition)
        #Super() calls __init__ from 'Weather Entry' so we dont have to write existing data, e.g. city, date, condition
        self.temperature = temperature
        self.humidity = humidity
        self.wind_speed = wind_speed
    
    def __str__(self):
        # Overrides the print in 'Weather Entry'to include additional details
        return (f"[{self.date}] {self.city} - {self.condition} |" 
                f"[Temp: {self.temperature}C] |"    
                f"Humidity: {self.humidity}% |"
                f"Wind Speed: {self.wind_speed}kn/kt |")