import pgzrun
import random
WIDTH=700
HEIGHT=466
basket=Actor('basket.png',(350,380))
fruits_images=['kiwi.png','strawberry.png','cherry.png','mango.png']
fruits=[]
score=0
def new_fruit():
    fruit=Actor(random.choice(fruits_images))
    fruit.pos=(random.randint(0,WIDTH),0)
    fruits.append(fruit)
    clock.schedule(new_fruit,random.randint(1,3))

def draw():
    screen.blit('fruitbackground.jpg',(0,0))
    if score<0:
        screen.blit('endscreen.png',(175,100))
        return
    basket.draw()
    screen.draw.text('score: '+str(score),(20,20))
    for fruit in fruits:
        fruit.draw()
def update():
    global score
    if score<0:
        return
    if keyboard.a:
        basket.x-=5
    if keyboard.d:
        basket.x+=5
    for fruit in fruits:
        fruit.y+=4
        if fruit.colliderect(basket):
            fruits.remove(fruit)
            score+=1
        if fruit.y>466:
            fruits.remove(fruit)
            score-=1



new_fruit()
pgzrun.go()