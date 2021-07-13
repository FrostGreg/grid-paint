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

#####Function to create the grid#####
sqr_id = list()

coord = list()
X = list(range(41))
coord.append(X)
Y = list(range(30))
coord.append(Y)

def create_grid():
    for i in range(29):
        for i in range(40):
            i = 0
            j = 0
            id1 = c.create_rectangle(x1, y1, x2, y2, outline='#ccc', fill='white')
            x1 += 20
            x2 += 20
            
            
        y1 += 20
        y2 += 20
        for i in range(40):
            x1 -= 20
            x2 -= 20
            id1 = c.create_rectangle(x1, y1, x2, y2, outline='#ccc', fill='white')


create_grid()
c.pack()
