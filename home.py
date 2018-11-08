import tkinter as tk
import functools
from menu_bar import MenuBar
from custom_buttons import NumberButton, OperatorButton, SpecialButton

win = tk.Tk()
win.resizable(False, False)
win.title("Simple Calculator")
win.config(background='#243313')

# marked true once equals has been pressed (and answer has been displayed)
# when true, pressing most buttons causes a reset to 0 before performing button action
expression_evaluated = False

# the last answer calculated is stored
# if there is was error in expression, the value is set to None again
last_answer = None

# Expression Label Frame
# TODO remove the line created by label frame
input_frame = tk.LabelFrame(win, text='')
input_frame.grid(row=0, column=0, columnspan=2, sticky=tk.W + tk.E, padx=5, pady=5)

# TODO find a way to increase height of textbox
expression_str = tk.StringVar(value='0')
expression_box = tk.Entry(input_frame, textvariable=expression_str, state='readonly', width=34)
expression_box.config(readonlybackground='BLACK', foreground='#F2FF80')
expression_box.grid(row=0, column=0, sticky=tk.EW)

# Numbers Label Frame
numbers_frame = tk.LabelFrame(win, text='')
numbers_frame.grid(row=1, column=0, padx=5, pady=5)


# create the numbers buttons
def _on_press_number(number, event=None):
    """
    Adds the pressed number to the expression bar
    When at 0 state, just replaces that state with the number
    :param number: (int) the button that has been pressed
    :return: (None)
    """

    if expression_evaluated:
        _on_press_ac()

    s = expression_str.get()
    if s == '0':
        expression_str.set(str(number))
    else:
        s = s + str(number)
        expression_str.set(s)


def _on_press_backspace(event=None):
    """
    Implements functionality for pressing backspace
    In most cases, simply removes the last character in the expression
    If this causes the expression to become blank, resets to 0 state
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


def _on_press_decimal(event=None):
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
        button_val = (2 - i) * 3 + j + 1  # to get numbers in the order you see on a calc
        button = NumberButton(numbers_frame, text=button_val, command=functools.partial(_on_press_number, button_val),
                              grid_placement=(i, j))

        # bind keyboard key to button
        win.bind(str(button_val), functools.partial(_on_press_number, button_val))

        # add button the the dictionary
        num_buttons_dict[button_val] = button

# add button zero
button = NumberButton(numbers_frame, text='0', command=functools.partial(_on_press_number, 0), grid_placement=(3, 1))
win.bind('0', functools.partial(_on_press_number, 0))  # bind to keyboard
num_buttons_dict[0] = button  # add to buttons dictionary

# add backspace
backspace_button = OperatorButton(numbers_frame, text='<<', command=_on_press_backspace, grid_placement=(3, 2))
win.bind('<BackSpace>', _on_press_backspace)

# add decimal point button
decimal_button = OperatorButton(numbers_frame, text='.', command=_on_press_decimal, grid_placement=(3, 0))
win.bind('.', _on_press_decimal)

# operations frame
operations_frame = tk.LabelFrame(win, text='')
operations_frame.grid(row=1, column=1, padx=5, pady=5)


def _on_press_ac():
    """
    Clears all user input
    Also resets certain boolean flags back to defaults
    :return: (None)
    """
    global expression_evaluated
    expression_evaluated = False
    expression_str.set('0')
    expression_box.config(foreground='#F2FF80')


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


def _on_press_add(event=None):
    """
    Determines what happens when add button is pressed.
    When pressed, a plus sign appears in expression bar
    :return: (None)
    """
    global expression_evaluated

    if expression_evaluated:
        if last_answer is None:
            _on_press_ac()
        else:
            expression_evaluated = False

    s = expression_str.get()
    s += '+'
    expression_str.set(s)


def _on_press_subtract(event=None):
    """
    Determines what happens when the subtract button is pressed.
    When pressed, a minus sign appears in the expression bar
    :return: (None)
    """
    global expression_evaluated

    if expression_evaluated:
        if last_answer is None:
            _on_press_ac()
        else:
            expression_evaluated = False

    s = expression_str.get()
    s += '-'
    expression_str.set(s)


def _on_press_multiply(event=None):
    """
    Determines what happens when the multiply button is pressed.
    When pressed, a multiplication sign appears in the expression bar
    :return: (None)
    """
    global expression_evaluated

    if expression_evaluated:
        if last_answer is None:
            _on_press_ac()
        else:
            expression_evaluated = False

    s = expression_str.get()
    s += '*'
    expression_str.set(s)


def _on_press_divide(event=None):
    """
    Determines what happens when the division button is pressed.
    When pressed, a divide sign appears in the expression bar
    :return: (None)
    """
    global expression_evaluated

    if expression_evaluated:
        if last_answer is None:
            _on_press_ac()
        else:
            expression_evaluated = False

    s = expression_str.get()
    s += '/'
    expression_str.set(s)


def _on_press_equals(event=None):
    """
    Action performed upon pressing the equals button
    Runs eval and displays the output. Error message displayed for bad input.
    :return:
    """
    global expression_evaluated
    global last_answer
    s = expression_str.get()

    try:
        out = eval(s)
        last_answer = out
    except SyntaxError:
        out = 'Invalid Input'
        expression_box.config(foreground='red')
        last_answer = None
    except ZeroDivisionError:
        out = 'Division by Zero'
        expression_box.config(foreground='red')
        last_answer = None

    expression_str.set(out)
    expression_evaluated = True


ac_button = SpecialButton(operations_frame, text='AC', command=_on_press_ac, grid_placement=(0, 0))

ans_button = SpecialButton(operations_frame, text='Ans', command=_on_press_ans, grid_placement=(0, 1))

add_button = OperatorButton(operations_frame, text='+', command=_on_press_add, grid_placement=(1, 0))
win.bind('+', _on_press_add)

subtract_button = OperatorButton(operations_frame, text='-', command=_on_press_subtract, grid_placement=(1, 1))
win.bind('-', _on_press_subtract)

multiply_button = OperatorButton(operations_frame, text='*', command=_on_press_multiply, grid_placement=(2, 0))
win.bind('*', _on_press_multiply)

divide_button = OperatorButton(operations_frame, text='/', command=_on_press_divide, grid_placement=(2, 1))
win.bind(r'/', _on_press_divide)

equals_button = SpecialButton(operations_frame, text='=', command=_on_press_equals, grid_placement=(3, 0))
equals_button.grid(columnspan=2, sticky=tk.W + tk.E)
win.bind('<Enter>', _on_press_equals)

# add a menu bar
win.config(menu=MenuBar(win))

# test case
expression_str.set('0')

win.mainloop()
