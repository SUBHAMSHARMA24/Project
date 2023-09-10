import pygame
pygame.init() #intialisation of pygame

SIZE=WIDTH, HEIGHT=1000,600
SCREEN=pygame.display.set_mode(SIZE)

#RGB color code
WHITE=255,255,255
RED=255,0,0
BLUE=0,0,255
BLACK=0,0,0

SCREEN.fill(WHITE)
circle_x=50
circle_y=50
radius=50
SPEED_X=0.5
SPEED_Y=0.5
while True:
    eventList= pygame.event.get()
    for event in eventList:
        #print(event)
        if event.type==pygame.QUIT:
            #Quit pygame
            pygame.quit()
            #Quit Python
            quit()

    SCREEN.fill(WHITE)
    pygame.draw.circle(SCREEN, BLUE,[circle_x,circle_y],radius)
    circle_x +=SPEED_X  #making new circle at 0.5 speed looks like animation
    circle_y +=SPEED_Y

    if circle_x > WIDTH - radius:
        SPEED_X = -0.5
    elif circle_y > HEIGHT - radius:
        SPEED_Y = -0.5
    elif circle_x < radius:
        SPEED_X = 0.5
    elif circle_y < radius:
        SPEED_Y = 0.5

    #updates the Screen
    pygame.display.flip()