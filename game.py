import pgzrun
import random
WIDTH=700
HEIGHT=438
duck=Actor('character.png')
duck.pos=(random.randint(0,WIDTH-100),random.randint(0,HEIGHT-100))
sponge=Actor('character2.png')
sponge.pos=(375,275)
def draw():
    screen.blit('background.jpg',(0,0))
    duck.draw()
    sponge.draw()
def randompos():
    duck.pos=(random.randint(0,WIDTH-100),random.randint(0,HEIGHT-100))
    clock.schedule(randompos,2)
def on_mouse_down(pos):
     sponge.pos=pos
randompos()
pgzrun.go()
