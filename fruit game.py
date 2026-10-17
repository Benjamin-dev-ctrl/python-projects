import pgzrun
import random
WIDTH=700
HEIGHT=466
basket=Actor('basket.png',(350,380))
mango=Actor('mango.png',(0,0))
strawberry=Actor('strawberry.png',(0,0))
kiwi=Actor('kiwi.png',(0,0))
cherry=Actor('cherry.png',(0,0))
def draw():
    screen.blit('fruitbackground.jpg',(0,0))
    basket.draw()
    mango.draw()
    kiwi.draw()
    strawberry.draw()
    cherry.draw()
def update():
    if keyboard.a:
        basket.x-=5
    if keyboard.d:
        basket.x+=5
    if mango.y>466:
        mango.pos=(random.randint(0,WIDTH),30)
    if cherry.y>466:
        cherry.pos=(random.randint(0,WIDTH),30)
    if kiwi.y>466:
        kiwi.pos=(random.randint(0,WIDTH),30)
    if strawberry.y>466:
        strawberry.pos=(random.randint(0,WIDTH),30)
    if mango.colliderect(basket):
        mango.pos=(random.randint(0,WIDTH),30)
    if cherry.colliderect(basket):
        cherry.pos=(random.randint(0,WIDTH),30)
    if strawberry.colliderect(basket):
        strawberry.pos=(random.randint(0,WIDTH),30)
    if kiwi.colliderect(basket):
        kiwi.pos=(random.randint(0,WIDTH),30)

def mangodrop():
    mango.y+=9
    clock.schedule(mangodrop,0.1)
def cherrydrop():
    cherry.y+=8
    clock.schedule(cherrydrop,0.1)
def strawberrydrop():
    strawberry.y+=11
    clock.schedule(strawberrydrop,0.1)
def kiwidrop():
    kiwi.y+=6
    clock.schedule(kiwidrop,0.1)
mangodrop()
kiwidrop()
cherrydrop()
strawberrydrop()

pgzrun.go()
    
