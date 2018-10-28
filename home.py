import tkinter as tk
from tkinter import ttk
import functools
from menu_bar import MenuBar

win = tk.Tk()
win.resizable(False, False)
win.title("Simple Calculator")

# a boolean which marks that an expression has been evaluated
expression_evaluated = False

# the last answer calculated is stored
last_answer = None

# Expression Label Frame
# TODO remove the line created by label frame
input_frame = ttk.LabelFrame(win, text='')
input_frame.grid(row=0, column=0, columnspan=2)

# TODO find a way to increase height of textbox
expression_str = tk.StringVar(value='0')
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
    if expression_evaluated:
        _on_press_ac()

    s = expression_str.get()
    if s == '0':
        expression_str.set(str(number))
    else:
        s = s + str(number)
        expression_str.set(s)


def _on_press_backspace():
    """
    implements functionality for pressing backspace
    :return:
    """
    if expression_evaluated:
        _on_press_ac()
        return

    s = expression_str.get()
    if len(s) > 0:
        s = s[:-1]
    expression_str.set(s)
    if s == '':
        expression_str.set('0')


def _on_press_decimal():
    """
    Determines what happens when the decimal button is pressed.
    When pressed, a decimal point appears in the expression bar
    :return: (None)
    """
    if expression_evaluated:
        _on_press_ac()

    s = expression_str.get()
    s += '.'
    expression_str.set(s)


num_buttons_dict = {}

# creates 1-9 number buttons in a 3x3 grid
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
backspace_button.grid(row=3, column=2, sticky=tk.W + tk.E)
backspace_button.config(height=2, width=4)

# add decimal point button
decimal_button = tk.Button(numbers_frame, text='.', command=_on_press_decimal)
decimal_button.grid(row=3, column=0, sticky=tk.W + tk.E)
decimal_button.config(height=2, width=4)

# operations frame
operations_frame = ttk.LabelFrame(win, text='')
operations_frame.grid(row=1, column=1)


def _on_press_ac():
    """
    Clears all user input
    :return: (None)
    """
    global expression_evaluated
    expression_evaluated = False
    expression_str.set('0')
    expression_box.config(foreground='black')


def _on_press_ans():
    """
    Pressing this button causes the last value evaluated
    to be printed in the expression bar.
    If there is nothing in history, nothing happens.
    :return: (None)
    """
    global last_answer
    global expression_evaluated

    if last_answer is None:
        return

    if expression_evaluated:
        _on_press_ac()

    s = expression_str.get()
    if s == '0':
        expression_str.set(last_answer)
    else:
        s += str(last_answer)
        expression_str.set(s)


def _on_press_add():
    """
    Determines what happens when add button is pressed.
    When pressed, a plus sign appears in expression bar
    :return: (None)
    """
    if expression_evaluated:
        if last_answer is None:
            _on_press_ac()
        else:
            global expression_evaluated
            expression_evaluated = False

    s = expression_str.get()
    s += '+'
    expression_str.set(s)


def _on_press_subtract():
    """
    Determines what happens when the subtract button is pressed.
    When pressed, a minus sign appears in the expression bar
    :return: (None)
    """
    if expression_evaluated:
        if last_answer is None:
            _on_press_ac()
        else:
            global expression_evaluated
            expression_evaluated = False

    s = expression_str.get()
    s += '-'
    expression_str.set(s)


def _on_press_multiply():
    """
    Determines what happens when the multiply button is pressed.
    When pressed, a multiplication sign appears in the expression bar
    :return: (None)
    """
    if expression_evaluated:
        if last_answer is None:
            _on_press_ac()
        else:
            global expression_evaluated
            expression_evaluated = False

    s = expression_str.get()
    s += '*'
    expression_str.set(s)


def _on_press_divide():
    """
    Determines what happens when the division button is pressed.
    When pressed, a divide sign appears in the expression bar
    :return: (None)
    """
    if expression_evaluated:
        if last_answer is None:
            _on_press_ac()
        else:
            global expression_evaluated
            expression_evaluated = False

    s = expression_str.get()
    s += '/'
    expression_str.set(s)


def _on_press_equals():
    global expression_evaluated
    global last_answer
    s = expression_str.get()

    try:
        out = eval(s)
        expression_box.config(foreground='black')
        last_answer = out
    except SyntaxError:
        out = 'Invalid Input'
        expression_box.config(foreground='red')
    except ZeroDivisionError:
        out = 'Division by Zero'
        expression_box.config(foreground='red')

    expression_str.set(out)
    expression_evaluated = True


ac_button = tk.Button(operations_frame, text='AC', command=_on_press_ac)
ac_button.grid(row=0, column=0, columnspan=1, sticky=tk.W + tk.E)
ac_button.config(height=2, width=4)

ans_button = tk.Button(operations_frame, text='Ans', command=_on_press_ans)
ans_button.grid(row=0, column=1, columnspan=1, sticky=tk.EW)
ans_button.config(height=2, width=4)

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

# add a menu bar
win.config(menu=MenuBar(win))

# test case
expression_str.set('0')

win.mainloop()
