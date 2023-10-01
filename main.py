# ******************************************************************************
# Author:           Noah McGarry, Andrew Stiers
# Lab:              Lab 8
# Date:             8/17/2023
# Description:      Lab 8 Program
#
# Input:            Celsius float to be converted to fahrenheit
#                   Fahrenheit float to be converted to celsius
#                   Inches float to be converted to Feet
#                   Feet float to be converted to Inches
#
# Output:           Fahrenheit float converted from celsius
#                   Celsius float converted from fahrenheit
#                   Inches float converted from feet
#                   Feet float converted from inches
#                   GUI outputs the calculators
#
# Sources:          Lab 8 specifications
#
#
# Comments:         We hope you like our calculators!
#
#
#
#
#
# ******************************************************************************


#!/usr/bin/env python3

import tkinter as tk
import tkinter.ttk as ttk

from AboutApp import AboutApp
from FahrenheitCelsius import FahrenheitCelsius
from CelsiusFahrenheit import CelsiusFahrenheit
from FeetToInches import FeetToInch
from InchesToFeet import InchesToFeet

# Main Window for the team calculator project.
# To add a new tab, create an App object with a get_top_frame method.
# Then, add the app to the __main_notebook, along with a name for the tab.


class MainApp:
    def __init__(self, master):
        # This is needed to allow the notebook tabs to stretch.
        tk.Grid.columnconfigure(master, 0, weight=1)
        tk.Grid.rowconfigure(master, 0, weight=1)

        # build ui
        self.__main_notebook = ttk.Notebook(master)
        self.__main_notebook.grid(column='0', row='0', sticky='nsew')
        self.__main_notebook.rowconfigure('0', weight='1')
        self.__main_notebook.columnconfigure('0', weight='1')

        # Main widget
        self.__mainwindow = self.__main_notebook

        # Add About... tab
        about_app = AboutApp(self.__mainwindow)
        self.__main_notebook.add(about_app.get_top_frame(), text="About...")

        # Add first calculator
        fahr_to_cels = FahrenheitCelsius(self.__mainwindow)
        self.__main_notebook.add(fahr_to_cels.get_top_frame(), text="Fahrenheit to Celsius")

        # Add second calculator
        cels_to_fahr = CelsiusFahrenheit(self.__mainwindow)
        self.__main_notebook.add(cels_to_fahr.get_top_frame(), text="Celsius to Fahrenheit")

        # Add third calculator
        feetToInches = FeetToInch(self.__mainwindow)
        self.__main_notebook.add(feetToInches.get_top_frame(), text="Feet to Inches")

        # Add fourth calculator
        inchesToFeet = InchesToFeet(self.__mainwindow)
        self.__main_notebook.add(inchesToFeet.get_top_frame(), text="Inches to Feet")
      
    def run(self):
        self.__mainwindow.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    root.title("The World's Greatest Calculator")
    app = MainApp(root)
    app.run()