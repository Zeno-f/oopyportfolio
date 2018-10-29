import json
import requests


class Buienradar(object):
    def __init__(self):
        self.feed = self.request_weather_data()
        self.update_weather_data()

    def request_weather_data(self):
        """Requests buienradar data and returns it as a dictionary"""
        try:
            response = requests.get("https://api.buienradar.nl/data/public/2.0/jsonfeed")
        except requests.RequestException:
            return 'no connection'
        else:
            return json.loads(response.text)

    def update_weather_data(self):
        self.feed = self.request_weather_data()


class WeatherStation(Buienradar):
    def __init__(self):
        super().__init__()
        self.meetstation_locations = self.locations_list()
        self.update_extremes()

    def netherlands_extreme_weather(self, weather_element, positive):
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
        if self.feed != 'no connection':
            for value in self.feed['actual']['stationmeasurements']:
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
        else:
            pass
        return weather_location

    def update_extremes(self):
        """updates extreme values for the overview"""
        self.max_temperature = self.netherlands_extreme_weather('temperature', True)
        self.min_temperature = self.netherlands_extreme_weather('temperature', False)
        self.max_sun = self.netherlands_extreme_weather('sunpower', True)
        self.max_windy = self.netherlands_extreme_weather('windspeedBft', True)
        self.min_windy = self.netherlands_extreme_weather('windspeedBft', False)

    def locations_list(self):
        meetstation_locations = []
        if self.feed != 'no connection':
            for meetstation in self.feed['actual']['stationmeasurements']:
                if meetstation['regio'] == 'Noordzee':
                    pass
                else:
                    meetstation_locations.append(meetstation['regio'])
        else:
            pass
        return meetstation_locations
