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
rect_x=0
rect_y=0
rect_w=50
rect_h=50

move_x=0
move_y=0

while True:
    eventList= pygame.event.get()
    for event in eventList:
        #print(event)
        if event.type==pygame.QUIT:
            #Quit pygame
            pygame.quit()
            #Quit Python
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x =0.5
            elif event.key ==pygame.K_LEFT:
                move_x= -0.5
        else:
            move_x =0

    SCREEN.fill(WHITE)
    pygame.draw.rect(SCREEN, BLUE,[rect_x,rect_y,rect_w,rect_h])
    rect_x += move_x;
    #updates the Screen
    pygame.display.flip()