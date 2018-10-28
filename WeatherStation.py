import json
import requests


class WeatherStation(object):

    def __init__(self):
        pass


class MaximumValues(object):

    def __init__(self):
        self.update_extremes()

    def update_extremes(self):
        """updates extreme values for the overview"""
        self.max_temperature = netherlands_extreme_weather('temperature', True)
        self.min_temperature = netherlands_extreme_weather('temperature', False)
        self.max_sun = netherlands_extreme_weather('sunpower', True)
        self.max_windy = netherlands_extreme_weather('windspeedBft', True)
        self.min_windy = netherlands_extreme_weather('windspeedBft', False)


# has to happen periodically TODO make this happen
def request_weatherdata():
    """Requests buienradar data and returns it as a dictionary"""
    response = requests.get("https://api.buienradar.nl/data/public/2.0/jsonfeed")
    return json.loads(response.text)


def netherlands_extreme_weather(weather_element, positive):
    """Determines the extreme values of the weather in the netherlands

    Looks at all the weatherstations in the netherlands and filters out the highest or lowest value.

    Args:
        weather_element: Specify what element of the weather should be determined what its extreme value is. It can take
            the following strings: 'temperature', 'sunpower', 'windspeed', 'windspeedBft', 'windgusts' and all other
            keys in the elements in buienradar_feed['actual']['stationmeasurements'] as long as they either contain
            a value or a NoneType
        positive: Set this to True to get a maximum value, set it to False for a minimum value

    Returns:
        A list containing the location with the highest or lowest value and the value. For example:
        ['Eindhoven', 14.4]
    """
    weather_location = []
    for value in buienradar_feed['actual']['stationmeasurements']:
        # locations on the Noordzee are not interesting for us, neither are elements containing no information currently
        # TODO value = 0 check is only for weather, place that in its own function
        if value[weather_element] is None or value['regio'] == 'Noordzee':
            pass
        # Exception for stupid JSON Data, windspeedBft
        elif int(value[weather_element]) is 0 and weather_element is 'windspeedBft':
            pass
        elif len(weather_location) == 0:
            weather_location = [value['regio'], value[weather_element]]
        elif positive is True:
            if float(weather_location[1]) < float(value[weather_element]):
                weather_location = [value['regio'], value[weather_element]]
            else:
                pass
        elif positive is False:
            if float(weather_location[1]) > float(value[weather_element]):
                weather_location = [value['regio'], value[weather_element]]
            else:
                pass
    return weather_location


buienradar_feed = request_weatherdata()

# generating a list of meetstations to display for selection in the interface
# run once on starting the program
meetstation_locations = []
for meetstation in buienradar_feed['actual']['stationmeasurements']:
    if meetstation['regio'] == 'Noordzee':
        pass
    else:
        meetstation_locations.append(meetstation['regio'])

