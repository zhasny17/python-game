import time
import pygame


pygame.init()

screen = pygame.display.set_mode([640, 480])

pygame.display.set_caption("The best game in the word!")

screen.fill([0, 0, 0])

pygame.display.flip()

time.sleep(1)
