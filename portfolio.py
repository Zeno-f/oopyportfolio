# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 21:06:11 2018

@author: Zeno
"""
import temperature_conversion
import living_space
import task_list


#   classes
class user_input(object):
    def ask_input():
        menu = ["\nWelcome",
        "\tPress A if you want to know your age",
        "\tPress B to see how many nights left till a certain date",
        "\tPress C to convert a temperature",
        "\tPress D to calculate the living area or space in a room",
        "\tPress E to see your activity list",
        "\t",
        "\tPress X to exit the program"]
        for s in menu:
            print(s)
        return input("> ")


#   main
def main():
    
    loop = 1
    
    while loop == 1:
        user_pick = user_input.ask_input()
        if user_pick == 'A' or user_pick == 'a':
            print("Not merged with this program yet. Please run portfolioWeek_1 for this functionality")
        
        elif user_pick == 'B' or user_pick == 'b':
            print("Not merged with this program yet. Please run portfolioWeek_1 for this functionality")
        
        #   users wants to convert a temperature, in the file temperature_conversion
        #   is the code that handles the input, calculations and output for this
        elif user_pick == 'C' or user_pick == 'c':
            x = temperature_conversion.temperature_interface
            temperature_conversion.temperature_interface.handle_user(x)
            
        elif user_pick == 'D' or user_pick == 'd':
            x = living_space.living_space_interface
            living_space.living_space_interface.handle_user(x)
        
        elif user_pick == 'E' or user_pick == 'e':
            input_date = task_list.ask_input()
            convert_date = task_list.convert_input(input_date)
            task_list.add_new_activity(convert_date)
            input("\nPress any button to continue\n")
        
        elif user_pick == 'X' or user_pick == 'x':
            print("Goodbye......")
            loop = 0
        
        else:
            print("Please make a valid choice > ")


if __name__ == "__main__":
    main()
