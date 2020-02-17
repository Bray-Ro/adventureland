import pygame, sys
from pygame.locals import *
from random import randint
import time
import random
import subprocess
import mods
pygame.init()

player_x = 50
player_y = 50
DISPLAY=pygame.display.set_mode((500,400),0,32)
WHITE=(255,255,255)
BLUE=(0,0,255)
GREEN=(0, 200, 0)
BROWN=(156,102,31)
#y = 350, x=450
tree_x =  randint(1, 18) * 25
tree_y = randint(1, 14) * 25
backcol = GREEN
DISPLAY.fill(backcol)
done = False
inventory = []
title_font = pygame.font.Font(pygame.font.get_default_font(), 30)
font = pygame.font.Font(pygame.font.get_default_font(), 12)
mods.mod_blocks()
# now print the text
text = font.render('inventory: ' + ', '.join(inventory), False, (0, 0, 0))
DISPLAY.blit(text, dest=(0,0))
player = pygame.draw.rect(DISPLAY,BLUE,(player_x,player_y,50,50))
tree = pygame.draw.rect(DISPLAY,BROWN,(tree_x, tree_y,50, 50))
def main():
    global tree_x
    global tree_y
    global player_x 
    global player_y
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        pygame.draw.rect(DISPLAY,backcol,(player_x,player_y,50,50))
        player_y -= 25
        player = pygame.draw.rect(DISPLAY,BLUE,(player_x,player_y,50,50))
        
    if pressed[pygame.K_DOWN]:
        pygame.draw.rect(DISPLAY,backcol,(player_x,player_y,50,50))
        player_y += 25
        print(player_y)
        player = pygame.draw.rect(DISPLAY,BLUE,(player_x,player_y,50,50)) 
        
    if pressed[pygame.K_LEFT]:
        player = pygame.draw.rect(DISPLAY,backcol,(player_x,player_y,50,50))
        player_x -= 25
        player = pygame.draw.rect(DISPLAY,BLUE,(player_x,player_y,50,50)) 
        
    if pressed[pygame.K_RIGHT]:
        pygame.draw.rect(DISPLAY,backcol,(player_x,player_y,50,50))
        player_x += 25
        print(player_x)
        player = pygame.draw.rect(DISPLAY,BLUE,(player_x,player_y,50,50))
    mods.collision_checks()
    if player_x == tree_x and player_y == tree_y:
        if len(inventory) < 12:
            inventory.append('wood')
        else:
            inventory_full()
        # now print the text
        text = font.render('inventory: ' + ', '.join(inventory), False, (0, 0, 0))
        DISPLAY.blit(text, dest=(0,0))   
        tree_x =  randint(1, 18) * 25
        tree_y = randint(1, 14) * 25 

        tree = pygame.draw.rect(DISPLAY,BROWN,(tree_x, tree_y,50, 50))
    pygame.event.pump()
def inventory_full():
    text2 = title_font.render('inventory full!', False, (0, 0, 0))
    DISPLAY.blit(text2, dest=(175,100))   
    time.sleep(1)
    text2 = title_font.render('', False, (0, 0, 0))
    DISPLAY.blit(text2, dest=(175,100))   


while True:

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
    time.sleep(0.125)
    main()