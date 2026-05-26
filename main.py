from pyxel import *
from time import *
x = 64
y = 64
UP = [False, 0]
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
    rect(x, y, 5, 5, 7)
   

def move():
    global x, y, UP, LEFT, RIGHT, speed, DOWN
    if UP[0] == True :
        if UP[1] == 0 :
            UP[0] = False
        else :
            UP[1] -= 1
            if speed == 4 or speed >= 4 :
                if speed == 0 or speed <= 0 :
                    speed += 0.4
                else :
                    speed = speed - 4
            else :
                speed = speed + 0.4
            y = y - speed
    elif btn(KEY_UP) == True and DOWN[0] == False :
        if UP[0] == False and DOWN[0] == False:
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
            if speed_down == 4 or speed_down >= 4 :
                if speed_down == 0 or speed_down <= 0 :
                    speed_down += 0.4
                else :
                    speed_down = speed_down - 4
            else :
                speed_down = speed_down + 0.4
            y = y + speed_down 
        if DOWN[0] == True and sol == True:
            DOWN[0] = False
def ground():
    global y, sol
    sol = False
    if y > 64 :
        sol = True
        return True



        

    

run(update, draw)