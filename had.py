import os 
import time 
import keyboard
import random




#YHRANICE=int(input("zadej velikost y pole"))+2
YHRANICE=10


XHRANICE=int(YHRANICE*2)+2
X=int(XHRANICE/2)
Y=int(YHRANICE/2)
STARPOZ=(XHRANICE/3,YHRANICE/3)
GAME=True
DELEY=0.1
SCORE=0



def render_board():
    global XHRANICE,YHRANICE
    print("/"*XHRANICE)
    for index_radek in range(YHRANICE-2):
        print("/", end="")
        for index_sloupec in range(XHRANICE):
            if (index_radek,index_sloupec) == (Y,X):
                print( "X", end="")
                
            else:
                print(" ", end="")
        print("/")
        
    print("/"*XHRANICE)
    print("nakresleno")
    time.sleep(2)


def skore():
    global STARPOZ,X,Y,SCORE
    if STARPOZ==(X,Y):
        SCORE+=1
        return



def star():
    global STARPOZ
    global X 
    global Y
    x=random.randint(1,XHRANICE-1)
    y=random.randint(1,YHRANICE-1)
    if (x, y)!= (X , Y):
        STARPOZ=(x,y)
        
    else:
        star()
    print("star done")
    time.sleep(2)



def move_player():
    global X ,Y,STARPOZ,GAME
    

    if keyboard.is_pressed("w"):
            Y   -= 1

    if keyboard.is_pressed("s"):
            Y += 1

    if keyboard.is_pressed("a"):
            X -= 1

    if keyboard.is_pressed("d"):
            X += 1

        



def game_loop():
    global GAME
    while GAME==True:
        print("vasdf")
        time.sleep(2)
        render_board()
        star()
        move_player()
        render_board()
        skore()
        if keyboard.is_pressed("space"):
            GAME = False
            break

print("před")
game_loop()

