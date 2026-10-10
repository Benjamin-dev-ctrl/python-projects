import pgzrun
import random
WIDTH=700
HEIGHT=466
basket=Actor('basket.png',(350,380))
def draw():
    screen.blit('fruitbackground.jpg',(0,0))
    basket.draw()
def update():
    if keyboard.a:
        basket.x-=3
    if keyboard.d:
        basket.x+=3
pgzrun.go()
    
