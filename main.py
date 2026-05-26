from pyxel import *
x = 0
y = 0
init(128, 128, title="Nuit du Code")

def update():
    pass
def draw():
    global x, y
    rect(x, y, 1, 5, 00)
    pass

def move():
    global x, y 
    if btn(KEY_UP) == True :
    
    if btn(KEY_DOWN) == True :

    if btn(KEY_LEFT) == True :

    if btn(KEY_RIGHT) == True :
