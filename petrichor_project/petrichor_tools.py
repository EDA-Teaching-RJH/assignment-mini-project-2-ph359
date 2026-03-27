# =====================================================================================================================
# petrichor_tools.py is a custom library for Petrichor
# =====================================================================================================================

#IMPORTS
import re # used for regex pattern matching
import datetime

# Validations
def validate_date(date):
    # Checks date matches DD - MM - YYYY format
    # \d{2} = exactly 2 digits \d{4} = exactly 4 digits
    pattern = re.compile(r"^\d{2}-\d{2}-\d{4}$")         #compile() builds the regex pattern once and stores it
    return bool(pattern.match(date))

def validate_city(city):
    # Checks that city only contains letters and spaces, no numbers
    pattern = re.compile(r"^[A-Za-z\s]+$")
    return bool(pattern.match(city))

def validate_temperature(temperature):
    # Checks temperature is a valid number 
    pattern = re.compile(r"^-?\d+(\.\d+)?$")
    return bool(pattern.match(temperature))

def validate_positive_number(value):
    # Checks value is a positive number
    pattern = re.compile(r"^\d+(\.\d+)?$")
    return bool(pattern.match(value))

#Functions
def get_today_date():
    # Returns today's date as a string in DD-MM-YYYY
    return datetime.datetime.now().strftime("%d-%m-%Y")

def aqi_description(aqi):
    # Returns a description based on the AQI score
    aqi = int(aqi)
    
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 150:
        return "Unhealthy"
    else:
        return "Hazardous"

        