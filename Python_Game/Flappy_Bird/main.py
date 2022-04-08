import pygame, sys # ctrl+F5 to check
pygame.init()

# Step 1: Create window game
screen = pygame.display.set_mode((432, 768)) # x2 width, height of background image game

# Step 2: Create loop event of game 
while True:
    # get all events of game
    for event in pygame.event.get():
        # when user click quit button
        if event.type == pygame.QUIT:
            pygame.quit() # close this window of game
            sys.exit() # exit system of game (err: pygame.error: video system not initialized)

    pygame.display.update() # the screen always update when loop event finish 
