# Noah McGarry 8/17/2023
import os
import pygubu

import tkinter as tk
import tkinter.messagebox as mb

PROJECT_PATH = os.path.dirname(__file__)
PROJECT_UI = os.path.join(PROJECT_PATH, "FahrenheitCelsius.ui")


class FahrenheitCelsius:
    # This creates a class to build a calculator to calculate Fahrenheit into Celsius
    def __init__(self, master):
        self.__builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.__mainwindow = builder.get_object('top_frame', master)
        builder.connect_callbacks(self)

        self.__fahr_entry = builder.get_object('fahr_entry', master)
        self.__cels_entry_variable = builder.get_variable('cels_entry_variable')

    def calculate(self):
        # Convert fahrenheit to celsius
        try:
            fahr = float(self.__fahr_entry.get())
            cels = (fahr - 32)/1.8
            self.__cels_entry_variable.set("{:.2f} Celsius".format(cels))
        except ValueError:
            mb.showerror(title="Error Calculating Celsius!", message="Fahrenheit must be a float or integer. Please try again.")

    def get_top_frame(self):
        return self.__mainwindow

    def run(self):
        self.__mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = FahrenheitCelsius(root)
    app.run()