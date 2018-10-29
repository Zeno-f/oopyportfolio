"""modules that are needed for tkinter"""
from tkinter import *
from tkinter import ttk
from weatherstation import *


class WeatherStationGUI(ttk.Frame):
    """"This contains the code to draw the GUI. Its sorted in the following way:

    - Style's
        For now for debugging
    - Frames
        A left and a right one
    - Left frame widget
    - Left frame layout
    - Right frame widget
    - Right frame layout
    - Notebook in Right frame
        For every page in the notebook:
        - Widget creation
        - Page layout
    """

    def __init__(self, master):
        super().__init__(master)
        data = WeatherStation()

        """for debugging. Adding backgrounds to different objects to recognize the space they take"""
        self.s = ttk.Style()
        self.s.configure('red.TFrame', background='red')
        self.s.configure('yellow.TFrame', background='yellow')

        # creating 2 frames
        self.master = master
        self.left_frame = ttk.Frame(master, padding='3 3 12 12')    # left, top, right, bottom
        self.right_frame = ttk.Frame(master, padding='3 3 12 12')    # left, top, right, bottom

        self.left_frame.grid(column=1, row=1)
        self.right_frame.grid(column=2, row=1, sticky=(N, W))

        # widgets for the left frame
        self.location_selection = StringVar()
        self.location_selection.set('Locatie')
        self.location_selection.trace('w', self.change_dropdown)
        self.extreme_weather = data.MaximumValues()
        # self.max_temp_str = ('\nHoogste temperatuur:\n' + self.extreme_weather.max_temperature[0] + ' ' +
        #                 str(self.extreme_weather.max_temperature[1]) + ' °C')
        # self.min_temp_str = ('Laagste temperatuur:\n' + self.extreme_weather.min_temperature[0] + ' ' +
        #                 str(self.extreme_weather.min_temperature[1]) + ' °C')
        # self.sunpower_str = ('Meest Zonnige locatie:\n' + self.extreme_weather.max_sun[0] + ' ' +
        #                 str(self.extreme_weather.max_sun[1]) + ' W/m2')
        # self.max_wind_str = ('Het waait het hardst in:\n' + self.extreme_weather.max_windy[0] + ' ' +
        #                 str(self.extreme_weather.max_windy[1]) + ' Bft')
        # self.min_wind_str = ('Het waait het minst in:\n' + self.extreme_weather.min_windy[0] + ' ' +
        #                 str(self.extreme_weather.min_windy[1]) + ' Bft')

        # layout for the left frame
        self.popup_menu = OptionMenu(self.left_frame, self.location_selection, *meetstation_locations)
        self.popup_menu.grid(row=1, column=1, sticky=(W, E))
        # self.max_temp_label = ttk.Label(self.left_frame, text=self.max_temp_str)
        # self.max_temp_label.grid(column=1, row=3, sticky='W')
        # self.min_temp_label = ttk.Label(self.left_frame, text=self.min_temp_str)
        # self.min_temp_label.grid(column=1, row=4, sticky='W')
        # self.sunpower_label = ttk.Label(self.left_frame, text=self.sunpower_str)
        # self.sunpower_label.grid(column=1, row=5, sticky='W')
        # self.max_wind_label = ttk.Label(self.left_frame, text=self.max_wind_str)
        # self.max_wind_label.grid(column=1, row=6, sticky='W')
        # self.min_wind = ttk.Label(self.left_frame, text=self.min_wind_str)
        # self.min_wind.grid(column=1, row=7, sticky='W')

        self.display_min_max()

        # widgets for the right frame
        self.weather_pages = ttk.Notebook(self.right_frame)
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

    def display_min_max(self):
        self.extreme_weather = MaximumValues()
        self.max_temp_str = ('\nHoogste temperatuur:\n' + self.extreme_weather.max_temperature[0] + ' ' +
                        str(self.extreme_weather.max_temperature[1]) + ' °C')
        self.min_temp_str = ('Laagste temperatuur:\n' + self.extreme_weather.min_temperature[0] + ' ' +
                        str(self.extreme_weather.min_temperature[1]) + ' °C')
        self.sunpower_str = ('Meest zonnige locatie:\n' + self.extreme_weather.max_sun[0] + ' ' +
                        str(self.extreme_weather.max_sun[1]) + ' W/m2')
        self.max_wind_str = ('Het waait het hardst in:\n' + self.extreme_weather.max_windy[0] + ' ' +
                        str(self.extreme_weather.max_windy[1]) + ' Bft')
        self.min_wind_str = ('Het waait het minst in:\n' + self.extreme_weather.min_windy[0] + ' ' +
                        str(self.extreme_weather.min_windy[1]) + ' Bft')

        self.max_temp_label = ttk.Label(self.left_frame, text=self.max_temp_str)
        self.max_temp_label.grid(column=1, row=3, sticky='W')
        self.min_temp_label = ttk.Label(self.left_frame, text=self.min_temp_str)
        self.min_temp_label.grid(column=1, row=4, sticky='W')
        self.sunpower_label = ttk.Label(self.left_frame, text=self.sunpower_str)
        self.sunpower_label.grid(column=1, row=5, sticky='W')
        self.max_wind_label = ttk.Label(self.left_frame, text=self.max_wind_str)
        self.max_wind_label.grid(column=1, row=6, sticky='W')
        self.min_wind = ttk.Label(self.left_frame, text=self.min_wind_str)
        self.min_wind.grid(column=1, row=7, sticky='W')
        print('done update')
        self.after(10000, self.display_min_max)

    def change_dropdown(self, *args):
        self.selected_location = self.location_selection.get()
        # update open tab
        print(self.selected_location)



def main():
    root = Tk()
    root.title('Weatherstations Netherlands')
    app = WeatherStationGUI(root, data)
    app.mainloop()


if __name__ == "__main__":
    main()
