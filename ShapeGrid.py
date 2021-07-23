from tkinter import *


class GridPaint:
    def __init__(self):
        # Creates the window and colours it
        self.HEIGHT = 600
        self.WIDTH = 800
        self.window = Tk()
        self.window.title('Grid Paint')
        f = Frame(self.window, width=self.WIDTH, height=50, bg='white')
        self.c = Canvas(self.window, width=self.WIDTH, height=self.HEIGHT, bg='black')

        self.pen_colour = 'black'

        self.sqr_id = list()

        # Binds the mouse buttons to the correct functions
        self.c.bind_all('<Button-1>', self.colour)
        self.c.bind_all('<Button-3>', self.erase)

        # Runs the selected function to create the grid
        self.create_grid()

        # Buttons to select the colour of the Pen
        button_black = Button(f, text='Black', command=lambda: self.change_clr("black"), bg='black', fg='white')
        button_black.pack(side=LEFT)

        button_red = Button(f, text='Red', command=lambda: self.change_clr("red"), bg='red', fg='white')
        button_red.pack(side=LEFT)

        button_yellow = Button(f, text='Yellow', command=lambda: self.change_clr("yellow"), bg='yellow')
        button_yellow.pack(side=LEFT)

        button_blue = Button(f, text='Blue', command=lambda: self.change_clr("blue"), bg='blue', fg='white')
        button_blue.pack(side=LEFT)

        button_green = Button(f, text='Green', command=lambda: self.change_clr("#0f0"), bg='#0f0')
        button_green.pack(side=LEFT)

        # Buttons to clear the grid and to exit the program
        button_clear = Button(f, text='Clear!', command=self.create_grid)
        button_clear.pack(side=LEFT)

        button_exit = Button(f, text='X', command=self.close, bg="red")
        button_exit.pack(side=LEFT)

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
                x1 += 20
                row.append(id1)

            self.sqr_id.append(row)
            y1 += 20

    # Function to fill the selected square
    def colour(self, event):
        if self.c.find_withtag(CURRENT):
            self.c.itemconfig(CURRENT, fill=self.pen_colour)
            self.c.update_idletasks()

    # Function to erase the selected square
    def erase(self, event):
        if self.c.find_withtag(CURRENT):
            self.c.itemconfig(CURRENT, fill='white')
            self.c.update_idletasks()

    def close(self):
        self.window.destroy()

    def change_clr(self, clr):
        self.pen_colour = clr


if __name__ == "__main__":
    GridPaint()
