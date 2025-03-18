import pygame

pygame.init()
pantalla = pygame.display.set_mode(600,600)
salir = False
while not salir:
    pygame.display.flip()

pygame.quit()