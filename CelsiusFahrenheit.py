# Noah McGarry 8/17/2023
import os
import pygubu

import tkinter as tk
import tkinter.messagebox as mb

PROJECT_PATH = os.path.dirname(__file__)
PROJECT_UI = os.path.join(PROJECT_PATH, "CelsiusFahrenheit.ui")


class CelsiusFahrenheit:
    # This creates a class to create a calculator to calculate Celsius into Fahrenheit
    def __init__(self, master):
        """

        :param master:
        """
        self.__builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.__mainwindow = builder.get_object('top_frame', master)
        builder.connect_callbacks(self)

        self.__cels_entry = builder.get_object('cels_entry', master)
        self.__fahr_entry_variable = builder.get_variable('fahr_entry_variable')

    def calculate(self):
        """
        Converts celsius to fahrenheit
        :return: fahr, float, converted from celsius
        """
        try:
            cels = float(self.__cels_entry.get())
            fahr = cels * (9/5) + 32
            self.__fahr_entry_variable.set("{:.2f} Fahrenheit".format(fahr))
        except ValueError:
            mb.showerror(title="Error Calculating Fahrenheit!", message="Celsius must be a float or integer. Please try again.")

    def get_top_frame(self):
        return self.__mainwindow

    def run(self):
        self.__mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = CelsiusFahrenheit(root)
    app.run()