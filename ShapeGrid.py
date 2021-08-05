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
        self.c = tk.Canvas(self.window, width=self.WIDTH, height=self.HEIGHT, bg='black')

        self.pen_colour = 'black'

        self.sqr_id = ()
        self.board_state = {}

        # Binds the mouse buttons to the correct functions
        self.c.bind_all('<Button-1>', self.colour)
        self.c.bind_all('<Button-3>', self.erase)

        # Runs the selected function to create the grid
        self.create_grid()

        btn_save = tk.Button(f, text="Save", command=self.save)
        btn_save.pack(side=tk.LEFT)

        btn_load = tk.Button(f, text="Load", command=self.load)
        btn_load.pack(side=tk.LEFT)

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

        button_exit = tk.Button(f, text='X', command=self.close, bg="red")
        button_exit.pack(side=tk.LEFT)

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
