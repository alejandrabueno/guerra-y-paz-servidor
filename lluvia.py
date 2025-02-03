import pygame
import random

# Configuración de la pantalla escalada
ESCALA = 0.10  # Factor de escala para reducir la resolución
ANCHO = int(800 * ESCALA)  # Escalar ancho
ALTO = int(4800 * ESCALA)  # Escalar alto
COLUMNAS = 4  # Número de columnas
ANCHO_COLUMNA = ANCHO // COLUMNAS  # Ancho de cada columna
TAMANIO_LETRA = int(ANCHO_COLUMNA * 0.9)  # Tamaño de letra ajustado al 90% del ancho de columna
ESPACIO_ENTRE_LETRAS = int(TAMANIO_LETRA * 0.6)  # Espacio entre letras
FPS = 60  # Velocidad de fotogramas

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Cascada de Letras y Frases")
font_letras = pygame.font.Font(None, int(TAMANIO_LETRA * 0.8))  # Letras ligeramente más grandes
font_frases = font_letras  # Usar la misma tipografía para frases y letras

# Colores
NEGRO = (0, 0, 0)
AZUL = (0, 128, 255)
AZUL_BRILLANTE = (0, 150, 255)

# Lista de frases originales
frases_originales = [
    "LA PAZ ES UN DERECHO",
    "ARMONÍA UNIVERSAL",
    "AMOR Y PAZ",
    "RESPETO MUTUO",
    "PAZ ES JUSTICIA",
    "UNIDAD GLOBAL",
    "EQUILIBRIO EMOCIONAL",
    "ESPERANZA ETERNA",
    "SOLIDARIDAD HUMANA",
    "FELICIDAD COMPARTIDA"
]

# Invertir cada frase (tanto letras como palabras)
frases_invertidas = [" ".join(palabra[::-1] for palabra in frase.split()[::-1]) for frase in frases_originales]

# Clase para manejar frases completas
class Frase:
    def __init__(self, texto, columna):
        self.texto = texto
        self.x = columna * ANCHO_COLUMNA + ANCHO_COLUMNA // 2  # Centrado en la columna
        self.y = -len(texto) * ESPACIO_ENTRE_LETRAS  # Comienza fuera de la pantalla
        self.alpha = 255  # Opacidad inicial
        self.columna = columna  # Columna asignada

    def mover(self):
        self.y += 3  # Velocidad más lenta ajustada
        if self.y > (ALTO * 3) // 4:  # Reducir opacidad en el último cuarto de la pantalla
            self.alpha = max(0, 255 - int(((self.y - (ALTO * 3) // 4) / (ALTO // 4)) * 255))

    def dibujar(self):
        for i, letra in enumerate(self.texto):  # Dibuja cada letra en posición vertical
            texto_surface = font_frases.render(letra, True, AZUL_BRILLANTE)
            texto_surface.set_alpha(self.alpha)  # Ajustar opacidad
            screen.blit(texto_surface, (self.x - texto_surface.get_width() // 2, self.y + i * ESPACIO_ENTRE_LETRAS))

    def fuera_de_pantalla(self):
        return self.y > ALTO or self.alpha <= 0  # Sale de pantalla o desaparece completamente

# Lista de frases activas
frases_activas = []
espacios_ocupados = [False] * COLUMNAS  # Control de las columnas disponibles

# Clase para las letras que caen
class Letra:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.caracter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_.:;,¨Ç»«ˆ±*\"´¨ºª")
        self.velocidad = random.randint(2, 5)
        self.alpha = random.randint(100, 255)

    def mover(self):
        self.y += self.velocidad
        if self.y > (ALTO * 3) // 4:  # Reducir opacidad en el último cuarto de la pantalla
            self.alpha = max(0, 255 - int(((self.y - (ALTO * 3) // 4) / (ALTO // 4)) * 255))
        if self.y > ALTO:
            self.y = -random.randint(0, 50)
            self.caracter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_.:;,¨Ç»«ˆ±*\"´¨ºª")
            self.velocidad = random.randint(2, 5)
            self.alpha = random.randint(100, 255)

    def dibujar(self):
        letra_surface = font_letras.render(self.caracter, True, AZUL)
        letra_surface.set_alpha(self.alpha)
        screen.blit(letra_surface, (self.x, self.y))

# Crear un conjunto de letras iniciales
letras = []
for columna in range(COLUMNAS):
    for _ in range(50):  # Número de letras iniciales por columna
        x = columna * ANCHO_COLUMNA + random.randint(0, ANCHO_COLUMNA - 10)
        y = random.randint(-ALTO, 0)
        letras.append(Letra(x, y))

# Bucle principal
reloj = pygame.time.Clock()
corriendo = True
frame_counter = 0  # Contador de cuadros para espaciar las frases
while corriendo:
    screen.fill(NEGRO)  # Fondo negro

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Dibujar las frases activas
    if len(frases_activas) < COLUMNAS and frame_counter % 120 == 0:  # Espaciar la aparición de frases
        columna = random.randint(0, COLUMNAS - 1)
        if not espacios_ocupados[columna]:
            nueva_frase = Frase(random.choice(frases_invertidas), columna)
            frases_activas.append(nueva_frase)
            espacios_ocupados[columna] = True

    for frase in frases_activas[:]:
        frase.mover()
        frase.dibujar()
        if frase.fuera_de_pantalla():
            espacios_ocupados[frase.columna] = False
            frases_activas.remove(frase)

    # Actualizar y dibujar las letras
    for letra in letras:
        letra.mover()
        letra.dibujar()

    # Actualizar la pantalla
    pygame.display.flip()
    reloj.tick(FPS)
    frame_counter += 1

pygame.quit()









