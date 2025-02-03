import subprocess

# Ruta del video en el escritorio de Mac
video1_path = "/Users/alejandra/Desktop/mi_video1.mp4"

# Ruta correcta de VLC en macOS (instalado con Homebrew)
vlc_path = "/opt/homebrew/bin/vlc"

# Función para reproducir el video con VLC
def reproducir_video(video_path):
    subprocess.run([vlc_path, "--fullscreen", "--play-and-exit", video_path])

# Ejecutar la reproducción
reproducir_video(video1_path)
