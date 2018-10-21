import tkinter as tk
from tkinter import ttk
import functools

win = tk.Tk()
win.resizable(False, False)
win.title("Simple Calculator")

# Expression Label Frame
# TODO remove the line created by label frame
input_frame = ttk.LabelFrame(win, text='')
input_frame.grid(row=0, column=0, columnspan=2)

# TODO find a way to increase height of textbox
expression_str = tk.StringVar(value='3+4')
expression_box = ttk.Entry(input_frame, width=50, textvariable=expression_str, state='readonly')
expression_box.grid(row=0, column=0)

# Numbers Label Frame
numbers_frame = ttk.LabelFrame(win, text='')
numbers_frame.grid(row=1, column=0)


# create the numbers buttons
def _on_press_number(number):
    """
    :param number: the button that has been pressed
    :return:
    """
    # TODO requires the logic for button press
    s = expression_str.get()
    s += str(number)
    expression_str.set(s)


def _on_press_backspace():
    '''
    implements functionality for pressing backspace
    :return:
    '''
    s = expression_str.get()
    if len(s) > 0:
        s = s[:-1]
    expression_str.set(s)
    if s == '':
        expression_str.set('0')


def _on_press_decimal():
    pass


num_buttons_dict = {}

for i in range(3):
    for j in range(3):
        button_val = (2 - i) * 3 + j + 1
        button = tk.Button(numbers_frame, text=button_val, command=functools.partial(_on_press_number, button_val))
        button.config(height=2, width=4)
        button.grid(row=i, column=j, sticky=tk.EW)

        # add button the the dictionary
        num_buttons_dict[button_val] = button

# add button zero
button = tk.Button(numbers_frame, text='0', command=functools.partial(_on_press_number, 0))
button.grid(row=3, column=1, sticky=tk.W + tk.E)
button.config(height=2, width=4)
num_buttons_dict[0] = button

# add backspace
backspace_button = tk.Button(numbers_frame, text='<<', command=_on_press_backspace)
backspace_button.grid(row=3, column=2, sticky=tk.W+tk.E)
backspace_button.config(height=2, width=4)

# add decimal point button
decimal_button = tk.Button(numbers_frame, text='.', command=_on_press_decimal)
decimal_button.grid(row=3, column=0, sticky=tk.W+tk.E)
decimal_button.config(height=2, width=4)

# operations frame
operations_frame = ttk.LabelFrame(win, text='')
operations_frame.grid(row=1, column=1)


def _on_press_ac():
    '''
    Clears all user input
    :return: (None)
    '''
    expression_str.set('0')


def _on_press_add():
    pass


def _on_press_subtract():
    pass


def _on_press_multiply():
    pass


def _on_press_divide():
    pass


def _on_press_equals():
    s = expression_str.get()
    out = eval(s)
    expression_str.set(out)


ac_button = tk.Button(operations_frame, text='AC', command=_on_press_ac)
ac_button.grid(row=0, column=0, columnspan=2, sticky=tk.W + tk.E)
ac_button.config(height=2, width=4)
# ttk.Style().configure(ac_button, background='#006400')

add_button = tk.Button(operations_frame, text='+', command=_on_press_add)
add_button.config(height=2, width=4)
add_button.grid(row=1, column=0)
subtract_button = tk.Button(operations_frame, text='-', command=_on_press_subtract)
subtract_button.config(height=2, width=4)
subtract_button.grid(row=1, column=1)
multiply_button = tk.Button(operations_frame, text='*', command=_on_press_multiply)
multiply_button.config(height=2, width=4)
multiply_button.grid(row=2, column=0)
divide_button = tk.Button(operations_frame, text='/', command=_on_press_divide)
divide_button.config(height=2, width=4)
divide_button.grid(row=2, column=1)
equals_button = tk.Button(operations_frame, text='=', command=_on_press_equals)
equals_button.config(height=2, width=4)
equals_button.grid(row=3, column=0, columnspan=2, sticky=tk.W + tk.E)

win.mainloop()
