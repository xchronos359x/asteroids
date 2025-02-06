# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
    
        while True:
            pygame.Surface.fill(screen,(0,0,0))
            pygame.display.flip()
    
if __name__ == "__main__":
    main()
