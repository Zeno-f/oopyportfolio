# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 13:47:16 2018

@author: Zeno

The plan is:
    read the list
    add the item
    sort the list
    write the list 
    
i deserve a cookie!

ps: mijn 'task list' data format is 00:00, 00-00-0000, dit is de beschrijving
    
check how fucking slow this is xD
"""
import time
import datetime
import os


def ask_input():
    
    print("Here is your activity list:\n")
    
    file_read = open("files/task list.txt", "r")
    if file_read.mode == "r":
        task_list = file_read.read()
        print(task_list)
        file_read.close()
        
    add_input = input("Press A to add a activity > ")
    if add_input == 'A' or add_input == 'a':
        print("\nEnter the time, date and a discription")
        new_time = input("Enter the time as hh:mm > ")
        new_day = input("Enter the date as dd-mm-yyyy > ")
        new_desc = input("Enter a discription of the activity > ")
        return new_time, new_day, new_desc
    else:
        return


def convert_input(input_date):
    new_line_str = input_date[0] + ',' + input_date[1] + ',' + input_date[2] + '\n'

    new_time = list(map(int, input_date[0].split(':')))
    new_day = list(map(int, input_date[1].split('-')[::-1]))
    new_date = datetime.datetime(*new_day, *new_time)
    
    return new_date, new_line_str


def add_new_activity(convert_date):
    file_read = open("files/task list.txt", "r")
    file_write = open("files/temp.txt", "w+")
    
    if file_read.mode == "r":
        
        old_line = ['time', 'date', 'describtion']
        enter_new = False
        
        while True:  
            
            old_line_str = file_read.readline()
            old_line = old_line_str.split(',')

            if len(old_line) != 3:
                break
                """
                when the lenght of the list that contains the result from readline
                is not equel to 3 we have reached the end of the file and we need
                to break out of this loop
                """
            
            old_date = time.strptime(old_line[0] + ' ' + old_line[1], "%H:%M %d-%m-%Y")
            old_date = datetime.datetime(*old_date[:6])
            difference_date = old_date - convert_date[0]
            
            if difference_date.days < 0:
                file_write.write(old_line_str)
    
            elif difference_date.days > 0:
                if enter_new == False:
                    enter_new = True
                    file_write.write(convert_date[1])
                    # convert_date[1] = contains user input for new activity
                else:
                    pass
                file_write.write(old_line_str)
    
        file_read.close()
        file_write.close()
        
        os.remove("files/task list.txt")
        os.rename("files/temp.txt", "files/task list.txt")
        
        file_review = open("files/task list.txt", "r")
        if file_review.mode == "r":
            task_list = file_review.read()
            print("\nHere is your updated task list:\n")
            print(task_list)
    
    return 


if __name__ == "__main__":
    print('\nTo run this program, run portfolio.py and select the correct program')