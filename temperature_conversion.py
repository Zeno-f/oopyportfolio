# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 20:21:43 2018

Week 2 opdracht temperatuur conversion

@author: Zeno
"""

class temperature:
    
    celsius_absolute_zero = 273.15
    farenheit_absolute_zero = 459.67
    farenheit_ice_melting_point = 32
    
    kelvin = 0.0
    celsius = 0.0
    farenheit = 0.0
  
    def __init__(self, value, scale):
        self.value = value
        self.scale = scale
        self.__update_temperature(value, scale)
    
    def __update_temperature(self, value, scale):
        if scale == 'K' or scale == 'k':
            self.kelvin = value
            self.celsius = value - temperature.celsius_absolute_zero
            self.farenheit = value * (9/5) - temperature.farenheit_absolute_zero
        elif scale == 'C' or scale == 'c':
            self.celsius = value
            self.kelvin = value + temperature.celsius_absolute_zero
            self.farenheit = value * (9/5) + temperature.farenheit_ice_melting_point 
        elif scale == 'F' or scale == 'f':
            self.farenheit = value
            self.kelvin = (value + temperature.farenheit_absolute_zero) * (5/9)
            self.celsius = (value - temperature.farenheit_ice_melting_point) * (5/9)
        else:
            pass
        
class temperature_interface:
    #   1) user gets to input a temperature and a unit
    def ask_input_1():
        menu = ["What is the temperature you want to convert?",
                "\tEnter the value and unit, for example: 300 K"]
        for s in menu:
            print(s)
        return input("> ")
    
    #   4) user gets to input what unit he wants to know the temperature
    def ask_input_2():
        menu = ["To what temperature scale do you want to convert to?",
                "\tEnter the unit, for example: F"]
        for s in menu:
            print(s)
        return input("> ")
    
    #   2) processes the input, from a string to a value in int and a scale
    def process_input(self, user_input):
        user_input = user_input.split(' ')
        self.value = int(user_input[0])
        self.scale = user_input[1]   
    
    #   function that handles everything
    def handle_user(self):
        user_input = self.ask_input_1()
        self.process_input(self, user_input)
        
        #   3) user input is used to create a temperature object, object
        #      contains temperature in different units, this can be used
        #      to output any temperature
        temp = temperature(self.value, self.scale)
        user_choice = self.ask_input_2()
        if user_choice == 'K' or user_choice == 'k':
            print(temp.kelvin, "K")
        elif user_choice == 'C' or user_choice == 'c':
            print(temp.celsius, "C")
        elif user_choice == 'F' or user_choice == 'f':
            print(temp.farenheit, "F")

if __name__ == "__main__":
    print('\nTo run this program, run portfolio.py and select the correct program')
