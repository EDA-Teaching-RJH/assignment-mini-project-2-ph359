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
        self.condition = condition
        self.type = "WeatherLog"
        
    def __str__(self): 
        # prints out entry 
        return f"[{self.date}] {self.city} - {self.condition}"                
                        
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
        self.type = "WeatherObservation"
    
    def __str__(self):
        # Overrides the print in 'Weather Log'to include additional details
        return (f"[{self.date}] {self.city} - {self.condition} |" 
                f"[Temp: {self.temperature}C] |"    
                f"Humidity: {self.humidity}% |"
                f"Wind Speed: {self.wind_speed}kn |")
    
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
        self.type = "AtmosphericReading"

    def __str__(self):
        # Overrides the print in 'Weather Log' to include extra measurements
        return (f"[{self.date}] {self.city} - {self.condition} |"
                f"Visibility: {self.visibility} km |"
                f"Pressure: {self.pressure} hPa |"
                f"AQI: {self.aqi}")

# CLASS 4 - Petrichor Core (Manager)
# Centre of the programme, manages all entries
class PetrichorCore:

    def __init__(self):
        # Creates empty list when programme starts 
        self.entries = []
    
    def add_entry(self, entry):
        # Adds new entry
        self.entries.append(entry)
        # append() addes an item to the end of a list
        print(f"Entry added for {entry.city} on {entry.date}. ")

    def remove_entry(self, index):
        # Removes an entry by its position number on list
        if 0 <= index < len(self.entries):
            removed = self.entries.pop(index)
            print(f"Entry for {removed.city} on {removed.date} removed. ")
        else:
            print("Invalid entry number. ")
    
    def display_all(self):
        # Displays every entry 
        if not self.entries:
            print("No entries logged. ")
        else:
            print("\n----- All Entries -----")
            for i, entry in enumerate(self.entries):
                print(f"{i + 1}. {entry}")
            print("-------------------------")

    def search_by_city(self, city):
        # Loops through every entry and check for a match
        result = []
        for entry in self.entries:
            if city.lower() in entry.city.lower():
        # Lower() converts all inputs to lowercase, so python knows the inputs are the same. 
                result.append(entry)
        
        if not result:
            print(f"No entrie found for {city}. ")
        else:
            print(f"\n----- Results for {city} -----")
            for i, entry in enumerate(result):
        # enumerate() gives a position number and item at the same time. 
        # Does the counting manually
                print(f"{i + 1}. {entry}")
            print("---------------------------------")

    def filter_by_condition(self, condition):
        # Filters all entries by specific weather condition
        result = []
        for entry in self.entries:
            if entry.condition.lower() == condition.lower():
                result.append(entry)
            
            if not result:
                print(f"No entries found with condition: {condition}. ")
            else:
                print(f"\n----- Entries with {condition} -----")
                for i, entry in enumerate(result):
                    print(f"{i + 1}. {entry}")
                print("---------------------------------------")

    def statistics(self):
        # Calculates and displays a summery of statistics from all logged entries
        if not self.entries:
            print("No entries logged. ")
            return
        
        temperature = []
        # Collects temperatures from entries that have a temperature
        for entry in self.entries:
            try:
                temperature.append(entry.temperature)
            except AttributeError: 
        # Entry does not have a temperature - skips it
                pass
            
        print("\n----- Statistics -----")
        print(f"total entries logged: {len(self.entries)}")

        if temperature:
            print(f"Average Temperature: {sum(temperature) / len(temperature):.1f}C")
            print(f"Highest Reading:     {max(temperature)}C")
            print(f"Lowest reading:      {min(temperature)}C")
        else:
            print("No temperature data logged. ")
        
        print("-------------------------")

    def save_to_csv(self, filename="weather_log.csv"):
        # Saves all entries to a .csv file so data is not lost when programme is terminated 
        with open(filename, "W", newline="") as file:
            writer = csv.writer(file)
        # Writes the header row first
            writer.writerow(["type", "city", "date", "condition", "temperature",
                            "humidity", "wind_speed", "visibility", "pressure", "AQI"])
        
            for entry in self.entries:
                if entry.type == "WeatherObservation":
                    writer.writerow([entry.type, entry.city, entry.date,
                                    entry.condition, entry.temperature, 
                                    entry.humidity, entry.wind_speed,
                                    "", "", ""])
                
                 elif entry.type == "AtmosphericReading":
                    writer.writerow([entry.type, entry.city, entry.date,
                                    entry.condition, "", "", "",
                                    entry.visibility, entry.pressure, entry.aqi])
            
                elif entry.type == "WeatherLog":
                    writer.writerow([entry.type, entry.city, entry.date, entry.condition,
                                    "", "", "", "", "", ""])
        print(f"Log saved to {filename}. ")
    
    def load_from_csv(self, filename="weather_log.csv"):
        # Loads entries from a .csv file into programme
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                next(reader) # Skips the header row
                for row in reader:
                    if row[0] == "WeatherObservation":
                        entry = WeatherObservation(row[1], row[2], row[3],
                                           float(row[4]), float(row[5]),
                                            int(row[6]))
                        self.entries.append(entry)
                    elif row[0] == "AtmosphericReading":
                        entry = AtmosphericReading(row[1], row[2], row[3],
                                                   float(row[7]), float(row[8]),
                                                   int(row[9]))
                        self.entries.append(entry)
                    elif row[0] == "WeatherLog":
                        entry = WeatherLog(row[1], row[2], row[3])
                        self.entries.append(entry)
            
            print(f"Log loaded from {filename}. ")
        except FileNotFoundError:
            print("No saved log found. ")
                             
