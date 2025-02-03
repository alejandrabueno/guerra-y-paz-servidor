import pygame
import random
import math

# Configuración de la pantalla escalada
ESCALA = 0.25  # Factor de escala para reducir la resolución
ANCHO = int(800 * ESCALA)  # Escalar ancho
ALTO = int(4800 * ESCALA)  # Escalar alto
COLUMNAS = 4  # Número de columnas
ANCHO_COLUMNA = ANCHO // COLUMNAS  # Ancho de cada columna
FRASES_SIMULTANEAS = COLUMNAS  # Máximo de frases simultáneamente (una por columna)
TAMANIO_LETRA = int(ANCHO_COLUMNA * 0.9)  # Tamaño de letra ajustado al 90% del ancho de columna
ESPACIO_ENTRE_LETRAS = int(TAMANIO_LETRA * 0.6)  # Reducir el espacio entre letras (60% del tamaño de letra)
FPS = 60  # Velocidad de fotogramas

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Instalación de Paz con Fondo Abstracto")
font = pygame.font.Font(None, TAMANIO_LETRA)

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Lista de frases originales
frases_originales = [
    "La paz es un derecho",
    "Armonía universal",
    "Amor y paz",
    "Respeto mutuo",
    "Paz es justicia",
    "Unidad global",
    "Equilibrio emocional",
    "Esperanza eterna",
    "Solidaridad humana",
    "Felicidad compartida"
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
        self.y += 5  # Velocidad fija ajustada (más lenta)
        if self.y > ALTO - len(self.texto) * ESPACIO_ENTRE_LETRAS:
            self.alpha -= 5  # Desvanece al llegar cerca del final

    def dibujar(self):
        for i, letra in enumerate(self.texto):  # Dibuja cada letra en posición vertical
            texto_surface = font.render(letra, True, BLANCO)
            texto_surface.set_alpha(self.alpha)  # Ajustar opacidad
            screen.blit(texto_surface, (self.x - texto_surface.get_width() // 2, self.y + i * ESPACIO_ENTRE_LETRAS))

    def fuera_de_pantalla(self):
        return self.y > ALTO or self.alpha <= 0  # Sale de pantalla o desaparece completamente

# Lista de frases activas
frases_activas = []
espacios_ocupados = [False] * COLUMNAS  # Control de las columnas disponibles

# Función para generar fondo abstracto
def fondo_abstracto(tiempo):
    for y in range(0, ALTO, 5):
        for x in range(0, ANCHO, 5):
            # Generación de colores con tonos azul, violeta y rosa palo
            base_azul = int(100 + 155 * math.sin((x + tiempo) * 0.01))
            azul = max(0, min(255, base_azul))
            violeta = max(0, min(50, base_azul - 50)) if random.random() < 0.2 else 0
            rosa = max(0, min(50, base_azul - 100)) if random.random() < 0.1 else 0
            color = (azul // 2, violeta, azul + rosa)  # Mezcla tonos de azul, violeta y rosa palo
            color = tuple(max(0, min(255, c)) for c in color)  # Asegurar rango válido
            pygame.draw.circle(screen, color, (x, y), 3)  # Dibujar partículas suaves

# Bucle principal
reloj = pygame.time.Clock()
corriendo = True
tiempo = 0  # Control del tiempo para el fondo
while corriendo:
    screen.fill(NEGRO)  # Fondo negro (opcional para borrar)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Dibujar el fondo abstracto
    fondo_abstracto(tiempo)
    tiempo += 1  # Incrementar el tiempo para animar el fondo

    # Añadir frases nuevas con un tiempo de espera mayor
    if len(frases_activas) < FRASES_SIMULTANEAS and random.random() < 0.002:
        for columna in range(COLUMNAS):
            if not espacios_ocupados[columna]:
                nueva_frase = Frase(random.choice(frases_invertidas), columna)
                frases_activas.append(nueva_frase)
                espacios_ocupados[columna] = True
                break

    # Actualizar y dibujar las frases activas
    for frase in frases_activas[:]:
        frase.mover()
        frase.dibujar()
        if frase.fuera_de_pantalla():
            espacios_ocupados[frase.columna] = False
            frases_activas.remove(frase)

    # Actualizar la pantalla
    pygame.display.flip()
    reloj.tick(FPS)

pygame.quit()

