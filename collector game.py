import pgzrun 
import random
WIDTH=700
HEIGHT=438
score=0
actor1=Actor('character2.png')
actor1.pos=(375,275)
actor2=Actor('character1.png')
actor2.pos=(475,375)
def draw():
    screen.blit('background.jpg',(0,0))
    actor1.draw()
    actor2.draw()
    screen.draw.text('Score: '+str(score),(10,10))
def randompos():
    actor2.pos=(random.randint(0,WIDTH-100),random.randint(0,HEIGHT-100))
    clock.schedule(randompos,2)
def update():
    global score
    if keyboard.d:
        actor1.x+=3
    elif keyboard.a:
        actor1.x-=3
    elif keyboard.w:
        actor1.y-=3
    elif keyboard.s:
        actor1.y+=3
    if actor1.colliderect(actor2):
        score+=1
        actor2.pos=(random.randint(0,WIDTH-100),random.randint(0,HEIGHT-100))


randompos()
pgzrun.go()