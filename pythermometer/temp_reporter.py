from os import path
from threading import Timer
import sys
import json
import requests
from pprint import pprint
from result import Result
from temp_post import save_record

def initialize():
    here = path.abspath(path.dirname(__file__))

    with open(path.join(here,'config.json')) as config_json:
        config = json.load(config_json)

    return config

def celsius_to_fahrenheit(temperature):
    '''Converts a temperature in degrees Celsius to a temperature in degrees Fahrenheit

    Args:
        temperature: The temperature in degrees Celsius

    Returns:
        The temperature in degrees Fahrenheit
    '''
    
    return temperature * 1.8 + 32

def get_temperature_reading(fileName):
    '''Gets a successful temperature reading or records a failure

    Args:
        fileName: The full path to the file containing temperature data

    Returns:
        A Result containing the temperature in degrees Fahrenheit or a failure message
    '''

    with open(fileName, mode='rt', encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines()]

    statusLine = lines[0]
    temperatureLine = lines[1]

    #Sensor took a temperature reading
    tookReading = statusLine.find('YES')

    if (tookReading < 0):
        return Result.Fail('No temperature reading was taken')

    #temperature is present
    temperatureIndex = temperatureLine.find('=')

    if(temperatureIndex < 0):
        return Result.Fail('Temperature data was malformed.')

    temperatureCelsius = float(temperatureLine[temperatureIndex + 1:]) / 1000.00

    temperatureFahrenheit = celsius_to_fahrenheit(temperatureCelsius)

    reading = {'temperature' : temperatureFahrenheit, 'reading_time': 'mock'}

    return Result.Success(reading)

def report_temperature_loop(config):
    temperatureReadingResult = get_temperature_reading(config['client']['temperature_file'])

    if (temperatureReadingResult.success()):
        save_record(config['server'], temperatureReadingResult.value())

    pprint(temperatureReadingResult.value())
    Timer(config['client']['read_interval_seconds'], report_temperature_loop, [config]).start()


def main():
    config = initialize()
    report_temperature_loop(config)
    