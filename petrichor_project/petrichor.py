# ==============================================================================================================
# Petrichor is a menu-based weather logging programme that allows users to; log, view, and search weather data
# Username: ph359 
# ==============================================================================================================

#Imports 
import re       # Used to validate users input      
import csv      # Used for saving and loading data to .csv files

from petrichor_tools import validate_date, validate_city, validate_temperature, validate_positive_number, get_today_date, aqi_description

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
                f"AQI: {self.aqi} ({aqi_description(self.aqi)})")

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
        # Does the counting automatically
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
        self.entry_type_count()
        self.most_logged_city()

        if temperature:
            print(f"Average Temperature: {sum(temperature) / len(temperature):.1f}C")
            print(f"Highest Reading:     {max(temperature)}C")
            print(f"Lowest reading:      {min(temperature)}C")
        else:
            print("No temperature data logged. ")
        
        print("-------------------------")

    def most_logged_city(self):
        # Counts how many times each city appears and returns most logged 
        if not self.entries:
            print("No entries logged. ")
            return
        
        city_count = {}
        for entry in self.entries:
            if entry.city in city_count:
                city_count[entry.city] += 1
            else:
                city_count[entry.city] = 1
        
        top_city = max(city_count, key = city_count.get)
        print(f"\nMost logged city: {top_city} ({city_count[top_city]} entries)")
    
    def entry_type_count(self):
        # Counts the different types of entries
        if not self.entries:
            print("No entries logged. ")
            return
        
        observation_count = 0
        Atmospheric_count = 0
        basic_count = 0

        for entry in self.entries:
            if entry.type == "WeatherObservation":
                observation_count += 1 
            elif entry.type == "AtmosphericReading":
                Atmospheric_count += 1
            elif entry.type == "WeatherLog":
                basic_count += 1 
        
        print(f"\n----- Entry Types ------")
        print(f"Weather Observation:   {observation_count}")
        print(f"Atmospheric Readings:  {Atmospheric_count}")
        print(f"Basic Entries:         {basic_count}")
        print("----------------------------")
    
    def save_to_csv(self, filename="weather_log.csv"):
        # Saves all entries to a .csv file so data is not lost when programme is terminated 
        with open(filename, "w", newline="") as file:
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
                                                  float(row[6]))
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

# Display Menu                         
def display_menu():
    # Prints the menu options to terminal
    print("\n==============================")
    print("         PETRICHOR            ")
    print("  Weather logging Programme   ")
    print("==============================")
    print("1. Log Weather Observation")
    print("2. Log Atmospheric Reading")
    print("3. Log Basic Weather Entry")
    print("4.        View all Entries")
    print("5.          Search by city")
    print("6.    Filter by Conditions")
    print("7.      Summary Statistics")
    print("8.            Delete Entry")
    print("9.                Save Log")
    print("10.               Load log")
    print("11.                   Exit")
    print("==============================")

    return input("Select option: ").strip()

# OPTION - 1
def log_weather_observation():
    # Collects input from the user for Weather Observation
    print("\n----- Log Weather Observation -----")
   
    city = input("Enter city: ").strip().title()                    # .strip().title() removes extra spaces and capitalise the first letter
    if not validate_city(city):
        print("Invalid city. Only letter and spaces allowed")
        return None

    today = get_today_date()
    date = input("Enter date (DD-MM-YYYY) [press Enter for today's date: {today}]: ").strip()
    if date == "":
        date = today
    if not validate_date(date):
        print("Invalid date. Please use DD-MM-YYYY format. ")
        return None
    
    print(f"Valid conditions: {WeatherLog.VALID_CONDITIONS}")
    condition = input("Enter condition: ").strip().title()
    if condition not in WeatherLog.VALID_CONDITIONS:                # Check if condition is valid before creating entry
        print("Invalid condition. Entry not logged. ")
        return None
    
    temperature = input("Enter temperature (C): ").strip()          # Float() to convert text into numbers with decimals
    if not validate_temperature(temperature):
        print("invalid temperature")
        return None               
                      
    humidity = input("Enter humidity (%): ").strip()                # int() converts text into numbers.
    if not validate_positive_number(humidity):
        print("Invalid measurement. ")
        return None
    
    wind_speed = (input("Enter wind speed (kn): ").strip())
    if not validate_positive_number(wind_speed):
        print("Invalid measurement. ")
        return None
    
    # Create and return a new WeatherObservation item
    return WeatherObservation(city, date, condition, temperature, humidity, wind_speed)

# OPTION - 2
def log_atmospheric_reading():
    # Collects input from the user for atmospheric reading
    print("\n----- Log Atmospheric Reading -----")

    city = input("Enter city: ").strip().title() 
    if not validate_city(city):
        print("Invalid city. Only letter and spaces allowed")
        return None
                      
    today = get_today_date()
    date = input("Enter date (DD-MM-YYYY) [press Enter for today's date: {today}]: ").strip()
    if date == "":
        date = today
    if not validate_date(date):
        print("Invalid date. Please use DD-MM-YYYY format. ")
        return None
    
    print(f"Valid conditions: {WeatherLog.VALID_CONDITIONS}")
    condition = input("Enter condition: ").strip().title()
    if condition not in WeatherLog.VALID_CONDITIONS:
        print("Invalid condition. Entry not logged. ")
        return None
    
    visibility = (input("Enter visibility (km): ").strip())
    if not validate_positive_number(visibility):
        print("Invalid distance. ")
        return None
    
    pressure = (input("Enter pressure (hPa): ").strip())
    if not validate_positive_number(pressure):
        print("Invalid pressure. ")
        return None
    
    aqi = (input("Enter air quality index (0 - 150+): ").strip())
    if not validate_positive_number(aqi):
        print("Invalid AQI value. ")
        return None

    return AtmosphericReading(city, date, condition, visibility, pressure, aqi)

# OPTION - 3 
def log_basic_entry():
    # Collects input from the user for a basic weather entry
    print("\n----- Log Basic Weather Entry -----")

    city = input("Enter city: ").strip().title()      
    if not validate_city(city):
        print("Invalid city. Only letter and spaces allowed")
        return None      
           
    today = get_today_date()
    date = input("Enter date (DD-MM-YYYY) [press Enter for today's date: {today}]: ").strip()
    if date == "":
        date = today
    if not validate_date(date):
        print("Invalid date. Please use DD-MM-YYYY format. ")
        return None
    
    print(f"Valid conditions: {WeatherLog.VALID_CONDITIONS}")
    condition = input("Enter condition: ").strip().title()
    if condition not in WeatherLog.VALID_CONDITIONS:
        print("Invalid condition. Entry not logged. ")
        return None
    
    return WeatherLog(city, date, condition)

# MAIN FUNCTION
def main(): 
    core = PetrichorCore()
    print("\nLoading...")
    print("Loading...")
    print("loaded")

    while True:
        choice = display_menu()

        if choice == "1":
            entry = log_weather_observation()
            if entry:
                core.add_entry(entry)

        elif choice == "2":
            entry = log_atmospheric_reading()
            if entry:
                core.add_entry(entry)
        
        elif choice == "3":
            entry = log_basic_entry()
            if entry:
                core.add_entry(entry)
        
        elif choice == "4":
            core.display_all()
        
        elif choice == "5":
            city = input("Enter city to search: ").strip().title()
            core.search_by_city(city)
        
        elif choice == "6":
            print(f"Valid conditions: {WeatherLog.VALID_CONDITIONS}")
            condition = input("Enter condition: ").strip().title()
            core.filter_by_condition(condition)

        elif choice == "7":
            core.statistics()
        
        elif choice == "8":
            core.display_all()
            try:
                index = int(input("Enter entry number to be deleted: ").strip())
                core.remove_entry(index - 1)
            except ValueError:
                print("Invalid input. Please enter valid entry number. ")
        
        elif choice == "9":
            core.save_to_csv()

        elif choice == "10":
            core.load_from_csv()
        
        elif choice == "11":
            print("Exiting Petrichor. Goodbye")
            break

        else:
            print("Invalid option. Please try again")
# Runs the main function only when this file is run directly
if __name__ == "__main__":
    main()