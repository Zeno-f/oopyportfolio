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

        # creating 2 frames
        self.master = master
        self.left_frame = ttk.Frame(master, padding='5 5 5 5', borderwidth=2)    # left, top, right, bottom
        self.right_frame = ttk.Frame(master, padding='5 5 5 5')    # left, top, right, bottom

        self.left_frame.grid(column=1, row=1)
        self.right_frame.grid(column=2, row=1, sticky=(N, W))

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

        self.max_temperature1 = ['Vlieland', 7.2]
        self.min_temperature1 = ['Goes', 4.4]
        self.max_sun1 = ['Terschelling', 530]
        self.max_wind1 = ['Terschelling', 6]
        self.min_wind1 = ['Maastricht', 2]

        self.max_temp_location = StringVar()
        self.min_temp_location = StringVar()
        self.sunpower_location = StringVar()
        self.max_wind_location = StringVar()
        self.min_wind_location = StringVar()

        self.max_temp = StringVar()
        self.min_temp = StringVar()
        self.sunpower = StringVar()
        self.max_wind = StringVar()
        self.min_wind = StringVar()

        self.max_temp_location.set(self.max_temperature1[0])
        self.min_temp_location.set(self.min_temperature1[0])
        self.sunpower_location.set(self.max_sun1[0])
        self.max_wind_location.set(self.max_wind1[0])
        self.min_wind_location.set(self.min_wind1[0])

        self.max_temp.set(str(self.max_temperature1[1]) + '°C')
        self.min_temp.set(str(self.min_temperature1[1]) + '°C')
        self.sunpower.set(str(self.max_sun1[1]) + 'W/m²')
        self.max_wind.set(str(self.max_wind1[1]) + 'Bft')
        self.min_wind.set(str(self.min_wind1[1]) + 'Bft')

        self.max_temp_text = ttk.Label(self.left_frame, text='Highest temperature', padding='2 2 2 0')
        self.max_temp_text_w = ttk.Label(self.left_frame, textvariable=self.max_temp_location)
        self.max_temp_text_o = ttk.Label(self.left_frame, textvariable=self.max_temp)

        self.min_temp_text = ttk.Label(self.left_frame, text='Lowest temperature', padding='2 2 2 0')
        self.min_temp_text_w = ttk.Label(self.left_frame, textvariable=self.min_temp_location)
        self.min_temp_text_o = ttk.Label(self.left_frame, textvariable=self.min_temp)

        self.sunpower_text = ttk.Label(self.left_frame, text='Most sunshine', padding='2 2 2 0')
        self.sunpower_text_w = ttk.Label(self.left_frame, textvariable=self.sunpower_location)
        self.sunpower_text_o = ttk.Label(self.left_frame, textvariable=self.sunpower)

        self.max_wind_text = ttk.Label(self.left_frame, text='Most windy', padding='2 2 2 0')
        self.max_wind_text_w = ttk.Label(self.left_frame, textvariable=self.max_wind_location)
        self.max_wind_text_o = ttk.Label(self.left_frame, textvariable=self.max_wind)

        self.min_wind_text = ttk.Label(self.left_frame, text='Least windy', padding='2 2 2 0')
        self.min_wind_text_w = ttk.Label(self.left_frame, textvariable=self.min_wind_location)
        self.min_wind_text_o = ttk.Label(self.left_frame, textvariable=self.min_wind)

        self.max_temp_text.grid(column=0, row=3, columnspan=2, sticky='S')
        self.max_temp_text_w.grid(column=0, row=4, sticky='W')
        self.max_temp_text_o.grid(column=1, row=4, sticky='E')

        self.min_temp_text.grid(column=0, row=5, columnspan=2, sticky='S')
        self.min_temp_text_w.grid(column=0, row=6, sticky='W')
        self.min_temp_text_o.grid(column=1, row=6, sticky='E')

        self.sunpower_text.grid(column=0, row=7, columnspan=2, sticky='S')
        self.sunpower_text_w.grid(column=0, row=8, sticky='W')
        self.sunpower_text_o.grid(column=1, row=8, sticky='E')

        self.max_wind_text.grid(column=0, row=9, columnspan=2, sticky='S')
        self.max_wind_text_w.grid(column=0, row=10, sticky='W')
        self.max_wind_text_o.grid(column=1, row=10, sticky='E')

        self.min_wind_text.grid(column=0, row=11, columnspan=2, sticky='S')
        self.min_wind_text_w.grid(column=0, row=12, sticky='W')
        self.min_wind_text_o.grid(column=1, row=12, sticky='E')


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
