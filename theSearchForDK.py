import pygame
from random import *

windowX = 240
windowY = 70
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (windowX,windowY)
os.chdir("photos")

pygame.init()

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

bigfont = pygame.font.SysFont("david", 32)   #informalroman, bookantiqua, daivd

house_files = ["Stairs Top.jpg", "More Stairs.jpg", "More More Stairs.jpg",
               "More More More Stairs.jpg", "Finally Less Stairs.jpg", "Bottom of stairs.jpg",
               "TV side.jpg", "Music room side.jpg", "Music room side WITH DK.jpg",
               "Left of stairs.jpg", "Towards Bathroom.jpg", "Bathroom side Door.jpg", "Bathroom.jpg",
               "Bathroom WITH DK.jpg", "Rocking Chair.jpg", "Rocking Chair WITH DK.jpg",
               "Lesser TV room.jpg", "TV room.jpg", "More TV room.jpg", "MORE More TV room.jpg",
               "MOOORE More TV room.jpg", "Couches.jpg", "Couches WITH DK.jpg"]
arrow_files = ["arrowRight.png"]

def loadImages (fileList, aList):
    for i in range(0, len(fileList)):
        temp = pygame.image.load(fileList[i])
        aList.append(temp)

house = []
arrow = []

loadImages(house_files, house)
loadImages(arrow_files, arrow)

arrow[0] = pygame.transform.scale(arrow[0], (150, 114))
arrow[0] = pygame.transform.rotate(arrow[0], 90)
arrow.append(pygame.transform.rotate(arrow[0], 90))
arrow.append(pygame.transform.rotate(arrow[1], 90))
arrow.append(pygame.transform.rotate(arrow[2], 90))

arrowCoords = [(365, 15), (10, 250), (365, 445), (640, 250)]

room0To5 = [-1, -1, -1, -1]
room6 = [-1, 9, -1, 7]
room7 = [-1, 6, -1, -1]
room8 = [-1, 6, -1, -1]
room9 = [16, -1, -1, 6]
room10 = [11, -1, -1, 16]
room11 = [-1, 12, 10, 14]
room12 = [-1, -1, 11, 11]
room13 = [-1, -1, 11, 11]
room14 = [-1, 11, 11, -1]
room15 = [-1, 11, 11, -1]
room16 = [17, 10, 9, -1]
room17 = [18, -1, 16, -1]
room18 = [-1, 19, 17, -1]
room19 = [-1, 20, -1, 18]
room20 = [-1, 21, -1, 19]
room21 = [-1, -1, -1, 20]
room22 = [-1, -1, -1, 20]

donkeyPossible = [8, 13, 15, 22] #The possible rooms DK can be in
donkeyRoom = donkeyPossible[randint(0, 3)] #Picks one at random
#print donkeyRoom
if donkeyRoom == 8: room6 = [-1, 9, -1, 8]
elif donkeyRoom == 13: room11 = [-1, 13, 10, 14]
elif donkeyRoom == 15: room11 = [-1, 12, 10, 15]
else: room20 = [-1, 22, -1, 19]

connections = [room0To5, room0To5, room0To5, room0To5, room0To5, room0To5, room6, room7, room8, room9, room10,
               room11, room12, room13, room14, room15, room16, room17, room18, room19, room20, room21, room22]

curRoom = 0


# Set the height and width of the screen
size = [800, 600]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("DK GAME")

screen.fill(WHITE)

clock = pygame.time.Clock()
done = False
enter = False
pressed = False
stairCount = 0
won = False
endCount = 0

while not done and not won:
   
    clock.tick(60)
    screen.fill(WHITE)
        
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

    #Stores all the keys values into an array called key
    key = pygame.key.get_pressed()

    if curRoom > 0:
        if key[pygame.K_w] and not pressed and connections[curRoom][0] != -1:
            pressed = True
            curRoom = connections[curRoom][0]

        if key[pygame.K_a] and not pressed and connections[curRoom][1] != -1:
            pressed = True
            curRoom = connections[curRoom][1]

        if key[pygame.K_s] and not pressed and connections[curRoom][2] != -1:
            pressed = True
            curRoom = connections[curRoom][2]

        if key[pygame.K_d] and not pressed and connections[curRoom][3] != -1:
            pressed = True
            curRoom = connections[curRoom][3]
    else:
        if key[pygame.K_w]: enter = True

    if not key[pygame.K_w] and not key[pygame.K_a] and not key[pygame.K_s] and not key[pygame.K_d]:
        pressed = False

    if enter:
        if stairCount >= 20:
            curRoom += 1
            stairCount = 0
        stairCount += 1
        if curRoom >= 6:
            enter = False

        #Checks if mouse is pressed
    mouseState = pygame.mouse.get_pressed()

    #MOUSE STUFFS
    #If the mouse was just pressed
    if mouseState[0] and released:
        released = False

        #Get the position of the mouse
        mousePos = pygame.mouse.get_pos()
        #print mousePos

        if mousePos[0] > 272 and mousePos[0] < 307 and mousePos[1] > 410 and mousePos[1] < 458 and curRoom == 8:
            won = True
        if mousePos[0] > 358 and mousePos[0] < 380 and mousePos[1] > 294 and mousePos[1] < 311 and curRoom == 13:
            won = True
        if mousePos[0] > 459 and mousePos[0] < 481 and mousePos[1] > 228 and mousePos[1] < 255 and curRoom == 15:
            won = True
        if mousePos[0] > 308 and mousePos[0] < 329 and mousePos[1] > 242 and mousePos[1] < 261 and curRoom == 22:
            won = True


    #If the mouse is not being clicked
    if not mouseState[0]:
        released = True

    screen.blit(house[curRoom], (0, 0))

    for i in range(4):
        if connections[curRoom][i] != -1:
            screen.blit(arrow[i], arrowCoords[i])



    pygame.display.flip()

screen.fill(WHITE)
screen.blit(bigfont.render("Winner!", 1, BLACK), (340, 270))
pygame.display.flip()

while endCount < 200 and not done:
    clock.tick(60)

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

    endCount += 1
    #print endCount

pygame.quit()
