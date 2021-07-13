from tkinter import *
import sys
#####Creates the window and colours it#####
HEIGHT = 600
WIDTH = 800
window = Tk()
window.title('Shape Grid')
f = Frame(window, width=WIDTH, height=50, bg='white')
c = Canvas(window, width=WIDTH, height=HEIGHT, bg='black')
id1 = None

pen_colour = 'black'

#####Function to fill the selected square#####
def colour(event):                              
    if c.find_withtag(CURRENT):
        c.itemconfig(CURRENT, fill = pen_colour)
        c.update_idletasks()

#####Function to erase the selected square#####
def erase(event):
    if c.find_withtag(CURRENT):
        c.itemconfig(CURRENT, fill='white')
        c.update_idletasks()


def find_click(e):
    global n
    n = c.find_closest(e.x, e.y)
    print(n)
    




#####Function to create the grid#####
sqr_id = list()

def create_grid():
    x1 = 0
    x2 = 20
    y1 = 0
    y2 = 20
    for i in range(29):
        for i in range(40):
            id1 = c.create_rectangle(x1, y1, x2, y2, outline='#ccc', fill='white')
            x1 += 20
            x2 += 20
            sqr_id.append(id1)
            
            
        y1 += 20
        y2 += 20
        for i in range(40):
            x1 -= 20
            x2 -= 20
            id1 = c.create_rectangle(x1, y1, x2, y2, outline='#ccc', fill='white')
            

#####Binds the mouse buttons to the correct functions#####
c.bind_all('<Button-1>', find_click)
c.bind_all('<Button-3>', erase)

#####Runs the selected function to create the grid#####
create_grid()

#####Function to exit the program#####
def Exit():
    window.destroy()
    
#####Functions to change the colour of the pen#####
def black():
    global pen_colour
    pen_colour = 'black'

def red():
    global pen_colour
    pen_colour = 'red'

def yellow():
    global pen_colour
    pen_colour = 'yellow'

def blue():
    global pen_colour
    pen_colour = 'blue'

def green():
    global pen_colour
    pen_colour = '#0f0'



#####Functions for set shapes#####
def square():
    global n

    for i in range(10):
        c.itemconfig(n, fill = pen_colour)
        c.update_idletasks()
        n += 1
            
        
    n = 50
    for i in range(10):
        line = sqr_id[n]
        c.itemconfig(line, fill = pen_colour)
        c.update_idletasks()
        n += 40
        
    n = 59
    for i in range(10):
        line = sqr_id[n]
        c.itemconfig(line, fill = pen_colour)
        c.update_idletasks()
        n += 40

    n = 410
    for i in range(10):
        line = sqr_id[n]
        c.itemconfig(line, fill=pen_colour)
        c.update_idletasks()
        n += 1
    


#####Buttons to select the colour of the Pen#####
buttonBlack = Button(f, text='Black', command=black, bg='black', fg='white')
buttonBlack.pack(side=LEFT)

buttonRed = Button(f, text='Red', command=red, bg='red', fg='white')
buttonRed.pack(side=LEFT)

buttonYellow = Button(f, text='Yellow', command=yellow, bg='yellow')
buttonYellow.pack(side=LEFT)

buttonBlue = Button(f, text='Blue', command=blue, bg='blue', fg='white')
buttonBlue.pack(side=LEFT)

buttonGreen = Button(f, text='Green', command=green, bg='#0f0')
buttonGreen.pack(side=LEFT)

buttonSquare = Button(f, text="Square", command=square)
buttonSquare.pack(side=LEFT)

#####Buttons to clear the grid and to exit the program#####
buttonClear = Button(f, text='Clear!', command=create_grid)
buttonClear.pack(side=LEFT)

buttonExit = Button(f, text='Exit', command=Exit)
buttonExit.pack(side=LEFT)

buttonclck =Button(f, text='FindClick', command=find_click)
buttonclck.pack(side=LEFT)

#####closes the canvas#####
f.pack()
c.pack()

while True:
    window.update()


