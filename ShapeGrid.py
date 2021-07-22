from tkinter import *


class GridPaint:
    def __init__(self):
        # Creates the window and colours it
        self.HEIGHT = 600
        self.WIDTH = 800
        self.window = Tk()
        self.window.title('Shape Grid')
        self.f = Frame(self.window, width=self.WIDTH, height=50, bg='white')
        self.c = Canvas(self.window, width=self.WIDTH, height=self.HEIGHT, bg='black')
        self.id1 = None

        self.pen_colour = 'black'

        self.sqr_id = list()

        # Binds the mouse buttons to the correct functions
        self.c.bind_all('<Button-1>', self.colour)
        self.c.bind_all('<Button-3>', self.erase)

        # Runs the selected function to create the grid
        self.create_grid()

        # Buttons to select the colour of the Pen
        button_black = Button(self.f, text='Black', command=self.black, bg='black', fg='white')
        button_black.pack(side=LEFT)

        button_red = Button(self.f, text='Red', command=self.red, bg='red', fg='white')
        button_red.pack(side=LEFT)

        button_yellow = Button(self.f, text='Yellow', command=self.yellow, bg='yellow')
        button_yellow.pack(side=LEFT)

        button_blue = Button(self.f, text='Blue', command=self.blue, bg='blue', fg='white')
        button_blue.pack(side=LEFT)

        button_green = Button(self.f, text='Green', command=self.green, bg='#0f0')
        button_green.pack(side=LEFT)

        button_square = Button(self.f, text="Square", command=self.square)
        button_square.pack(side=LEFT)

        # Buttons to clear the grid and to exit the program
        button_clear = Button(self.f, text='Clear!', command=self.create_grid)
        button_clear.pack(side=LEFT)

        button_exit = Button(self.f, text='Exit', command=self.close)
        button_exit.pack(side=LEFT)

        # closes the canvas
        self.f.pack()
        self.c.pack()

        self.window.mainloop()

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

    # Function to create the grid

    def create_grid(self):
        x1 = 0
        x2 = 20
        y1 = 0
        y2 = 20
        for i in range(29):
            for i in range(40):
                id1 = self.c.create_rectangle(x1, y1, x2, y2, outline='#ccc', fill='white')
                x1 += 20
                x2 += 20
                self.sqr_id.append(id1)

            y1 += 20
            y2 += 20
            for i in range(40):
                x1 -= 20
                x2 -= 20
                id1 = self.c.create_rectangle(x1, y1, x2, y2, outline='#ccc', fill='white')

    # Function to exit the program
    def close(self):
        self.window.destroy()

    # Functions to change the colour of the pen
    def black(self):
        self.pen_colour = 'black'

    def red(self):
        self.pen_colour = 'red'

    def yellow(self):
        self.pen_colour = 'yellow'

    def blue(self):
        self.pen_colour = 'blue'

    def green(self):
        self.pen_colour = '#0f0'

    # Functions for set shapes
    def square(self):
        n = 11
        for i in range(10):
            self.c.itemconfig(n, fill=self.pen_colour)
            self.c.update_idletasks()
            n += 1

        n = 50
        for i in range(10):
            line = self.sqr_id[n]
            self.c.itemconfig(line, fill=self.pen_colour)
            self.c.update_idletasks()
            n += 40

        n = 59
        for i in range(10):
            line = self.sqr_id[n]
            self.c.itemconfig(line, fill=self.pen_colour)
            self.c.update_idletasks()
            n += 40

        n = 410
        for i in range(10):
            line = self.sqr_id[n]
            self.c.itemconfig(line, fill=self.pen_colour)
            self.c.update_idletasks()
            n += 1


if __name__ == "__main__":
    GridPaint()
