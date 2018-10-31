import tkinter as tk
from tkinter import Button


class NumberButton(Button):
    def __init__(self, window, text, command=None, grid_placement=None, **kw):
        # call to Button super class init
        super().__init__(window, text=text, **kw)

        # setting command
        if command is not None:
            self.config(command=command)

        # giving grid placement (if provided)
        if grid_placement is not None:
            self.grid(row=grid_placement[0], column=grid_placement[1], sticky=tk.EW)

        # colour configurations
        self.config(background='#99A62B', foreground='#F2FF80')

        # other config
        self.config(bd=1, height=2, width=4)


class OperatorButton(Button):
    def __init__(self, window, text, command=None, grid_placement=None, **kw):
        # call to Button super class init
        super().__init__(window, text=text, **kw)

        # setting command
        if command is not None:
            self.config(command=command)

        # giving grid placement (if provided)
        if grid_placement is not None:
            self.grid(row=grid_placement[0], column=grid_placement[1], sticky=tk.EW)

        # colour configurations
        self.config(background='#5E661B', foreground='#F2FF80')

        # other config
        self.config(bd=1, height=2, width=4)


class SpecialButton(Button):
    def __init__(self, window, text, command=None, grid_placement=None, **kw):
        # call to Button super class init
        super().__init__(window, text=text, **kw)

        # setting command
        if command is not None:
            self.config(command=command)

        # giving grid placement (if provided)
        if grid_placement is not None:
            self.grid(row=grid_placement[0], column=grid_placement[1], sticky=tk.EW)

        # colour configurations
        self.config(background='#163317', foreground='#F2FF80')

        # other config
        self.config(bd=1, height=2, width=4)
