# ====================================================================================================================
# test_petrichor.py will test the functionality of the programme
# ====================================================================================================================

#IMPORTS
from petrichor_tools import validate_date, validate_city, validate_temperature, validate_positive_number
from petrichor import WeatherLog, WeatherObservation, AtmosphericReading, PetrichorCore

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

# CITY TEST
def test_valid_city():
    # A City name will return true
    assert validate_city("Canterbury") == True

def test_valid_city_with_space():
    # City with a space will return true
    as