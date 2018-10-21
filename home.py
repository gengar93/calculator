import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.resizable(False, False)
win.title("Simple Calculator")

# Expression Label Frame
# TODO remove tha line created by label frame
input_frame = ttk.LabelFrame(win, text='')
input_frame.grid(row=0, column=0, columnspan=2)

# TODO find a way to increase height of textbox
expression_str = tk.StringVar()
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
    pass

num_buttons_list = []

for i in range(3):
    for j in range(3):
        button_val = (2-i) * 3 + j + 1
        button = ttk.Button(numbers_frame, text=button_val, command=lambda: _on_press_number(button_val))
        button.grid(row=i, column=j)


win.mainloop()
