import pygame

#########################################################
# Configuraciones
#########################################################

# Ancho de la pantalla
ALTO = 600
ANCHO = 800

ALTO_PALA = 100
ANCHO_PALA = 10
MARGEN = 30
VEL_JUGADOR = 1

TAM_PELOTA = 8

COLOR_FONDO = (0, 0, 0)
COLOR_OBJETOS = (200, 200, 200)

#########################################################

# pinto la pelota
# xp = (ANCHO - TAM_PELOTA) / 2
# yp = (ALTO - TAM_PELOTA) / 2
# pelota = pygame.Rect(xp, yp, TAM_PELOTA, TAM_PELOTA)
# pygame.draw.rect(self.pantalla, COLOR_OBJETOS, pelota)

# Qué debe tener la pelota
# - un constructor
# - método que la mueva
# - atributos para el movimiento ?
# - ¿puntuación?


class Pintable(pygame.Rect):

    def __init__(self, x, y, ancho, alto):
        super().__init__(x, y, ancho, alto)

    def pintar(self, pantalla):
        pygame.draw.rect(pantalla, COLOR_OBJETOS, self)


class Pelota(Pintable):
    # atributos
    tam_pelota = TAM_PELOTA
    # mov??

    # métodos
    def __init__(self):
        x = (ANCHO - self.tam_pelota) / 2
        y = (ALTO - self.tam_pelota) / 2
        super().__init__(x, y, self.tam_pelota, self.tam_pelota)

    def mover(self):
        pass


class Jugador(Pintable):

    def __init__(self, x):
        y = (ALTO - ALTO_PALA) / 2
        super().__init__(x, y, ANCHO_PALA, ALTO_PALA)

    def subir(self):
        self.y -= VEL_JUGADOR

    def bajar(self):
        self.y += VEL_JUGADOR


class Pong:

    """
    J1: 
        - Arriba: A
        - Abajo: Z
    J2:
        - Arriba: flecha arriba
        - Abajo: flecha abajo
    """

    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        self.pelota = Pelota()
        self.jugador1 = Jugador(MARGEN)
        self.jugador2 = Jugador(ANCHO - MARGEN - ANCHO_PALA)

    def jugar(self):
        salir = False

        while not salir:
            # bucle principal (main loop)

            # capturar los eventos
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    print('Has pulsado el botón de cerrar la ventana')
                    salir = True
                if evento.type == pygame.KEYUP and evento.key == pygame.K_ESCAPE:
                    print('Has "soltado" la tecla ESC')
                    salir = True

            estado_teclas = pygame.key.get_pressed()
            if estado_teclas[pygame.K_a]:
                self.jugador1.subir()
            if estado_teclas[pygame.K_z]:
                self.jugador1.bajar()
            if estado_teclas[pygame.K_UP]:
                self.jugador2.subir()
            if estado_teclas[pygame.K_DOWN]:
                self.jugador2.bajar()

            # renderizar mis objetos
            # 1. borrar la pantalla
            pygame.draw.rect(
                self.pantalla,
                COLOR_FONDO,
                ((0, 0), (ANCHO, ALTO)))

            # 2. pintar los objetos en la posición correspondiente

            # pinto los jugadores
            self.jugador1.pintar(self.pantalla)
            self.jugador2.pintar(self.pantalla)

            # pinto la red
            self.pintar_red()

            # pinto la pelota
            self.pelota.pintar(self.pantalla)

            # 3. mostrar los cambios en la pantalla
            pygame.display.flip()

        pygame.quit()

    def pintar_red(self):
        """Pinta la red en la pantalla"""
        # está centrada horizontalmente

        # es una línea discontinua que:
        # son "muchas" líneas de tamaño `tramo_pintado`
        # con una separación entre ellas `tramo_vacio`
        # la vamos a pintar del color `COLOR_OBJETOS`
        # de un ancho `ancho_red`
        # ocupa todo el alto de la pantalla

        pos_x = ANCHO / 2 - 1
        tramo_pintado = 20
        tramo_vacio = 15
        ancho_red = 4

        # bucle:
        # 1. dónde empiezo: pos_y = 0
        # 2. dónde termino: pos_y = ALTO
        # 3. cómo voy de un paso al siguiente: incrementar y en tramo_pintado + tramo_vacio
        # 4. pintar la línea con pygame.draw.line()

        for pos_y in range(0, ALTO, tramo_pintado+tramo_vacio):
            pygame.draw.line(
                self.pantalla,
                COLOR_OBJETOS,
                (pos_x, pos_y),
                (pos_x, pos_y+tramo_pintado),
                ancho_red
            )


juego = Pong()
juego.jugar()