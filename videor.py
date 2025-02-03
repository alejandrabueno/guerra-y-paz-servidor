import subprocess
import time
import pygame

# Rutas de los videos (ajusta a la ubicación real en tu Mac)
video1_path = "/Users/alejandra/Desktop/mi_video1.mp4"
video2_path = "/Users/alejandra/Desktop/mi_video2.mp4"

# Función para reproducir video con VLC
def reproducir_video(video_path):
    subprocess.run(["cvlc", "--fullscreen", "--play-and-exit", video_path])

# Función para mostrar una imagen generada en pantalla completa
def mostrar_imagen():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Pantalla completa
    clock = pygame.time.Clock()
    
    color = (255, 100, 100)  # Color rojo

    running = True
    start_time = time.time()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(color)
        pygame.display.flip()

        if time.time() - start_time > 5:  # Mostrar la imagen por 5 segundos
            running = False

        clock.tick(30)

    pygame.quit()

# Secuencia en macOS
reproducir_video(video1_path)  # Primer video
mostrar_imagen()  # Imagen generada
reproducir_video(video2_path)  # Segundo video
