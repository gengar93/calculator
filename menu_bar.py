import tkinter as tk
from tkinter import ttk, Menu, messagebox


class MenuBar(Menu):
    def __init__(self, window, **kw):
        #Menu.__init__(self, window)
        super().__init__(window)
        self.window = window
        self._make_file_menu()
        self._make_help_menu()

    def _not_implemented(self):
        messagebox.showinfo("Not implemented", "This feature is not implemented yet")

    def _select_new(self):
        self._not_implemented()

    def _quit(self):
        self.window.quit()
        self.window.destroy()
        exit()

    def _make_file_menu(self):
        file_menu = Menu(self, tearoff=0)
        file_menu.add_command(label='New', command=self._select_new)
        file_menu.add_separator()
        file_menu.add_command(label='Quit', command=self._quit)
        self.add_cascade(label='File', menu=file_menu)

    def _select_about(self):
        messagebox.showinfo("A Basic Calculator", "This is a basic calculator built using tkinter.")

    def _make_help_menu(self):
        help_menu = Menu(self, tearoff=0)
        help_menu.add_command(label='About', command=self._select_about)
        self.add_cascade(label='Help', menu=help_menu)


if __name__ == '__main__':
    win = tk.Tk()
    ttk.Label(win, text='Paganizer').grid(row=0, column=0)
    win.config(menu=MenuBar(win))
    win.mainloop()
