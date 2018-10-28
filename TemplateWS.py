"""The Program Template

things you need
buienradar_feed contains the data from the JSON
app.selected_location contains the selected location
"""

import json
import requests
from tkinter import *
from tkinter import ttk


class WeatherStationGUI(ttk.Frame):

    def __init__(self, master, buienradar_feed):
        super()\
            .__init__(master)
        self.selected_location = 'Groningen'
        self.master = master
        self.buienradar_feed = buienradar_feed

        # creating the widget for the screen
        """example:
            self.max_temp_str = ('Hoogste temperatuur:\n' + self.extreme_weather.max_temperature[0] + ' ' +
                        str(self.extreme_weather.max_temperature[1]) + ' °C\n')
        """

        # fixing the layout for the widget
        """example:
            self.max_temp_label = ttk.Label(self.left_frame, text=self.max_temp_str)
            self.max_temp_label.grid(column=1, row=2, sticky='W')
        """
        locatie_test = ttk.Label(self.master, text=self.selected_location)
        locatie_test.grid(column=1, row=1, sticky='S')

        for meetstation in buienradar_feed['actual']['stationmeasurements']:
            if meetstation['regio'] == self.selected_location:
                print(meetstation)


def request_weatherdata():
    """Requests buienradar data and returns it as a dictionary"""
    response = requests.get("https://api.buienradar.nl/data/public/2.0/jsonfeed")
    return json.loads(response.text)


def main():
    """this contains the data for the program"""
    buienradar_feed = request_weatherdata()

    # generating a list of meetstations to display for selection in the interface
    # run once on starting the program
    meetstation_locations = []
    for meetstation in buienradar_feed['actual']['stationmeasurements']:
        if meetstation['regio'] == 'Noordzee':
            pass
        else:
            meetstation_locations.append(meetstation['regio'])

    root = Tk()
    root.title('Weatherstations Netherlands')
    app = WeatherStationGUI(root, buienradar_feed)

    """this contains the selected location"""
    print(app.selected_location)
    app.mainloop()


if __name__ == "__main__":
    main()
