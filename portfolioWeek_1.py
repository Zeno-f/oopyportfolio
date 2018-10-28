# -*- coding: utf-8 -*-
"""
Main file voor de Portfolio voor OOP met python voor Jaar 2 Electrotechniek

Contains the following assignments:
    Calculate your age
    How many days till a certain date
    
Program lacks the following things (also a todo list):
    Providing guidelines for how you have to format your input
    Methods to deal with wrong user input
        A or a
        don't need year for option B
    
Discussion:
    What is the right place to deal with user input. The function 
    userInput.inputToDate deals with userInput. 

Created on Wed Sep 12 13:23:19 2018

@author: Zeno
"""

#   import
from datetime import date
from calendar import monthrange

#   classes
class userInput():
    def askInput():
        menu = ["Welcome",
        "\tPress A if you want to know your age",
        "\tPress B to see how many nights left till a certain date"]
        for s in menu:
            print(s)
        return input("> ")
        
    def inputToDate(userDate):
        userDate = userDate.split('/')[::-1]
        userDate = list(map(int, userDate))
        
        return date(*userDate)
    
class yourAge():
    def calculateAge(born):
        today = date.today()
        #   age in years
        ageYear = today.year - born.year - ((today.month, today.day) < ( born.month, born.day))
        #   age in months
        ageMonth = today.month - born.month - (today.day < born.day)
        if (born.month > today.month):
            ageMonth += 12
        #   age in days
        ageDay = today.day - born.day
        if (born.day > today.day):
            if (born.month == 1):
                ageDay += monthrange(born.year, born.month + 11)[1]
            else:
                ageDay += monthrange(born.year, born.month - 1)[1]

        return ageYear, ageMonth, ageDay

class daysToEvent():
    def howManyDaysLeft(event):
        today = date.today()
        daysTillEvent = event.toordinal() - today.toordinal()
        return daysTillEvent
    
#   main
def main():
    userPick = userInput.askInput()
    
    if userPick.upper() == 'A':
        userDate = input("Please enter your date of birth: ")
        userDate = (yourAge.calculateAge(userInput.inputToDate(userDate)))
        if userDate[1] == 0:
            print("You are", userDate[0], "years and", userDate[2], "days old")
        else:
            print("You are", userDate[0], "years and", userDate[1], "months and", userDate[2], "days old")

    elif userPick.upper() == 'B':
        userDate = input("Please enter the date of the event you are looking forward too: ")
        userDate = (daysToEvent.howManyDaysLeft(userInput.inputToDate(userDate)))
        if userDate == 0:
            print("The event is today! Enjoy yourself")
        elif userDate > 0:
            print("You still have to sleep", userDate, "nights before the event")
        elif userDate < 0:
            print("The event has already happened,", userDate * -1, "days in the past, awww")
        else:
            pass
    
    else:
        input("Please make a valid choice")

if __name__ == "__main__":
    main()