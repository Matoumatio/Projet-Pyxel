from pyxel import *
from time import *
from math import *
# Le Double saut marche pas et ne parchera surement pas
x = 64
y = 64
UP = [False, 0, 1]
RIGHT = [False, 0]
LEFT = [False, 0]
DOWN = [False,0]
speed = 0
speed_down = 0
sol = False
init(128, 128, title="Nuit du Code")

def update():
    global y, x
    move()
    sol = False
    ground()
    gravite()

def draw():
    global x, y
    cls(1)
    rect(x, y,8, 8, 7)
    rect(0, 100, 128,  10, 3)
   

def move():
    global x, y, UP, LEFT, RIGHT, speed, DOWN
    if UP[0] == True :
        if UP[1] == 0 :
            UP[0] = False
            speed = 0
            UP[2] = 1
        else :
            UP[1] -= 1
            speed = speed + 0.5
            y = y - speed
            y = y//1
    elif btn(KEY_UP) == True and DOWN[0] == False or (UP[2] == 1 and btn(KEY_UP)):
        if UP[0] == False and DOWN[0] == False and UP[2] == 1 :
            UP[2] = 0
            UP[0] = True
            UP[1] = 10    
    
    if RIGHT[0] == True :
        if RIGHT[1] == 0 :
            RIGHT[0] = False
        else :
            RIGHT[1] -= 1
            x = x + 2
    elif btn(KEY_RIGHT) == True :    
        RIGHT[0] = True
        RIGHT[1] = 1
    
    if LEFT[0] == True :
        if LEFT[1] == 0 :
            LEFT[0] = False
        else :
            LEFT[1] -= 1
            x = x - 2
    elif btn(KEY_LEFT) == True :    
        LEFT[0] = True
        LEFT[1] = 1

def gravite():
    global y, speed_down, DOWN
    if UP[0] == False :
        if sol == False :
            DOWN[0] = True
            speed_down = speed_down + 0.5
            y = y + speed_down 
        if DOWN[0] == True and sol == True:
            DOWN[0] = False
            speed_down = 0

def ground():
    global y, sol
    sol = False
    w = pget(x + 3, y + 10)
    if w == 3 or w == 4 or w == 6 :
        if w == 3 :
            sol = True
        if w == 4 or w == 6 :
            while w != 3 :
                y = y + 1
                w = pget(x + 3, y + 10)
            sol = True 
        


   

run(update, draw)