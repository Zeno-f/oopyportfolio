# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 12:34:51 2018

@author: Zeno
"""

class floor:
    """ Calculates the surface area
    
    args:
        length:
        width:
            
    returns:
        a value for the surface area + m2
    """
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = self.__living_area(length, width)
        
    def __living_area(self, length, width):
        return length * width
    
    def __str__(self):
        return str(self.area) + " m2"
        
class room(floor):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
        self.space = self.__living_space(length, width, height)
        
    def __living_space(self, length, width, height):
        return length * width * height
    
    def __str__(self):
        return str(self.space) + " m3"
    
class living_space_interface:
    def ask_input_1():
        menu = ["What are the measurements of the room?",
                "\tEnter in order the lenght and width of the room to calculate its area",
                "\tInclude its height at the end to calculate its space"]
        for s in menu:
            print(s)
        return input("> ")
    
    def process_input(self, user_input):
        user_input = user_input.split(' ')
        return list(map(int, user_input))
        
    def handle_user(self):
        user_input = self.ask_input_1()
        user_input = self.process_input(self, user_input)
        
        if len(user_input) == 2:
            room_1 = floor(*user_input)
            print("The room has a living area of ", room_1)
        elif len(user_input) == 3:
            room_1 = room(*user_input)
            print("The room has a living area of ", room_1.area, "m2")
            print("and a living space of ", room_1)
            return

if __name__ == "__main__":
    print('\nTo run this program, run portfolio.py and select the correct program')
