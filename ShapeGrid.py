import tkinter as tk
import json
from tkinter import filedialog


class GridPaint:
    def __init__(self):
        self.DIR = "saves/"

        # Creates the window and colours it
        self.HEIGHT = 600
        self.WIDTH = 800
        self.window = tk.Tk()
        self.window.title('Grid Paint')
        f = tk.Frame(self.window, width=self.WIDTH, height=50, bg='white')
        self.c = tk.Canvas(self.window, width=self.WIDTH, height=self.HEIGHT, bg='white')

        self.pen_colour = 'black'

        self.sqr_id = ()
        self.board_state = {}

        # Binds the mouse buttons to the correct functions
        self.c.bind_all('<Button-1>', self.colour)
        self.c.bind_all('<Button-3>', self.erase)

        menu_bar = tk.Menu(self.window)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Save As", command=self.save)
        file_menu.add_command(label="Load", command=self.load)
        file_menu.add_command(label="Close", command=self.close)
        menu_bar.add_cascade(label="File", menu=file_menu)

        colour_menu = tk.Menu(menu_bar, tearoff=0)
        colour_menu.add_command(label="Black", command=lambda: self.change_clr("black"))
        colour_menu.add_command(label="Red", command=lambda: self.change_clr("red"))
        colour_menu.add_command(label="Yellow", command=lambda: self.change_clr("yellow"))
        colour_menu.add_command(label="Blue", command=lambda: self.change_clr("blue"))
        colour_menu.add_command(label="Green", command=lambda: self.change_clr("#0f0"))
        menu_bar.add_cascade(label="Colours", menu=colour_menu)

        format_menu = tk.Menu(menu_bar, tearoff=0)
        format_menu.add_command(label="Clear", command=self.clear)
        menu_bar.add_cascade(label="Format", menu=format_menu)

        self.window.config(menu=menu_bar)

        # Runs the selected function to create the grid
        self.create_grid()

        # Buttons to select the colour of the Pen
        button_black = tk.Button(f, text='Black', command=lambda: self.change_clr("black"), bg='black', fg='white')
        button_black.pack(side=tk.LEFT)

        button_red = tk.Button(f, text='Red', command=lambda: self.change_clr("red"), bg='red', fg='white')
        button_red.pack(side=tk.LEFT)

        button_yellow = tk.Button(f, text='Yellow', command=lambda: self.change_clr("yellow"), bg='yellow')
        button_yellow.pack(side=tk.LEFT)

        button_blue = tk.Button(f, text='Blue', command=lambda: self.change_clr("blue"), bg='blue', fg='white')
        button_blue.pack(side=tk.LEFT)

        button_green = tk.Button(f, text='Green', command=lambda: self.change_clr("#0f0"), bg='#0f0')
        button_green.pack(side=tk.LEFT)

        # Buttons to clear the grid and to exit the program
        button_clear = tk.Button(f, text='Clear!', command=self.clear)
        button_clear.pack(side=tk.LEFT)

        self.current_clr = tk.Label(f, text="Current", bg=self.pen_colour, fg=self.pen_colour)
        self.current_clr.pack(side=tk.LEFT)

        # closes the canvas
        f.pack()
        self.c.pack()

        self.window.mainloop()

    def create_grid(self):
        self.sqr_id = []
        y1 = 0
        size = 20
        while y1 < self.HEIGHT:
            row = []
            x1 = 0
            while x1 < self.WIDTH:
                id1 = self.c.create_rectangle(x1, y1, x1 + size, y1 + size, outline='#ccc', fill="white")
                self.board_state[id1] = "white"
                x1 += 20
                row.append(id1)

            self.sqr_id.append(row)
            y1 += 20

    def clear(self):
        for row in self.sqr_id:
            for square in row:
                CURRENT = self.c.find_withtag(square)
                self.c.itemconfig(CURRENT, fill="white")

    # Function to fill the selected square
    def colour(self, event):
        found = self.c.find_withtag(tk.CURRENT)
        if found:
            self.c.itemconfig(tk.CURRENT, fill=self.pen_colour)
            self.board_state[found[0]] = self.pen_colour
            self.c.update_idletasks()

    # Function to erase the selected square
    def erase(self, event):
        if self.c.find_withtag(tk.CURRENT):
            self.c.itemconfig(tk.CURRENT, fill='white')
            self.c.update_idletasks()

    def close(self):
        self.window.destroy()

    def change_clr(self, clr):
        self.pen_colour = clr
        self.current_clr.configure(bg=clr, fg=clr)

    def save(self):
        file = filedialog.asksaveasfile(mode="w", initialdir=self.DIR,
                                        title="Select a File",
                                        defaultextension=".json",
                                        filetypes=(("JSON files",
                                                    "*.json*"),
                                                   ))
        if not file:
            return

        json.dump(self.board_state, file)

    def load(self):
        file = filedialog.askopenfile(mode="r",
                                      initialdir=self.DIR,
                                      title="Open a Save",
                                      filetypes=(("JSON files",
                                                  "*.json"),
                                                 ))

        if not file:
            return

        self.board_state = json.load(file)

        for row in self.sqr_id:
            for square in row:
                current = self.c.find_withtag(square)
                self.c.itemconfig(current, fill=self.board_state[str(square)])


if __name__ == "__main__":
    GridPaint()
