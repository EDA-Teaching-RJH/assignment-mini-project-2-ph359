# ====================================================================================================================
# test_petrichor.py will test the functionality of the programme
# ====================================================================================================================

#IMPORTS
from petrichor_tools import validate_date, validate_city, validate_temperature, validate_positive_number
from petrichor import WeatherLog, WeatherObservation, AtmosphericReading, PetrichorCore

# ====================================================================================================================

# DATE TEST
def test_valid_date():
    # Date in the correct format will return true
    assert validate_date("25-03-26") == True

def test_invalid_date_format()
    # Date in incorrect format will return false
    assert validate_date("2026-03-25") == False

def test_invalid_date_letters():
    # Letters instead of numbers will return false
    assert validate_date("25-MA-2026") == False

def test_invalid_date_empty():
    # Empty string should return False
    assert validate_date("") == False 

def test_invalid_date_incomplete():
    assert validate_date("25-03") == False

# ====================================================================================================================

# CITY TEST
def test_valid_city():
    # A City name will return true
    assert validate_city("Canterbury") == True

def test_valid_city_with_space():
    # City with a space will return true
    assert validate_city("New York") == True

def test_invalid_city_numbers():
    # City with numbers will return flase
    assert validate_city("London123") == False

def test_invalid_city_symbols():
    # City with symbols will return false
    assert validate_city("Par!s") == False

def test_invalid_city_empty():
    # Empty string will return false
    assert validate_city("") = False

# ====================================================================================================================

# TEMPERATURE TEST
def test_valid_temp_pos():
    # Positive temperature will return true
    assert validate_temperature("23.4") == True

def test_valid_temp_neg():
    # Negative temperature will return true
    assert validate_temperature("-2.1") == True

def test_valid_temp_zero(): 
    # Zero will return true
    assert validate_temperature("0") == True

def test_invalid_temp_letters():
    # Temperature with letters will return falase
    assert validate_temperature("cold") == False

def test_invalid_temp_empty():
    # Temp with no string will return falase\
    assert validate_temperature("") == False

# ====================================================================================================================

# POSITIVE NUMBER TEST
def test_valid_positive_number():
    # Positive number will return true
    assert validate_positive_number("44") == True

def test_valid_positive_number_decimal():
    #Positive number with decimal will return true
    assert validate_positive_number(90.5) == True

def test_invalid_positive_number_negative():
    # Negative number will return false
    assert validate_positive_number(-6) == False

def test_invalid_positive_number_letters():
    # Letters will return false
    assert validate_positive_number("Letters") == False

def test_invalid_positive_number_empty():
    # Empty string will return false
    assert validate_positive_number("") == False
    
# ====================================================================================================================