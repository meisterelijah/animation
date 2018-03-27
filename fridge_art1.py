
import pygame
import random
import math

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Pyramid"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
RED = (255, 0, 0)
GREEN = (0, 125, 0)
BLUE = (91, 154, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 242, 0)
DUST = (255, 125, 0)
SAND = (255, 213, 61)
BURST = (246, 255, 0)
GRAY = (177, 178, 162)

#music
run_music = pygame.mixer.music.load('bleach.ogg')
pygame.mixer.music.play(-1)

#object

object1 = [25,25,25,25]
object1_img = pygame.image.load('rip.png')
vel = [0, 0]
object1_speed = 5

#setting
stormy = True


def draw_clouds(loc):
    x = loc[0]
    y = loc[1]

    pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])

num_clouds = 20
clouds = []
for i in range(num_clouds):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 150)
    loc = [x, y]
    clouds.append(loc)


    


def draw_raindrop(drop):
    rect = drop[:4]
    pygame.draw.ellipse(screen, DARK_BLUE, rect)


            
# make rain

rain = []
for i in range (2000):
    x = random.randrange(0,500)
    y = random.randrange(50,2000)
    r = random.randrange(2,3)
    n = [x, y, r, r]
    rain.append(n)

# make clouds


    
# make grass

def draw_grass():
    pygame.draw.rect(screen, SAND, [50, 100, 300, 200])
    pygame.draw.rect(screen, YELLOW, [50, 100, 300, 200])

# make fence

def draw_fence(y) :
    
    y = 520
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5], [x+10, y+40], [x, y+40],[x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 530], [800, 530], 5)
    pygame.draw.line(screen, WHITE, [0, 550], [800, 550], 5)

# make house 
def house():
    pygame.draw.rect(screen, SAND, [1, 500, 800, 100])
    pygame.draw.line(screen, SAND, [1, 1], [1,1], 10)
    pygame.draw.rect(screen, DUST, [1, 480, 500, 70])
    pygame.draw.rect(screen, DUST, [1, 410, 400, 70])
    pygame.draw.rect(screen, DUST, [1, 340, 300, 70])
    pygame.draw.rect(screen, DUST, [1, 270, 200, 70])
    pygame.draw.rect(screen, DUST, [1, 200, 100, 70]) 
    pygame.draw.polygon(screen,DUST,[[0,125], [-140,200], [100,200]])  
        
   
# Game loop
done = False


while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                daytime = not daytime
            elif event.key == pygame.K_l:
                lights_on = not lights_on
                # constants keys
    
    pressed = pygame.key.get_pressed()

    
    up = pressed[pygame.K_UP]
    down = pressed[pygame.K_DOWN]
    left = pressed[pygame.K_LEFT]
    right = pressed[pygame.K_RIGHT]

    if left:
        vel[0] = -object1_speed
    elif right:
        vel[0] = object1_speed
    else:
        vel[0] = 0

    if up:
        vel[1] = -object1_speed
        
    elif down:
        vel[1] = object1_speed
    else:
        vel[1] = 0


    object1[0] += vel[0]
    object1[1] += vel[1]
    

             
    lightning_timer = 0


    daytime = True
    lights_on = False

    # Game logic
    for c in clouds:
        c[0] += 2

        if c[0] > 900:
            c[0] = random.randrange(-900, 0)
            c[1] = random.randrange(50, 200)

    for n in rain:
        n[1] += 5
        n[0] += 0

        if n[1] > 550:
            n[0] = random.randrange(-100, 800)
            n[1] = random.randrange(-10, 1000)

    ''' flash lighting '''
    if stormy:        
        if random.randrange(0, 150) == 0:
            lightning_timer = 5
        else:
            lightning_timer -= 1
            
    ''' set sky color '''
    if daytime:
        sky = BLUE
    else:
        sky = BLACK

    ''' set window color (if there was a house)'''
    if lights_on:
        window_color = YELLOW
    else:
        window_color = WHITE
        

        
            
    # Drawing code
    ''' sky '''
    if lightning_timer > 0:
        screen.fill(BURST)
    else:
        screen.fill(GRAY)
    ''' sun '''
    pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])
    house()
    draw_fence(100)      
    for n in rain:
        pygame.draw.ellipse(screen, BLUE, n)
    for loc in clouds:
        draw_clouds(loc)

    
    loc2 = object1[:2]
    screen.blit(object1_img,loc2)
       


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()

