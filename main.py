from pyxel import *
from time import *
x = 64
y = 64
UP = [False, 0]
RIGHT = [False, 0]
LEFT = [False, 0]
init(128, 128, title="Nuit du Code")

def update():
    global y, x
    move()
    print(x)
    print(y)

def draw():
    global x, y
    rect(x, y, 5, 5, 12)
    cls(0)
   

def move():
    global x, y, UP, LEFT, RIGHT
    if UP[0] == True :
        if UP[1] == 0 :
            UP[0] = False
        else :
            UP[1] -= 1
            y = y - 10
            sleep(0.1)
    elif btn(KEY_UP) == True :   
        if UP[0] == False :
            UP[0] = True
            UP[1] = 10    
    
    if RIGHT[0] == True :
        if RIGHT[1] == 0 :
            RIGHT[0] = False
        else :
            RIGHT[1] -= 1
            x = x + 10
    elif btn(KEY_RIGHT) == True :    
        RIGHT[0] = True
        RIGHT[1] = 1
    
    if LEFT[0] == True :
        if LEFT[1] == 0 :
            LEFT[0] = False
        else :
            LEFT[1] -= 1
            x = x - 10
    elif btn(KEY_LEFT) == True :    
        LEFT[0] = True
        LEFT[1] = 1

run(update, draw)