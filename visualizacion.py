import pygame
import requests

# Configuración inicial de Pygame
pygame.init()
screen = pygame.display.set_mode((100, 1250))  # Ajusta el tamaño según tus necesidades
pygame.display.set_caption("Visualización de Frases")
font = pygame.font.Font(None, 50)

# Variables
frase = ""

# Función para obtener la frase del servidor
def obtener_frase():
    global frase
    try:
        response = requests.get("http://127.0.0.1:5000/obtener_frase")
        if response.status_code == 200:
            data = response.json()
            frase = data.get("frase", "")
    except Exception as e:
        print(f"Error al obtener la frase: {e}")


# Bucle principal de Pygame
reloj = pygame.time.Clock()
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Obtener la frase del servidor
    obtener_frase()

    # Dibujar en la pantalla
    screen.fill((0, 0, 0))  # Fondo negro
    texto_surface = font.render(frase, True, (255, 255, 255))
    screen.blit(texto_surface, (50, 300))  # Ajusta la posición según tus necesidades

    # Actualizar la pantalla
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
