from random import randint, choice

import pygame


"""
1. El contador empieza en (0,0) (es decir, mantiene dos puntuaciones, una para cada jugador)

2. Siempre aumenta de uno en uno
3. Hay que aumentar un punto para el jugador "contrario"
   al lado del campo por el que sale la pelota.
   A esto lo llamamos "condición de punto".
4. Cuando la puntuación de un jugador alcanza 9 ha ganado la partida
5. Hay que pintarlo en la parte superior de la pantalla

------

- Clase Marcador
- Tiene un atributo tipo lista / un atributo por jugador para mantener la puntuación
- Al inicio, ese atributo tiene los valores [0, 0]
- Tiene un método incrementar que aumenta el marcador para el jugador que gana un punto
  (y siempre lo hace de uno en uno)
- Tiene un método pintar para hacerlo visible en la pantalla
- Tiene un método quien_gana para comprobar si alguno de los dos jugadores ha ganado
  (esto pasa cuando uno de los dos alcanza una puntuación de 9)
- Tiene un método reset que pone el marcador en (0,0)
"""

#########################################################
# Configuraciones
#########################################################

# Ancho de la pantalla
ALTO = 600
ANCHO = 800

FPS = 80

ALTO_PALA = 100
ANCHO_PALA = 10
MARGEN = 30
VEL_JUGADOR = 5

TAM_PELOTA = 8
VEL_PELOTA = 5

COLOR_FONDO = (0, 0, 0)
COLOR_OBJETOS = (200, 200, 200)

"""
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
"""


class Pintable(pygame.Rect):

    def __init__(self, x, y, ancho, alto):
        super().__init__(x, y, ancho, alto)

    def pintar(self, pantalla):
        pygame.draw.rect(pantalla, COLOR_OBJETOS, self)


class Pelota(Pintable):
    tam_pelota = TAM_PELOTA

    def __init__(self):
        super().__init__(0, 0, self.tam_pelota, self.tam_pelota)

        haciaIzquierda = choice([True, False])
        self.reiniciar(haciaIzquierda)

    def mover(self):
        limite_sup = 0
        limite_inf = ALTO - self.tam_pelota

        self.x += self.vel_x
        self.y += self.vel_y

        if self.y <= limite_sup or self.y >= limite_inf:
            self.vel_y = -self.vel_y

        punto_para = 0
        if self.x <= 0:
            self.reiniciar(True)
            punto_para = 2
        if self.x >= (ANCHO - self.tam_pelota):
            self.reiniciar(False)
            punto_para = 1

        return punto_para

    def reiniciar(self, irIzquierda):
        self.x = (ANCHO - self.tam_pelota) / 2
        self.y = (ALTO - self.tam_pelota) / 2
        self.vel_y = randint(-VEL_PELOTA, VEL_PELOTA)
        self.vel_x = randint(1, VEL_PELOTA)

        if irIzquierda:
            self.vel_x = -self.vel_x

    def parar(self):
        self.vel_x = 0
        self.vel_y = 0


class Jugador(Pintable):

    def __init__(self, x):
        y = (ALTO - ALTO_PALA) / 2
        super().__init__(x, y, ANCHO_PALA, ALTO_PALA)

    def subir(self):

        limite = 0

        self.y -= VEL_JUGADOR
        if self.y < limite:
            self.y = limite

    def bajar(self):

        limite = ALTO - ALTO_PALA

        self.y += VEL_JUGADOR
        if self.y > limite:
            self.y = limite


class Marcador:
    """
        - Tiene un atributo tipo lista / un atributo por jugador para mantener la puntuación
        - Al inicio, ese atributo tiene los valores [0, 0]
        - Tiene un método reset que pone el marcador en (0,0)
        - Tiene un método incrementar que aumenta el marcador para el jugador que gana un punto
        (y siempre lo hace de uno en uno)

    - Tiene un método quien_gana para comprobar si alguno de los dos jugadores ha ganado
    (esto pasa cuando uno de los dos alcanza una puntuación de 9)


    - Tiene un método pintar para hacerlo visible en la pantalla
    """

    def __init__(self):
        self.reset()

    def reset(self):
        self.puntuacion = [0, 0]

    def incrementar(self, jugador: int):
        if jugador in (1, 2):
            self.puntuacion[jugador-1] += 1

    def quien_gana(self):

        ganador = 0

        if self.puntuacion[0] == 9:
            ganador = 1
        elif self.puntuacion[1] == 9:
            ganador = 2

        return ganador

    def pintar(self):
        print(f'Marcador: ({self.puntuacion[0]}, {self.puntuacion[1]})')


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
        self.reloj = pygame.time.Clock()

        self.pelota = Pelota()
        self.jugador1 = Jugador(MARGEN)
        self.jugador2 = Jugador(ANCHO - MARGEN - ANCHO_PALA)
        self.marcador = Marcador()

    def jugar(self):
        salir = False
        self.marcador.pintar()

        while not salir:
            # bucle principal (main loop)
            self.reloj.tick(FPS)

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
            # pygame.draw.rect(self.pantalla,COLOR_FONDO,((0, 0), (ANCHO, ALTO)))
            self.pantalla.fill(COLOR_FONDO)

            # 2. pintar los objetos en la posición correspondiente

            # pinto los jugadores
            self.jugador1.pintar(self.pantalla)
            self.jugador2.pintar(self.pantalla)

            # pinto la red
            self.pintar_red()

            # pinto la pelota
            punto_para = self.pelota.mover()
            if punto_para in (1, 2):
                self.marcador.incrementar(punto_para)
                ganador = self.marcador.quien_gana()
                if ganador > 0:
                    print(f'El jugador {ganador} ha ganado la partida')
                    self.pelota.parar()
                self.marcador.pintar()

            self.pelota.pintar(self.pantalla)

            if self.pelota.colliderect(self.jugador1):
                self.pelota.vel_x = randint(1, VEL_PELOTA)
                self.pelota.vel_y = randint(-VEL_PELOTA, VEL_PELOTA)

            if self.pelota.colliderect(self.jugador2):
                self.pelota.vel_x = randint(-VEL_PELOTA, -1)
                self.pelota.vel_y = randint(-VEL_PELOTA, VEL_PELOTA)

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


if __name__ == '__main__':
    print('Invocado desde la línea de comandos')
    juego = Pong()
    juego.jugar()
else:
    print('Invocado como módulo', __name__)