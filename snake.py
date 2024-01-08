import tkinter as tk
import time
import threading


win = tk.Tk()
win.title("Snake Game")
win.geometry("500x500")

canvas = tk.Canvas(win, width="500", height="500", background="black")
canvas.pack(fill="both", expand=True)

class Shape():
    def __init__(self, l, x, y):
        self.x = x
        self.y = y
        self.length = l
        self.create()
        self.direction = ""

    def create(self):
        self.canvas = tk.Canvas(canvas, width=self.length, height=self.length, background="white")
        self.canvas.place(relx=self.x, rely=self.y, anchor="center")

    def changeX(self, num):
        self.x += num

    def changeY(self, num):
        self.y += num

    def moveLeft(self):
        if self.x - 0.05 > 0:
            self.canvas.place(relx=player.x - 0.05)
            self.changeX(-0.05)
        else:
            self.canvas.place(relx=player.x + 1)
            self.changeX(1)
 
    def moveRight(self):
        if self.x - 0.05 < 0.95:
            self.canvas.place(relx=player.x + 0.05)
            self.changeX(0.05)
        else:
            self.canvas.place(relx=player.x - 1)
            self.changeX(-1)
    
    def moveUp(self):
        if self.y - 0.05 > 0:
            self.canvas.place(rely=player.y - 0.05)
            self.changeY(-0.05)
        else:
            self.canvas.place(rely=player.y + 1)
            self.changeY(1)

    def moveDown(self):
        if self.y + 0.05 < 1.05:
            self.canvas.place(rely=player.y + 0.05)
            self.changeY(0.05)
        else:
            self.canvas.place(rely=player.y - 1)
            self.changeY(-1)

def onKeyPress(e):
    key = e.keysym
    if key == "Left":
        player.direction = "left"
    elif key == "Right":
        player.direction = "right"
    elif key == "Up":
        player.direction = "up"
    elif key == "Down":
       player.direction = "down"
    
player = Shape(40, 0.5, 0.5)

win.bind("<KeyPress>", onKeyPress)

#win.mainloop()

while True:
    sec = 0.1
    if player.direction == "left":
        time.sleep(sec)
        player.moveLeft()
    elif player.direction == "right":
        player.moveRight()
        time.sleep(sec)
    elif player.direction == "up":
        player.moveUp()
        time.sleep(sec)
    elif player.direction == "down":
        player.moveDown()
        time.sleep(sec)
        
    #print([round(player.x, 2), round(player.y, 2)])
    
    win.update_idletasks()
    win.update()








