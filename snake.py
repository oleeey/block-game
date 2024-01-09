import tkinter as tk
import time, random, sys, os

global score, winL
score = 0
winL = 500

win = tk.Tk()
win.title("Snake Game")
win.geometry(str(winL) + "x" + str(winL))

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
        self.speed = self.length / winL # 0.05
        self.deltaL = (self.length / 2) / winL
        self.p1 = [round(self.x - self.deltaL, 2), round(self.y - self.deltaL, 2)] # Oben links
        self.p2 = [round(self.x + self.deltaL, 2), round(self.y - self.deltaL, 2)] # Oben rechts
        self.p3 = [round(self.x + self.deltaL, 2), round(self.y + self.deltaL, 2)] # Unten rechts
        self.p4 = [round(self.x - self.deltaL, 2), round(self.y + self.deltaL, 2)] # Unten links

    def create(self):
        self.canvas = tk.Canvas(canvas, width=self.length, height=self.length, background=self.color)
        self.canvas.place(relx=self.x, rely=self.y, anchor="center")

    def changeX(self, num):
        self.x += num
        self.p1[0] = round(self.p1[0] + num, 2)
        self.p2[0] = round(self.p2[0] + num, 2)
        self.p3[0] = round(self.p3[0] + num, 2)
        self.p4[0] = round(self.p4[0] + num, 2)

    def changeY(self, num):
        self.y += num
        self.p1[1] = round(self.p1[1] + num, 2)
        self.p2[1] = round(self.p2[1] + num, 2)
        self.p3[1] = round(self.p3[1] + num, 2)
        self.p4[1] = round(self.p4[1] + num, 2)

    def gameOver(self):
        self.game_over = True
        print("game over")

    def moveLeft(self):
        if self.p1[0] == 0:
            self.gameOver()
        else:
            self.canvas.place(relx=player.x - self.speed)
            self.changeX(-self.speed)
            
    def moveRight(self):
        if self.p3[0] == 1:
            self.gameOver()
        else:
            self.canvas.place(relx=player.x + self.speed)
            self.changeX(self.speed)
    
    def moveUp(self):
        if self.p1[1] == 0:
            self.gameOver()
        else:
            self.canvas.place(rely=player.y - self.speed)
            self.changeY(-self.speed)

    def moveDown(self):
        if self.p3[1] == 1:
            self.gameOver()
        else:
            self.canvas.place(rely=player.y + self.speed)
            self.changeY(self.speed)

    def __repr__(self):
        return repr(self.p1), repr(self.p3)
    
    def respawn(self):
        self.canvas.place(relx=-100, rely=-100)
        apple.__init__(25, (random.randrange(5, 95)) / 100, (random.randrange(5, 95)) / 100, "red")

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
        
# startPos = ((winL/2) - player.length) / winL) + deltaL
player = Shape(25, 0.475, 0.475, "white")

apple = Shape(25, (random.randrange(5, 95)) / 100, (random.randrange(5, 95)) / 100, "red")

scoreL = tk.Label(canvas, text="Score: 0", background="white")
scoreL.pack()

win.bind("<KeyPress>", onKeyPress)

sec = 0.1   # Geschwindigkeit des Spieles; je kleiner, desto schneller
while not player.game_over:
    if player.direction == "left":
        player.moveLeft()
        time.sleep(sec)
    elif player.direction == "right":
        player.moveRight()
        time.sleep(sec)
    elif player.direction == "up":
        player.moveUp()
        time.sleep(sec)
    elif player.direction == "down":
        player.moveDown()
        time.sleep(sec)

    if (player.p1[0] <= apple.p3[0] and player.p1[0] >= apple.p1[0] and  # wenn P1 vom Spieler den Apfel berührt
        player.p1[1] <= apple.p3[1] and player.p1[1] >= apple.p1[1]):

        apple.respawn()
        score += 1
        sec *= 0.96
        
    if (player.p2[0] >= apple.p4[0] and player.p2[0] <= apple.p2[0] and # wenn P2 vom Spieler den Apfel berührt
        player.p2[1] <= apple.p4[1] and player.p2[1] >= apple.p2[1]):

        apple.respawn()
        score += 1
        sec *= 0.96

    if (player.p3[0] >= apple.p1[0] and player.p3[0] <= apple.p3[0] and # wenn P3 vom Spieler den Apfel berührt
        player.p3[1] <= apple.p3[1] and player.p3[1] >= apple.p1[1]):

        apple.respawn()
        score += 1
        sec *= 0.96

    if (player.p4[0] <=  apple.p2[0] and player.p4[0] >= apple.p4[0] and # wenn P4 vom Spieler den Apfel berührt
        player.p4[1] >= apple.p2[1] and player.p4[1] <= apple.p4[1]):

        apple.respawn()
        score += 1
        sec *= 0.96

    #print([round(player.x, 2), round(player.y, 2)])  
    #print(player.p1)
        
    scoreL.configure(text="Score: " + str(score))
    win.update_idletasks()
    win.update()

print("Score:", score)
os.execl(sys.executable, f'"{sys.executable}"', *sys.argv) # Startet das Programm automatisch neu wenn man verloren hat











