import pygame

pygame.init()
pantalla = pygame.display.set_mode((600, 600))
reloj = pygame.time.Clock()

salir = False
while not salir:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            print('Has pulsado el botón de cerrar la ventana')
            salir = True

    pantalla.fill((0, 0, 100))

    r1 = pygame.rect.Rect(50, 50, 100, 100)
    pygame.draw.rect(pantalla, (100, 100, 0), r1)

    r2 = pygame.rect.Rect(100, 100, 100, 100)
    pygame.draw.rect(pantalla, (0, 100, 100), r2)

    print('Se solapan?', r1.colliderect(r2))

    pygame.display.flip()
    reloj.tick(1)


pygame.quit()