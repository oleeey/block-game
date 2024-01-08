import tkinter as tk
import time, random, sys, os


win = tk.Tk()
win.title("Snake Game")
win.geometry("500x500")

canvas = tk.Canvas(win, width="500", height="500", background="black")
canvas.pack(fill="both", expand=True)

class Shape():
    def __init__(self, l, x, y, c):
        self.x = x
        self.y = y
        self.length = l
        self.color = c
        self.create()
        self.direction = ""
        self.game_over = False
        self.speed = 0.05
        self.deltax = (self.length / 2) / 500
        self.deltay = (self.length / 2) / 500
        self.p1 = [round(self.x - self.deltax, 2), round(self.y - self.deltay, 2)] # Oben links
        self.p2 = [round(self.x + self.deltax, 2), round(self.y + self.deltay, 2)] # Unten rechts

    def create(self):
        self.canvas = tk.Canvas(canvas, width=self.length, height=self.length, background=self.color)
        self.canvas.place(relx=self.x, rely=self.y, anchor="center")

    def changeX(self, num):
        self.x += num
        self.p1[0] += num
        self.p2[0] += num

    def changeY(self, num):
        self.y += num
        self.p1[1] += num
        self.p2[1] += num

    def moveLeft(self):
        if self.p1[0] < self.deltax:
            self.game_over = True
            print("game over")
        else:
            self.canvas.place(relx=player.x - self.speed)
            self.changeX(-self.speed)
            
    def moveRight(self):
        if self.p2[0] > 1 - self.deltax:
            self.game_over = True
            print("game over")
        else:
            self.canvas.place(relx=player.x + self.speed)
            self.changeX(self.speed)
    
    def moveUp(self):
        if self.p1[1] < self.deltay:
            self.game_over = True
            print("game over")
        else:
            self.canvas.place(rely=player.y - self.speed)
            self.changeY(-self.speed)

    def moveDown(self):
        if self.p2[1] > 1 - self.deltay:
            self.game_over = True
            print("game over")
        else:
            self.canvas.place(rely=player.y + self.speed)
            self.changeY(self.speed)

    def __repr__(self):
        return repr(self.p1), repr(self.p2)

def onKeyPress(e):
    key = e.keysym
    if key == "Left":
        if player.direction != "right":
            player.direction = "left"
    elif key == "Right":
        if player.direction != "left":
            player.direction = "right"
    elif key == "Up":
        if player.direction != "down":
            player.direction = "up"
    elif key == "Down":
        if player.direction != "up":
            player.direction = "down"
        
player = Shape(40, 0.5, 0.5, "white")

apple = Shape(40, (random.randrange(5, 95)) / 100, (random.randrange(5, 95)) / 100, "red")

win.bind("<KeyPress>", onKeyPress)

while not player.game_over:
    sec = 0.05
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

    if player.p1[0] <= apple.p2[0] and player.p1[0] >= apple.p1[0] and player.p1[1] <= apple.p2[1] and player.p1[1] >= apple.p1[1]:
        apple.canvas.place(relx=-100, rely=-100)
        del apple
        apple = Shape(40, (random.randrange(5, 95)) / 100, (random.randrange(5, 95)) / 100, "red")
        
    #print([round(player.x, 2), round(player.y, 2)])  
    #print(player.p2)
    
    win.update_idletasks()
    win.update()

os.execl(sys.executable, f'"{sys.executable}"', *sys.argv) # Startet das Programm automatisch neu wenn man verloren hat











