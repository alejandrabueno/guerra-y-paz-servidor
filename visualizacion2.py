import pygame
import random
import requests

# Configuración de la pantalla
ESCALA = 0.25  # Factor de escala
ANCHO = int(800 * ESCALA)
ALTO = int(4800 * ESCALA)  # Mantener tamaño vertical de lluvia.py
FPS = 60

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Visualización de Frases con Lluvia")
font_frase = pygame.font.Font(None, int(80 * ESCALA))
font_letras = pygame.font.Font(None, int(50 * ESCALA))

# Colores
NEGRO = (0, 0, 0)
AZUL = (0, 128, 255)
AZUL_BRILLANTE = (0, 150, 255)

# Función para obtener la frase del servidor e invertirla
def obtener_frase():
    try:
        response = requests.get("http://127.0.0.1:5000/obtener_frase")
        if response.status_code == 200:
            data = response.json()
            frase = data.get("frase", "")
            print(f"Frase recibida: {frase}")  # Depuración
            return [letra for palabra in frase.split()[::-1] for letra in palabra[::-1]]  # Invertir y separar letras en vertical
    except Exception as e:
        print(f"Error al obtener la frase: {e}")
    return []

# Clase para la lluvia de letras
class Letra:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidad = random.randint(2, 5)
        self.letra = chr(random.randint(65, 90))  # Letras aleatorias

    def mover(self):
        self.y += self.velocidad
        if self.y > ALTO:
            self.y = random.randint(-100, -10)
            self.x = random.randint(0, ANCHO)
            self.velocidad = random.randint(2, 5)
            self.letra = chr(random.randint(65, 90))

    def dibujar(self):
        screen.blit(font_letras.render(self.letra, True, AZUL_BRILLANTE), (self.x, self.y))

# Crear lluvia de letras
lluvia = [Letra(random.randint(0, ANCHO), random.randint(-ALTO, 0)) for _ in range(100)]

# Configuración inicial
frase = []
posiciones_frase = []

# Bucle principal
reloj = pygame.time.Clock()
corriendo = True

while corriendo:
    screen.fill(NEGRO)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            frase = obtener_frase()
            posiciones_frase = [(ANCHO // 2, -len(frase) * 40 + i * 40) for i in range(len(frase))]  # Letras en columna vertical
    
    # Dibujar lluvia de letras
    for letra in lluvia:
        letra.mover()
        letra.dibujar()
    
    # Dibujar la frase cayendo en vertical
    if frase:
        for i, letra in enumerate(frase):
            texto_surface = font_frase.render(letra, True, AZUL)
            screen.blit(texto_surface, (ANCHO // 2 - texto_surface.get_width() // 2, posiciones_frase[i][1]))
            posiciones_frase[i] = (posiciones_frase[i][0], posiciones_frase[i][1] + 2)  # Movimiento de caída
    
    pygame.display.flip()
    reloj.tick(FPS)

pygame.quit()

