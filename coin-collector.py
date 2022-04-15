import pgzrun
from random import randint

WIDTH = 800

HEIGHT = 800

score = 0

game_over = False

fox = Actor("fox")
fox.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200

def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color = "black", topleft = (10, 10))

    if game_over:
        screen.fill("black")
        screen.draw.text("Final Score: " + str(score), color = "white", topleft = (300, 300), fontsize = 40)

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def time_up():
    global game_over
    game_over = True

def update():

    global score
    
    if keyboard.left:
        fox.x -= 6
    elif keyboard.right:
        fox.x += 6
    elif keyboard.up:
        fox.y -= 6
    elif keyboard.down:
        fox.y += 6

    coin_collected = fox.colliderect(coin)

    if coin_collected:
        score += 10
        place_coin()

clock.schedule(time_up, 15.0)

place_coin()

pgzrun.go()
