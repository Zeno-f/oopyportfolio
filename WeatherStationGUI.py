from tkinter import *
from tkinter import ttk
from weatherstation import *


class WeatherStationGUI(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.selected_location = 'Groningen'

        # creating 2 frames
        self.master = master
        self.left_frame = WeatherStationLeft()
        self.right_frame = WeatherStationRight()

        self.left_frame.grid(column=1, row=1, sticky=E)
        self.right_frame.grid(column=2, row=1, sticky=(N, W))

        self.__update_data__()

    def __update_data__(self):
        data.update_weather_data()
        data.update_extremes()
        self.after(10000, self.__update_data__)


class WeatherStationWeerbeeld(ttk.Frame):
    def __init__(self):
        super().__init__()

        for meetstation in data.feed['actual']['stationmeasurements']:
            if meetstation['regio'] == self.selected_location:
                variable0 = str(meetstation['stationname']) + ", Netherlands"
                variable1 = str(meetstation['rainFallLast24Hour']) + " mm in the last 24 hours"
                variable2 = str(meetstation['sunpower']) + " W/m^2"
                variable3 = str(meetstation['airpressure']) + " hPa"
                variable4 = str(meetstation['winddirectiondegrees']) + "°"
                variable5 = str(meetstation['windspeedBft']) + " Bft"
                variable6 = str(meetstation['windgusts']) + " km/h"
                variable7 = str(meetstation['temperature']) + " °C"
                variablex = str(meetstation['timestamp'])

        # lay-out for a two by y grid for the data
        ttk.Label(self, text="Stationname").grid(column=1, row=1, sticky=W)
        ttk.Label(self, text=variable0).grid(column=2, row=1, sticky=E)
        ttk.Label(self, text="Rainfall").grid(column=1, row=2, sticky=W)
        ttk.Label(self, text=variable1).grid(column=2, row=2, sticky=E)
        ttk.Label(self, text="Sun power").grid(column=1, row=3, sticky=W)
        ttk.Label(self, text=variable2).grid(column=2, row=3, sticky=E)
        ttk.Label(self, text="Air pressure").grid(column=1, row=4, sticky=W)
        ttk.Label(self, text=variable3).grid(column=2, row=4, sticky=E)
        ttk.Label(self, text="Wind-direction").grid(column=1, row=5, sticky=W)
        ttk.Label(self, text=variable4).grid(column=2, row=5, sticky=E)
        ttk.Label(self, text="Wind power").grid(column=1, row=6, sticky=W)
        ttk.Label(self, text=variable5).grid(column=2, row=6, sticky=E)
        ttk.Label(self, text="Wind gusts").grid(column=1, row=7, sticky=W)
        ttk.Label(self, text=variable6).grid(column=2, row=7, sticky=E)
        ttk.Label(self, text="Temperature").grid(column=1, row=8, sticky=W)
        ttk.Label(self, text=variable7).grid(column=2, row=8, sticky=E)


class WeatherStationRight(ttk.Frame):
    def __init__(self):
        super().__init__()

        # widgets for the right frame
        self.weather_pages = ttk.Notebook(self)
        self.selected_location = 'Groningen'

        self.tab1 = ttk.Frame(self.weather_pages)
        self.tab2 = ttk.Frame(self.weather_pages)
        self.tab3 = ttk.Frame(self.weather_pages)
        self.tab4 = ttk.Frame(self.weather_pages)
        self.tab5 = ttk.Frame(self.weather_pages)
        self.tab6 = ttk.Frame(self.weather_pages)

        # layout for the right frame
        self.weather_pages.grid(row=1, column=1, sticky=(W, N, E, S))

        self.weather_pages.add(self.tab1, text='Weerbeeld', compound='top')
        self.weather_pages.add(self.tab2, text='tab two', compound='top')
        self.weather_pages.add(self.tab3, text='tab three', compound='top')
        self.weather_pages.add(self.tab4, text='tab three', compound='top')
        self.weather_pages.add(self.tab5, text='tab three', compound='top')
        self.weather_pages.add(self.tab6, text='tab three', compound='top')


class WeatherStationLeft(ttk.Frame):
    def __init__(self):
        super().__init__()

        # StringVars to update labels
        self.location_selection = StringVar()

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

        # Set a value to the StringVars
        self.location_selection.set('Locatie')
        self.location_selection.trace('w', self.change_dropdown)

        self.max_temp_location.set(data.max_temperature[0])
        self.min_temp_location.set(data.min_temperature[0])
        self.sunpower_location.set(data.max_sun[0])
        self.max_wind_location.set(data.max_wind[0])
        self.min_wind_location.set(data.min_wind[0])

        self.max_temp.set(str(data.max_temperature[1]) + '°C')
        self.min_temp.set(str(data.min_temperature[1]) + '°C')
        self.sunpower.set(str(data.max_sun[1]) + 'W/m²')
        self.max_wind.set(str(data.max_wind[1]) + 'Bft')
        self.min_wind.set(str(data.min_wind[1]) + 'Bft')

        # Creating widgets
        self.popup_menu = OptionMenu(self, self.location_selection, *data.meetstation_locations)

        self.max_temp_text = ttk.Label(self, text='Highest temperature', padding='2 2 2 0')
        self.max_temp_text_w = ttk.Label(self, textvariable=self.max_temp_location)
        self.max_temp_text_o = ttk.Label(self, textvariable=self.max_temp)

        self.min_temp_text = ttk.Label(self, text='Lowest temperature', padding='2 2 2 0')
        self.min_temp_text_w = ttk.Label(self, textvariable=self.min_temp_location)
        self.min_temp_text_o = ttk.Label(self, textvariable=self.min_temp)

        self.sunpower_text = ttk.Label(self, text='Most sunshine', padding='2 2 2 0')
        self.sunpower_text_w = ttk.Label(self, textvariable=self.sunpower_location)
        self.sunpower_text_o = ttk.Label(self, textvariable=self.sunpower)

        self.max_wind_text = ttk.Label(self, text='Most windy', padding='2 2 2 0')
        self.max_wind_text_w = ttk.Label(self, textvariable=self.max_wind_location)
        self.max_wind_text_o = ttk.Label(self, textvariable=self.max_wind)

        self.min_wind_text = ttk.Label(self, text='Least windy', padding='2 2 2 0')
        self.min_wind_text_w = ttk.Label(self, textvariable=self.min_wind_location)
        self.min_wind_text_o = ttk.Label(self, textvariable=self.min_wind)

        # Placing the widgets in the layout
        self.popup_menu.grid(column=0, row=1, columnspan=2, sticky=(W, E))

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

    def update_max_min(self):
        self.max_temp_location.set(data.max_temperature[0])
        self.min_temp_location.set(data.min_temperature[0])
        self.sunpower_location.set(data.max_sun[0])
        self.max_wind_location.set(data.max_wind[0])
        self.min_wind_location.set(data.min_wind[0])

        self.max_temp.set(str(data.max_temperature[1]) + '°C')
        self.min_temp.set(str(data.min_temperature[1]) + '°C')
        self.sunpower.set(str(data.max_sun[1]) + 'W/m²')
        self.max_wind.set(str(data.max_wind[1]) + 'Bft')
        self.min_wind.set(str(data.min_wind[1]) + 'Bft')

        self.after(10000, self.update_max_min())

    def change_dropdown(self, *args):
        self.selected_location = self.location_selection.get()
        # update open tab
        print(self.selected_location)


# provides global access to the buienradar data
data = WeatherStation()


def main():
    root = Tk()
    root.title('Weatherstation Netherlands')
    app = WeatherStationGUI(root)
    app.mainloop()


if __name__ == "__main__":
    main()
