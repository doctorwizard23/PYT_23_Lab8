# Andrew Stiers 8/17/2023

import os
import pygubu

import tkinter as tk
import tkinter.messagebox as mb

PROJECT_PATH = os.path.dirname(__file__)
PROJECT_UI = os.path.join(PROJECT_PATH, "InchesToFeet.ui")


class InchesToFeet:

    def __init__(self, master):

        # Boilerplate to build the tkinter interface based on grams_to_ounces.ui
        self.__builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.__mainwindow = builder.get_object('top_frame', master)
        builder.connect_callbacks(self)

        # Save these two UI elements as properties so that we can access them when
        # the user clicks on the calculate button.
        self.__inch_entry = builder.get_object('inch_entry', master)
        self.__feet_entry_variable = builder.get_variable('feet_entry_variable')

    def calculate(self):
        # Convert inches to feet. If there's an error, display an error message.
        try:
            inch = float(self.__inch_entry.get())
            feet = inch / 12
            self.__feet_entry_variable.set("{:.1f} Feet".format(feet))
        except ValueError:
            mb.showerror(title="Error Calculating Inches!", message="Feet must be a decimal number. Please try again.")

    def get_top_frame(self):
        # Return the top frame for the app so that it can be displayed in a tabbed notebook.
        return self.__mainwindow

    def run(self):
        self.__mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = InchesToFeet(root)
    app.run()