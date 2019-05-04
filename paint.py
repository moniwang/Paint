from tkinter import *

class Paint(object):

    def __init__(self):
        self.root = Tk()

        self.canvas = Canvas(self.root, bg='white', width=800, height=600)
        self.canvas.grid()

        self.x = None
        self.y = None

        self.line_width = 5.0
        self.color = 'black'

        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)
        
        self.root.mainloop()

    def paint(self, event):
        if self.x and self.y:
            self.canvas.create_line(self.x, self.y, event.x, event.y,
                               width=self.line_width, fill=self.color,
                               capstyle=ROUND, smooth=TRUE)
        self.x = event.x
        self.y = event.y

    def reset(self, event):
        self.x = None
        self.y = None


if __name__ == '__main__':
    Paint()
 